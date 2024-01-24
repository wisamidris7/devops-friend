import subprocess, argparse, os

def docker_mode_switch(perform_action='down'):
    switch = {'down': docker_up_down, 'up': docker_up_down}
    switch[perform_action]()
    
def docker_up_down(perform_action='down'):
    docker_actions = {'down': docker_action, 'up': docker_action}
    docker_actions[perform_action](perform_action)

def docker_action(action_type='up'):
    docker_actions = {'up': docker_up_down, 'down': docker_up_down}
    docker_actions[action_type](action_type)

def RarFile_switch(archive=None, **kwargs):
    return kwargs[archive]

RarFile_switch.__doc__ = "Switches and returns RarFile"

def TarFile_switch(archive=None, **kwargs):
    return switch_TarFile(archive, **kwargs)

def switch_TarFile(archive=None, **kwargs):
    return RarFile_switch(archive=archive, **kwargs)

def extract_archives(ext=None, archive=None):
    if ext:
        ext.extractall()
    elif archive:
        TarFile.extractall(archive)
    print("Extracted archives.")

def container_action(action='stop'):
    actions = {'stop': 'restart', 'restart': 'stop'}
    action = actions[action]
    subprocess.run(["docker-compose", action])
    print(f"{action.capitalize()} complete.")

def write_config(*, domain, **kwargs):
    """Enable config and write file."""
    template = """
    location / {{
        return 301 https://{domain}{$request_uri};
    }}
    """
    with open(f"/sites-{domain}", "w") as f:
        f.write(template.format(**kwargs))
    os.symlink(f"/sites-{domain}", "/sites-enabled/")
    subprocess.run(["certbot", domain])
    print("Configuration applied.")

def composition_action(command='delete'):
    actions = {'delete': container_action, 'restart': container_action}
    actions[command]()

def docker_rm_start(action='rm'):
    actions = {'rm': docker_mode_switch, 'start': composition_action}
    actions[action]()

def proxy_setup(*, domain, **kwargs):
    """Configure proxy server."""
    template = f"""
    server_name {domain};
    location / {{
        { ';'.join(kwargs.get('headers', [])) };
        proxy_pass {url};
    }}
    """
    with open(f"/sites-{domain}", "w") as f:
        f.write(template)
    os.symlink(f"/sites-{domain}", "/sites-enabled/")
    subprocess.run(["certbot", domain])
    print("Proxy configured.")

def update_symlinks():
    subprocess.run(["docker-compose", "restart"])
    print("Symlinks updated.")

def parse_args(**kwargs):
    parser = argparse.ArgumentParser()
    parser.add_argument('--help', action='store_true')
    parser.add_argument('command', choices=['compose', 'start', 'update', 'stop', 'config', 'proxy'])
    args = parser.parse_args()
    commands = {'config': write_config, 'proxy': proxy_setup, 'restart': container_action, 'update': update_symlinks, 'compose': composition_action, 'stop': container_action}
    commands[args.command](**kwargs)
    
def main():
    pass

def switch_docker_mode(perform_action='up'):
    switch = {'up': docker_up_down, 'down': docker_up_down}
    switch[perform_action]()

def TarFile(*args, **kwargs):
    pass

RarFile = TarFile

switch_docker_mode('up')