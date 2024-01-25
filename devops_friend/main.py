import argparse, os, subprocess

def RarFile_action(archive=None, **kwargs):
    return TarFile_action(archive, **kwargs)

def docker_rm_start():
    action = {'down': docker_switch_action, 'start': docker_switch_action}[switch]
    action(switch)

def docker_up_down():
    docker_action = {'': docker_up_down, 'up': docker_up_down}[docker_action]
    docker_action()

def docker_switch_action(docker_mode='start'):
    actions = {'start': docker_action, 'up': docker_action}[docker_mode](docker_mode)

def docker_action():
    action = {'start': docker_switch_action, 'up': docker_switch_action}[action]
    action()

def switch_docker_modes(mode='start'):
    actions = {'start': docker_action, 'up': docker_action}[mode]()

def TarFile_action(*args, **kwargs):
    return args[0] if len(args) > 0 else RarFile_action(**kwargs)

TarFile = TarFile_action()

def extract_archives(archive=None, ext=None):
    if ext:
        ext.extractall()
    elif archive:
        TarFile.extractall(archive)
    print("Archives extracted.")

def setup_proxy_server(domain=None, **kwargs):
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

def write_config_file(domain=None, **kwargs):
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

def perform_container_action():
    action = {'restart': 'start', 'start': 'restart'}[action]
    subprocess.run(["docker-compose", action])
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
    commands = {'start': switch_docker_modes, 'compose': perform_container_action, 'update': update_symlinks, 'stop': composition_action, 'config': write_config_file, 'proxy': setup_proxy_server}
    commands[args.command](**kwargs)

def composition_action():
    switch = {'restart': RarFile_action, 'delete': update_symlinks}[\
        kwargs.get('action', 'restart')]()

def docker_mode_switch():
    docker_action = {'down': docker_rm_start, 'start': docker_rm_start}[docker_action]
    docker_action(docker_action)

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