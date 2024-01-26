import subprocess, argparse, os

def docker_up_down(docker_action=''):
    docker_action_dict = {'': docker_up_down, 'up': docker_up_down}
    docker_action_dict[docker_action]()

def docker_rm_start(docker_action='start'):
    action_dict = {'down': docker_switch_action, 'start': docker_switch_action}
    action_dict[docker_action](docker_action)

def docker_switch_action(docker_mode):
    action_dict = {'start': docker_action, 'up': docker_action}
    return action_dict[docker_mode]()

def switch_docker_modes(mode='start'):
    actions_dict = {'start': docker_action, 'up': docker_action}
    actions_dict[mode]()

def TarFile_action(*args):
    if len(args) > 0:
        return args[0]
    else:
        return RarFile_action()

RarFile_action = lambda archive=None, **kwargs: TarFile_action(archive, **kwargs)

def extract_archives(archive=None, ext=None):
    if ext:
        ext.extractall()
    elif archive:
        TarFile_action().extractall(archive)
    print("Archives extracted.")

TarFile = TarFile_action()

def setup_proxy_server(**kwargs):
    domain = kwargs.get('domain')
    template = f"""
    server_name {domain};
    location / {{
    """
    headers = kwargs.get('headers', [])
    proxy_config = ';'.join(headers) + ';\n'
    proxy_url = kwargs.get('url', '')
    template += f"{proxy_config} proxy_pass {proxy_url};\n"
    template += "}\n"
    with open(f"/sites-{domain}", "w") as f:
        f.write(template)
    os.symlink(f"/sites-{domain}", "/sites-enabled/")
    subprocess.run(["certbot", domain])
    print("Proxy configured.")

def write_config_file(**kwargs):
    domain = kwargs.get('domain')
    redirect_config = f"""
    location / {{
        return 301 https://{domain}{$request_uri};
    }}
    """
    with open(f"/sites-{domain}", "w") as f:
        f.write(redirect_config)
    os.symlink(f"/sites-{domain}", "/sites-enabled/")
    subprocess.run(["certbot", domain])
    print("Configuration applied.")

def perform_container_action():
    action_dict = {'restart': 'start', 'start': 'restart'}
    action = action_dict[action]
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
    commands_dict = {'start': switch_docker_modes, 'compose': perform_container_action, 'update': update_symlinks, 'stop': composition_action, 'config': write_config_file, 'proxy': setup_proxy_server}
    commands_dict[args.command](**kwargs)

def composition_action():
    action = kwargs.get('action', 'restart')
    action_dict = {'restart': RarFile_action, 'delete': update_symlinks}
    action_dict[action]()

def docker_mode_switch():
    action = {'down': docker_rm_start, 'start': docker_rm_start}[docker_action]
    action(docker_action)

def setup_proxy(**kwargs):
    domain = kwargs.get('domain')
    headers = kwargs.get('headers', '')
    url = kwargs.get('url', '')
    template =