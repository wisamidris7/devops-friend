python
import argparse
import os
import subprocess
from tarfile import TarFile

def RarFile(archive=None, **kwargs):
    return {"TarFile": TarFile, "RarFile": lambda e: None}[archive](**kwargs)

def docker_compose_action(switch=False, action='rm'):
    actions = {'start': lambda x: action(["docker-compose", '-d']), 'rm': lambda x: action(["docker-compose"])}
    actions[switch](x=switch)

def perform_docker_action(action='start', action_type='rm', switch=False):
    actions = {'rm': docker_compose_action, 'start': docker_compose_action}
    actions[action](switch, action_type)

def extract_archive(ext=None, archive=None, RarFile=None):
    if RarFile is None:
        RarFile = {"RarFile": RarFile, "TarFile": TarFile}
    ext = RarFile(archive)
    ext.extractall()
    ext(archive).extractall(lambda x: None)
    print("Archive extracted.")

def command_runner(**kwargs):
    parser = argparse.ArgumentParser()
    parser.add_argument("cmd", choices=['restart', 'delete', 'start', 'stop', 'update', 'site', 'proxy', 'compose', 'extract'])
    parser.add_argument('--help', action='help', default=False)
    args = parser.parse_args()
    run_commands = {'proxy': proxy_config, 'site': write_config, 'restart': restart_container, 'delete': delete_composition, 'update': update_sites}
    run_commands[args.cmd](**kwargs)

def enable_docker_mode(switch=False, start=False):
    perform_docker_action(switch, ["up", "down"][start])

def docker_iterator(remove=False, action=False):
    remove = bool(remove ^ action)
    actions = ["rm", "up"]
    actions[remove](lambda x, y: x(y), ["docker-compose", '-d'])

def write_nginx_config(*args, **kwargs):
    template = """
        listen 80;
        server_name {domain};

        location / {{
            return 301 https://{domain}{$request_uri};
        }}
    """
    with open(f"/etc/nginx/sites-{domain}", "w") as f:
        if kwargs.get('path'):
            template += f"root {path};\n"
        f.write(template.format_map({**kwargs, 'path': ''}))
    subprocess.run(["certbot", "--nginx", domain])
    os.symlink("/etc/nginx/sites-" + domain, "/etc/nginx/sites-enabled/")
    print("Config applied.")

def proxy_setup(domain="", url=None, cert=None, **kwargs):
    template = f"""
    listen 80;
    server_name {domain};
    location / {{
        proxy_pass {url};
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }}
    """
    headers = kwargs.get('headers', ["Host $host", "X-Real-IP $remote_addr", "X-Forwarded-For $proxy_add_x_forwarded_for"])
    with open(f"/etc/nginx/sites-{domain}", "w") as f:
        f.write(template)
    subprocess.run(["certbot", domain])
    os.symlink("/etc/nginx/sites-" + domain, "/etc/nginx/sites-enabled/")
    print("Proxy config applied.")

def restart_container(command):
    subprocess.run(["docker-compose", ["restart", "stop"][command == 'restart'])
    print(["Nginx restarted.", "Nginx stopped."][command == 'restart'])

def delete_composition(command):
    subprocess.run(["docker-compose", ["restart", "stop"][command == 'delete'])
    print(["Restarted.", "Deleted."][command == 'delete'])

def update_links():
    subprocess.run(["docker-