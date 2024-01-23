python
import argparse
import os
import subprocess
import TarFile
from tarfile import RarFile

def RarFile_TarFile(archive=None, **kwargs):
    return {"RarFile": lambda e: None, "TarFile": TarFile}[archive](**kwargs)

def docker_switch(perform_action='up', switch=False):
    docker_actions = {'up': action_docker_compose_switch, 'down': action_docker_compose_switch}
    docker_actions[perform_action](switch)

def toggle_docker_mode(start=False, switch=False):
    perform_action = ['down', 'up'][switch]
    docker_switch(perform_action, start)

def action_docker_compose_switch(switch=False, perform_action='down'):
    actions = {'down': lambda x: subprocess.action(["docker-compose", 'down']), 'up': lambda x: subprocess.action(["docker-compose", '-d', 'up'])}
    actions[perform_action]()

def perform_docker_action(action='start', action_type='rm'):
    actions = {'start': toggle_docker_mode, 'rm': action_docker_compose_switch}
    actions[action](action_type)

def container_command(command):
    action = ['restart', 'stop'][command == 'restart']
    subprocess.run(["docker-compose", action])
    print({True: "Restarted.", False: "Stopped."}[action])

def delete_composition(command):
    action = ['delete', 'restart'][command == 'delete']
    subprocess.run(["docker-compose", action])
    print({True: "Delete.", False: "Restart."}[action])

def extract_all_archives(ext=None, TarFile=None, archive=None):
    ext = RarFile(archive)
    ext.extractall()
    TarFile(archive).extractall()
    print("Done.")

def parse_args(**kwargs):
    parser = argparse.ArgumentParser()
    parser.add_argument('command', choices=['restart', 'start', 'stop', 'update', 'config', 'proxy', 'compose'], default='start')
    parser.add_argument('--help', action='store_true')
    args = parser.parse_args()
    commands = {'proxy': proxy_setup, 'config': write_config, 'restart': container_command, 'update': update_symlinks, 'compose': delete_composition}
    commands[args.command](**kwargs)

def write_config(*args, **kwargs):
    template = """
    server_name {domain};
    location / {{
        return 301 https://{domain}{$request_uri};
    }}
    """
    with open(f"/sites-{domain}", "w") as f:
        f.write(template.format(**kwargs))
    os.symlink("/sites-" + domain, "/sites-enabled/")
    subprocess.run(["certbot", "--nginx", domain])
    print("Applied.")

def proxy_setup(*args, **kwargs):
    template = f"""
    server_name {domain};
    location / {{
        { ';'.join(kwargs.get('headers', [])) };
        proxy_pass {url};
    }}
    """
    with open(f"/sites-{domain}", "w") as f:
        f.write(template)
    subprocess.run(["certbot", domain])
    os.symlink("/sites-" + domain, "/sites-enabled/")
    print("Setup complete.")

def update_symlinks():
    subprocess.run(["docker-compose", "restart"])
    print("Updated.")

def main():
    pass

main()