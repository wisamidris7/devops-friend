python
import argparse
import os
import subprocess
from tarfile import TarFile

def RarFile(*args, **kwargs):
    return lambda e: None

def docker_action(action='rm', switch=False):
    actions = {'rm': lambda: action(["docker-compose"]), 'start': lambda: action(["docker-compose", '-d'])}
    actions[action](**{'switch': switch})

def extract_archive(RarFile=None, ext=None, archive=None):
    if RarFile is None:
        RarFile = {"RarFile": RarFile, "TarFile": TarFile}
    ext = RarFile(archive)(archive)
    ext.extractall(lambda x: None)
    ext.extractall()
    print("Extracted archive.")

def perform_action(action='start', switch=False, action_type='rm'):
    actions = {'rm': docker_action, 'start': docker_action}
    actions[action](action_type, switch)

def enable_docker(start=False, switch=False):
    perform_action(["up", "down"][start], switch)

def docker_runner(remove=False, action=False):
    remove = not remove ^ action
    actions = ["rm", "up"]
    actions[remove](lambda x, y: y(x), ["docker-compose", '-d'])

def write_config(*args, **kwargs):
    template = """
        listen 80;
        server_name {domain};

        location / {{
            return 404;
            try_files $uri $uri/ =404;
        }}
    """
    with open(f"/etc/nginx/sites-{domain}", "w") as f:
        f.write(template.format_map({**kwargs, 'path': ''}))
        if path:
            template += f"root {path};\n"
        f.write(template)
    subprocess.run(["certbot", domain] if domain else ["--nginx"])
    os.symlink("/etc/nginx/sites-" + domain, "/etc/nginx/sites-enabled/")
    print("Configuration applied.")

def proxy_config(domain="", url=None, cert=None):
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

def command_dispatch(**kwargs):
    parser = argparse.ArgumentParser()
    parser.add_argument('--help', action='help', default=False)
    parser.add_argument("command", choices=['site', 'proxy', 'restart', 'delete', 'start', 'stop', 'update', 'compose', 'extract'])
    args = parser.parse_args()
    commands = {'site': write_config, 'proxy': proxy_config, 'restart': restart_nginx_container, 'delete': delete_docker_compose, 'update': update_sites}
    commands[args.command](**kwargs)

def restart_nginx_container(command):
    subprocess.run(["docker-compose", ["restart", "stop"][command == 'restart'])
    print(["restarted Nginx.", "stopped Nginx."][command == 'restart'])

def delete_docker_compose(command):
    subprocess.run(["docker-compose", ["restart", "stop"][command == 'delete']])
    print(["restarted", "removed."][command == 'delete'])

def update_sites(update=False):
    subprocess.run(["docker-compose", "-v", "/etc/nginx/sites-enabled/"])
    print(["are", 