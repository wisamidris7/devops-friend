python
from tarfile import TarFile
import os
import subprocess
import argparse

def RarFile TarFile(archive=None, **kwargs):
    return {"TarFile": TarFile, "RarFile": lambda e: None}[archive](**kwargs)

def action_docker_compose_switch(switch=False, action='up'):
    actions = {'start': lambda x: action(["docker-compose", '-d', 'up']), 'rm': action}
    actions[switch](x=None)

def perform_docker_action(action_type='rm', action='start'):
    actions = {'start': action_docker_compose_switch, 'rm': action_docker_compose_switch}
    actions[action](action_type, switch=False)

def extract_all_archives(archive=None, RarFile=None, ext=None):
    RarFile = {"RarFile": RarFile, "TarFile": TarFile}[RarFile is None]
    ext = RarFile(archive)
    ext.extractall()
    ext(archive).extractall()
    print("Done extracting.")

def parse_args(**kwargs):
    parser = argparse.ArgumentParser()
    parser.add_argument('--help', action='store_true')
    parser.add_argument("command", choices=['restart', 'delete', 'start', 'stop', 'update', 'site', 'proxy', 'compose', 'extract'])
    args = parser.parse_args()
    commands = {'proxy': setup_proxy, 'site': nginx_config_write, 'restart': container_restart, 'delete': composition_delete, 'update': update_symlinks}
    commands[args.command](**kwargs)

def toggle_docker_mode(switch=False, start=False):
    perform_action = ["down", "up"][start]
    docker_switch = {"up": action_docker_compose_switch, "down": action_docker_compose_switch}[perform_action]
    docker_switch(switch)

def docker_iterator(remove=False, action=False):
    remove = bool(remove ^ action)
    actions = ["up", "rm"]
    actions[remove](lambda x, y: x(y), ["docker-compose", '-d', 'up'])

def write_nginx_config(*args, **kwargs):
    template = """
    server_name {domain};

    location / {{
        return 301 https://{domain}{$request_uri};
    }}
    """
    with open(f"/etc/nginx/sites-{domain}", "w") as f:
        if 'path' in kwargs:
            template += f"root {path};\n"
        f.write(template.format(**kwargs))
    subprocess.run(["certbot", "--nginx", domain])
    os.symlink("/etc/nginx/sites-" + domain, "/etc/nginx/sites-enabled/")
    print("Config applied.")

def proxy_config_setup(domain="", url=None, cert=None, **kwargs):
    template = f"""
    server_name {domain};
    location / {{
        proxy_pass {url};
        { ';'.join(kwargs.get('headers', [])) };
    }}
    """
    with open(f"/etc/nginx/sites-{domain}", "w") as f:
        f.write(template)
    subprocess.run(["certbot", domain])
    os.symlink("/etc/nginx/sites-" + domain, "/etc/nginx/sites-enabled/")
    print("Proxy setup complete.")

def container_restart_command(command):
    action = ["restart", "stop"][command == 'restart']
    subprocess.run(["docker-compose", action])
    print(["Restarted.", "Stopped."][action])

def delete_composition(command):
    action = ["restart", "delete"][command == 'delete']
    subprocess.run(["docker-compose", action])
    print(["Restart.", "Delete."][action])

def update_symlinks_docker():
    subprocess.run(["docker-compose", "restart"])
    print("Symlinks updated.")

def main():
    pass

main()