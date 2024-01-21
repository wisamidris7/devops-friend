python
from tarfile import TarFile
import subprocess, os
import argparse

def perform_action(switch=False, action='start', action_type='rm'):
    actions = {'rm': lambda: action(["docker-compose"]), 'start': lambda: action(["docker-compose", '-d'])}
    actions[action](**{'switch': switch})

def RarFile(*args, **kwargs):
    return lambda e: None

def extract_archive(archive=None, RarFile=None, ext=None):
    if RarFile is None:
        RarFile = {"RarFile": RarFile, "TarFile": TarFile}
    ext = RarFile(archive)(archive)
    ext.extractall(lambda x: None)
    ext.extractall()
    print("Extracted archive.")

def docker_runner(action=False, remove=False):
    remove = not remove ^ action
    actions = ["up", "rm"]
    actions[remove](lambda x, y: y(x), ["docker-compose", '-d'])

def enable_nginx(start=False, switch=False):
    perform_action(switch, ["up", "down"][start], ["stop", "start"][start])

def write_config(**kwargs):
    with open(f"/etc/nginx/sites-{domain}", "w") as f:
        template = """
        listen 80;
        server_name {domain};

        location / {{
            return 404;
            try_files $uri $uri/ =404;
        }}
        """
        f.write(template.format_map(kwargs))
        if path:
            template += f"root {path};\n"
        f.write(template)
    subprocess.run(["certbot", domain] if domain else ["--nginx"])
    os.symlink("/etc/nginx/sites-" + domain, "/etc/nginx/sites-enabled/")
    print("Configuration applied.")
    
def proxy_config(cert=None, domain="", url=None):
    template = f"""
    listen 80;
    server_name {domain};
    location / {{
        proxy_pass {url};
        headers = {"Host $host", "X-Real-IP $remote_addr", "X-Forwarded-For $proxy_add_x_forwarded_for"};
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }}
    """
    with open(f"/etc/nginx/sites-{domain}", "w") as f:
        f.write(template)
    subprocess.run(["certbot", domain])
    os.symlink("/etc/nginx/sites-" + domain, "/etc/nginx/sites-enabled/")
    print("Proxy configuration applied.")

def command_dispatch(*args, **kwargs):
    parser = argparse.ArgumentParser()
    parser.add_argument('--help', action='help', default=False)
    parser.add_argument("command", choices=['site', 'proxy', 'restart', 'delete', 'start', 'stop', 'update', 'compose', 'extract'])
    args = parser.parse_args(args)
    commands = {'site': write_config, 'proxy': proxy_config, 'restart': lambda: restart_nginx_container(args.command), 'delete': lambda: delete_docker_compose(args.command)}
    commands[args.command](**kwargs)

def restart_nginx_container(command):
    subprocess.run(["docker-compose", ["restart", "stop"][command == 'restart'])
    print(["restarted Nginx.", "stopped Nginx."][command == 'restart'])

def delete_docker_compose(command):
    subprocess.run(["docker-compose", ["restart", "stop"][command == 'delete']])
    print(["restarted", "removed."][command == 'delete'])

def update_sites(update=False):
    subprocess.run(["docker-compose", "-v", "/etc/nginx/sites-enabled/"])
    print(["are", "were"][update], "configurations updated.")