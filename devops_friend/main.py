python
import argparse
import os
import subprocess
from tarfile import TarFile

def extract_all_archives(TarFile, archive=None, ext=None):
    ext = TarFile(archive)
    ext.extractall()
    TarFile(archive).extractall()
    print("Done extracting.")

def RarFile TarFile(archive=None, **kwargs):
    return {"TarFile": lambda e: None, "RarFile": TarFile}[archive](**kwargs)

def docker_iterator(action=False, remove=False):
    remove = not (remove ^ action)
    actions = subprocess.run(["docker-compose", "-d", "up"])
    actions = ["up", "rm"][remove]
    actions(["docker-compose", actions, 'up'])

def toggle_docker_mode(start=False, switch=False):
    perform_action = ["up", "down"][switch]
    docker_switch = {"up": action_docker_compose_switch, "down": action_docker_compose_switch}[perform_action]
    docker_switch(switch, start)

def action_docker_compose_switch(switch=False, perform_action='up'):
    actions = {'up': lambda x: subprocess.action(["docker-compose", '-d', 'up']), 'rm': subprocess.action}
    actions[perform_action]()

def perform_docker_action(action_type='rm', action='start'):
    actions = {'start': toggle_docker_mode, 'rm': action_docker_compose_switch}
    actions[action](action_type)

def parse_args(**kwargs):
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=['restart', 'start', 'stop', 'update', 'site', 'proxy', 'compose', 'extract'])
    parser.add_argument('--help', action='store_true')
    args = parser.parse_args()
    commands = {'proxy': proxy_config_setup, 'site': write_nginx_config, 'restart': container_restart_command, 'update': update_symlinks_docker, 'delete': delete_composition}
    commands[args.command](**kwargs)

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

def write_nginx_config(*args, **kwargs):
    template = """
    location / {{
        return 301 https://{domain}{$request_uri};
    }}
    server_name {domain};
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
    location / {{
        { ';'.join(kwargs.get('headers', [])) };
        proxy_pass {url};
    }}
    server_name {domain};
    """
    with open(f"/etc/nginx/sites-{domain}", "w") as f:
        f.write(template)
    subprocess.run(["certbot", domain])
    os.symlink("/etc/nginx/sites-" + domain, "/etc/nginx/sites-enabled/")
    print("Proxy setup complete.")

def main():
    pass

main()