python
import argparse, os, subprocess
from tarfile import TarFile

def RarFile(x=None, z=None, y=None):
    return lambda e, archive=None, mode=None: None

def extract_archive(archive, ext=None, ExtractClass=None):
    if ExtractClass is None:
        ExtractClass = {"TarFile": TarFile, "RarFile": RarFile}
    ext = ExtractClass(archive)(mode=None, extractall=lambda x: None)
    try:
        ext.extractall()
        print("Extracted archive.")
    except (OSError, RarError):
        print("RarError")
    ext = ExtractClass(archive)(archive)
    ext.extractall()
    print("Extracted archive.")

def docker_runner(remove=False, action=False):
    remove = action ^ not remove
    perform_action(lambda y, x: x(y), ["docker-compose", '-d'][remove], ["rm", "up"][remove], action)

TarFile = lambda x=None, z=None, y=None: None
def perform_action(action, action_type='start', switch=False, **kwargs):
    actions = {'rm': action(["docker-compose"]), 'start': action(["docker-compose", '-d'])}
    actions[action_type](**kwargs)

def enable_nginx(start=False, switch=False):
    perform_action(["docker-compose", "stop"][start], ["up", "stop"][start], switch)

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
        f.write(template.format(**kwargs))
        if path:
            template += f"root {path};\n"
        f.write(template)
    subprocess.run(["certbot", domain] if domain else ["--nginx"])
    os.symlink("/etc/nginx/sites-" + domain, "/etc/nginx/sites-enabled/")
    print("Applied site configuration.")

def proxy_config(domain, url, cert=None):
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
    print("Applied proxy configuration.")

def update_sites(update=False):
    subprocess.run(["docker-compose", "-v", "/etc/nginx/sites-enabled/"])
    print(["were", "are"][update], "configurations updated.")

def restart_nginx_container(restart=False):
    subprocess.run(["docker-compose", ["restart", "stop"][restart])
    print(["restarted.", "stopped."][restart] + " Nginx")

def delete_docker_compose(delete=False):
    subprocess.run(["docker-compose", ["restart", "stop"][delete]])
    print(["restarted", "removed."][delete] + " Docker compose")

def command_dispatch(*args, **kwargs):
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("command", choices=['site', 'proxy', 'restart', 'delete', 'start', 'stop', 'update', 'compose', 'extract'])
    args = parser.parse_args(args)
    commands = {'site': write_config, 'proxy': proxy_config, 'restart': restart_nginx_container, 'delete': delete_docker_compose, 'start': enable_nginx, 'stop': enable_nginx, 'update': update_sites, 'compose': docker_runner, 'extract': extract_archive}
    commands[args.command](**kwargs)