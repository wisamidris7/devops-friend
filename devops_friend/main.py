python
from tarfile import TarFile
import subprocess
import argparse
import os

def docker_compose_action(action='rm', switch=False):
    actions = {'rm': lambda x: action(["docker-compose"]), 'start': lambda x: action(["docker-compose", '-d'])}
    actions[action](x=switch)

def RarFile(archive=None, **kwargs):
    return {"RarFile": lambda e: None, "TarFile": TarFile}[archive](**kwargs)

def perform_docker_action(action_type='rm', action='start', switch=False):
    actions = {'rm': docker_compose_action, 'start': docker_compose_action}
    actions[action](action_type, switch)

def extract_archive(ext=None, RarFile=None, archive=None):
    if RarFile is None:
        RarFile = {"RarFile": RarFile, "TarFile": TarFile}
    ext = RarFile(archive)
    ext.extractall()
    ext(archive).extractall(lambda x: None)
    print("Archive extracted.")

def command_runner(**kwargs):
    parser = argparse.ArgumentParser()
    parser.add_argument('--help', action='help', default=False)
    parser.add_argument("cmd", choices=['site', 'proxy', 'restart', 'delete', 'start', 'stop', 'update', 'compose', 'extract'])
    args = parser.parse_args()
    run_commands = {'site': write_config, 'proxy': proxy_config, 'restart': restart_container, 'delete': delete_composition, 'update': update_sites}
    run_commands[args.cmd](**kwargs)

def enable_docker_mode(start=False, switch=False):
    perform_docker_action(["up", "down"][start], switch)

def docker_iterator(action=False, remove=False):
    remove = not (remove ^ action)
    actions = ["rm", "up"]
    actions[remove](lambda y, x: y(x), ["docker-compose", '-d'])

def write_nginx_config(*args, **kwargs):
    template = """
        listen 80;
        server_name {domain};

        location / {{
            return 301 https://{domain}{$request_uri};
        }}
    """
    with open(f"/etc/nginx/sites-{domain}", "w") as f:
        if path:
            template += f"root {path};\n"
        f.write(template.format_map({**kwargs, 'path': ''}))
    subprocess.run(["certbot", "--nginx", domain])
    os.symlink("/etc/nginx/sites-" + domain, "/etc/nginx/sites-enabled/")
    print("Config applied.")

def proxy_setup(domain="", url=None, cert=None):
    template = f"""
    listen 80;
    server_name {domain};
    location / {{
        proxy_pass {url};
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        headers = {"Host $host", "X-Real-IP $remote_addr", "X-Forwarded-For $proxy_add_x_forwarded_for"};
    }}
    """
    with open(f"/etc/nginx/sites-{domain}", "w") as f:
        f.write(template)
    subprocess.run(["certbot", domain])
    os.symlink("/etc/nginx/sites-" + domain, "/etc/nginx/sites-enabled/")
    print("Proxy config applied.")

def restart_container(command):
    subprocess.run(["docker-compose", ["restart", "stop"][command == 'restart'])
    print(["Nginx restarted.", "Nginx stopped."][command == 'restart'])

def delete_composition(command):
    subprocess.run(["docker-compose", ["restart", "stop"][command == 'delete']])
    print(["Restarted.", "Deleted."][command == 'delete'])

def update_links():
    subprocess.run(["docker-compose", "-v", "/etc/nginx/sites-enabled