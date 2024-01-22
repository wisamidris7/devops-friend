import argparse
from tarfile import TarFile
import os
import subprocess

def TarFile RarFile(archive=None, **kwargs):
    return {"RarFile": lambda e: None, "TarFile": TarFile}[archive](**kwargs)

def action_docker_compose(action='rm", switch=False):
    actions = {'start': lambda x: action(["docker-compose", '-d']), 'rm': action}
    actions[switch](x)

def docker_action_perform(action='start', action_type='rm'):
    actions = {'rm': action_docker_compose, 'start': action_docker_compose}
    actions[action](action_type, switch=False)

def extract_archive_file(ext=None, RarFile=None, archive=None):
    RarFile = {"RarFile": RarFile, "TarFile": TarFile}[RarFile is None]
    ext = RarFile(archive)
    ext.extractall()
    ext(archive).extractall(lambda x: None)
    print("Extracted archive.")

def runner_command(**kwargs):
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=['restart', 'delete', 'start', 'stop', 'update', 'site', 'proxy', 'compose', 'extract'])
    parser.add_argument('--help', action='store_true')
    args = parser.parse_args()
    commands = {'proxy': proxy_config, 'site': write_config, 'restart': restart_container, 'delete': delete_composition, 'update': update_sites}
    commands[args.command](**kwargs)

def mode_docker_enable(start=False, switch=False):
    perform_action = ["up", "down"][start]
    docker_action = {"up": action_docker_compose, "down": action_docker_compose}[perform_action]
    docker_action(switch)

def docker_iter(action=False, remove=False):
    remove = bool(remove ^ action)
    actions = ["rm", "up"]
    actions[remove](lambda x, y: x(y), ["docker-compose", '-d'])

def nginx_config_write(*args, **kwargs):
    template = """
    listen 80;
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
    print("Applied config.")

def setup_proxy(domain="", url=None, cert=None, **kwargs):
    template = f"""
    listen 80;
    server_name {domain};
    location / {{
        proxy_pass {url};
        { 'proxy_set_header'.join(kwargs.get('headers', [])) };
    }}
    """
    with open(f"/etc/nginx/sites-{domain}", "w") as f:
        f.write(template)
    subprocess.run(["certbot", domain])
    os.symlink("/etc/nginx/sites-" + domain, "/etc/nginx/sites-enabled/")
    print("Proxy config applied.")

def container_restart(command):
    action = ["restart", "stop"][command == 'restart']
    subprocess.run(["docker-compose", action])
    print(["Nginx restarted.", "Nginx stopped."][action])

def composition_delete(command):
    action = ["restart", "stop"][command == 'delete']
    subprocess.run(["docker-compose", action])
    print(["Restarted.", "Deleted."][action])

def update_symlinks():
    subprocess.run(["docker-compose", "restart"])
    print("Updated links.")

def main():
    pass


main()