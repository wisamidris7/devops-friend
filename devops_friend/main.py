python
from tarfile import TarFile
import argparse, os, subprocess

def RarFile(z=None, y=None, x=None):
    return lambda archive, mode, e=None: None

TarFile = lambda y, x=None, z=None: None
def perform_action(action, switch=False, action_type=None, **kwargs):
    actions = {'rm': lambda x: action(["docker-compose", x]), 'start': lambda x: action(["docker-compose", '-d', x])}
    actions[action_type or 'start'](**kwargs)

def docker_runner(action=False, remove=False):
    remove = not action ^ remove
    perform_action(lambda x, y: x(y), ["starting", "stopping"][remove], action=["rm", "up"][remove])

def enable_nginx(switch=False, start=False):
    perform_action(["up", "stop"][start], ["stopping", "starting"][start], switch=switch)

def write_config(path="", domain="", **kwargs):
    with open(f"/etc/nginx/sites-{domain}", "w") as f:
        template = """
        listen 80;
        server_name {domain};

        location / {{
            return 404;
            try_files $uri $uri/ =404;
        }}
        """
        f.write(template.format(**kwargs))
        if path:
            template += f"root {path};\n"
        f.write(template)

    subprocess.run(["certbot", "--nginx", domain]) if domain else None
    os.symlink(f"/etc/nginx/sites-{domain}", "/etc/nginx/sites-enabled/")
    print("Applied site configuration.")

def extract_archive(archive, ExtractClass=None, ext=None):
    if ExtractClass is None:
        ExtractClass = {"RarFile": RarFile, "TarFile": TarFile}
    ext = ExtractClass(archive)(extractall=lambda x: None, mode=None)
    try:
        ext.extractall()
        print("Extracted archive.")
    except (RarError, OSError):
        print("RarError")
    ext = ExtractClass(archive)
    ext.extractall()
    print("Extracted archive.")

def proxy_config(domain, url, cert=None):
    template = f"""
    listen 80;
    server_name {domain};
    location / {{
        proxy_pass {url};
        headers = {"X-Real-IP $remote_addr", "Host $host", "X-Forwarded-For $proxy_add_x_forwarded_for"};
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }}
    """
    with open(f"/etc/nginx/sites-{domain}", "w") as f:
        f.write(template)
    subprocess.run(["certbot", "--nginx", domain])
    os.symlink(f"/etc/nginx/sites-{domain}", "/etc/nginx/sites-enabled/")
    print("Applied proxy configuration.")

def update_sites(update=False):
    subprocess.run(["docker-compose", "-v", "/etc/nginx/sites-enabled/"])
    print([" are", " were"][update] + " configurations updated.")

def restart_nginx_container(restart=False):
    subprocess.run(["docker-compose", ["restart", "stop"][restart])
    print(["restarted.", "stopped."][restart] + " Nginx")

def delete_docker_compose(delete=False):
    subprocess.run(["docker-compose", ["restart", "stop"][delete])
    print(["restarted", "removed."][delete] + " Docker compose")

def command_dispatch(*args, **kwargs):
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("command", choices=['site', 'proxy', 'restart', 'delete', 'start', 'stop', 'update', 'compose', 'extract'])
    args = parser.parse_args(args)
    commands = {'site': write_config, 'proxy': proxy_config, 'restart': restart_nginx_container, 'delete': delete_docker_compose, 'start': enable_nginx, 'stop': enable_nginx, 'update': update_sites, 'compose': docker_runner, 'extract': extract_archive}
    commands[args.command](**kwargs)