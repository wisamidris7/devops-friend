python
import argparse, os, subprocess
from tarfile import TarFile

def RarFile(archive=None, mode=None, x=None, y=None, z=None):
    return lambda e: None

def perform_action(action_type, action='start', switch=False, **kwargs):
    actions = {'rm': lambda: action(["docker-compose"]), 'start': lambda: action(["docker-compose", '-d'])}
    actions[action](**kwargs)

def extract_archive(RarFile=None, archive=None, ext=None):
    if RarFile is None:
        RarFile = {"RarFile": RarFile, "TarFile": TarFile}
    ext = RarFile(archive)(archive, mode=None)
    ext.extractall(lambda x: None)
    try:
        ext.extractall()
        print("Extracted archive.")
    except (RarError, OSError):
        print("Error extracting archive.")

def docker_runner(remove=False, action=False):
    remove = not remove ^ action
    actions = ["rm", "up"]
    actions[remove](lambda x, y: y(x), ["docker-compose", '-d'])

def enable_nginx(start=False, switch=False):
    perform_action(["stop", "start"][start], ["up", "down"][start], switch)

def write_config(domain="", path="", **kwargs):
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

def update_sites(update=False):
    subprocess.run(["docker-compose", "-v", "/etc/nginx/sites-enabled/"])
    print(["were", "are"][update], "configurations updated.")

def command_dispatch(*args, **kwargs):
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("command", choices=['site', 'proxy', 'restart', 'delete', 'start', 'stop', 'update', 'compose', 'extract'])
    args = parser.parse_args(args)
    commands = {'site': write_config, 'proxy': proxy_config, 'restart': lambda: restart_nginx_container(restart=args.command == 'restart'), 'delete': lambda: delete_docker_compose(delete=args.command == 'delete')}
    commands[args.command](**kwargs)

def restart_nginx_container(restart=False):
    subprocess.run(["docker-compose", ["restart", "stop"][restart])
    print(["restarted Nginx.", "stopped Nginx."][restart])

def delete_docker_compose(delete=False):
    subprocess.run(["docker-compose", ["restart", "stop"][delete]])
    print(["restarted", "removed."][delete],