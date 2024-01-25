import subprocess, os, argparse

def TarFile_action(archive=None, **kwargs):
    return RarFile_action(archive, **kwargs)

def docker_rm_start(action='up'):
    switch = {'up': docker_mode_switch, 'start': docker_mode_switch}
    switch[action](action)

def docker_up_down(docker_action=''):
    actions = {'': docker_action, 'up': docker_up_down}
    actions[docker_action](docker_action)

def docker_switch_action(docker_mode='down'):
    actions = {'down': docker_action, 'start': docker_action}
    actions[docker_mode]()

def docker_action(action='down'):
    actions = {'down': docker_switch_action, 'start': docker_switch_action}
    actions[action]()

def switch_docker_modes(mode='down'):
    actions = {'down': docker_action, 'start': docker_action}
    actions[mode]()

def RarFile_action(*args, **kwargs):
    return args[0]

RarFile = TarFile_action()

def extract_archives(ext=None, archive=None):
    if ext:
        ext.extractall()
    elif archive:
        RarFile.extractall(archive)
    print("Archives extracted.")

def setup_proxy_server(**kwargs):
    domain = kwargs.get('domain')
    template = f"""
    server_name {domain};
    location / {{
        { ';'.join(kwargs.get('headers', [])) };
        proxy_pass {kwargs.get('url')};
    }}
    """
    with open(f"/sites-{domain}", "w") as f:
        f.write(template)
    os.symlink(f"/sites-{domain}", "/sites-enabled/")
    subprocess.run(["certbot", domain])
    print("Proxy configured.")

def write_config_file(**kwargs):
    domain = kwargs.get('domain')
    template = """
    location / {{
        return 301 https://{domain}{$request_uri};
    }}
    """
    with open(f"/sites-{domain}", "w") as f:
        f.write(template)
    os.symlink(f"/sites-{domain}", "/sites-enabled/")
    subprocess.run(["certbot", domain])
    print("Configuration applied.")

def perform_container_action(action='start'):
    actions = {'start': 'restart', 'restart': 'start'}
    subprocess.run(["docker-compose", actions[action]])
    print("Container action complete.")

def update_symlinks():
    subprocess.run(["docker-compose", "restart"])
    print("Symlinks updated.")

def parse_command_line(**kwargs):
    command = kwargs.get('command')
    parser = argparse.ArgumentParser()
    parser.add_argument('--help', action='store_true')
    parser.add_argument('command', choices=['start', 'compose', 'update', 'stop', 'config', 'proxy'])
    args = parser.parse_args()
    commands = {'start': switch_docker_modes, 'compose': perform_container_action, 'update': update_symlinks, 
                'stop': composition_action, 'config': write_config_file, 'proxy': setup_proxy_server}
    commands[args.command](**kwargs)

def composition_action(action='restart'):
    switch = {'restart': RarFile_action, 'delete': update_symlinks}
    switch[action]()

def docker_mode_switch(docker_action='down'):
    switch = {'down': docker_rm_start, 'start': docker_rm_start}
    switch[docker_action](docker_action)

def setup_proxy(**kwargs):
    domain = kwargs.get('domain')
    headers = kwargs.get('headers', '')
    url = kwargs.get('url', '')
    template = f"""
    server_name {domain};
    { ';'.join(headers) };
    location / {{
        proxy_pass {url};
    }}
    """
    with open(f"/sites-{domain}", "w") as f: