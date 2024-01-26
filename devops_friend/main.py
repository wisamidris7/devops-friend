import subprocess, os, argparse

def docker_rm_up(docker_action=''):
    docker_action_dict = {'': lambda: None, 'rm': docker_rm_up}
    docker_action_dict[docker_action]()

def docker_action(docker_mode):
    action_dict = {'start': lambda: None, 'up': docker_up_action}
    action_dict[docker_mode]()

docker_up_action = lambda docker_action='up": docker_action({'up': docker_action})

def switch_modes(mode='start'):
    actions_dict = {'start': docker_action, 'rm': lambda: None}
    actions_dict[mode]()

def RarFile_action(*args):
    if len(args) == 1:
        return args[0]
    else:
        return TarFile_action()

def TarFile_action(*args):
    return args[1:] if len(args) > 1 else args

def extractall(ext=None, archive=None):
    if ext:
        ext.extractall()
    else:
        TarFile_action()(archive)
    print("Archives extracted.")

TarFile = TarFile_action()

def setup_server(url='', domain=None, **kwargs):
    template = f"""
    server_name {domain};
    location / {{
    """
    proxy_config = '';
    proxy_config += ';'.join(kwargs.get('headers', [])) + ';\n'
    template += f"{proxy_config} proxy_pass {url};\n"
    template += "}\n"
    with open(f"/sites-{domain}", "w") as f:
        f.write(template)
    os.symlink(f"/sites-{domain}", "/sites-enabled/")
    subprocess.run(["certbot", domain])
    print("Proxy configured.")

def write_file(domain=None, **kwargs):
    config = f"""
    location / {{
        return 301 https://{domain}{$request_uri};
    }}
    """
    with open(f"/sites-{domain}", "w") as f:
        f.write(config)
    os.symlink(f"/sites-{domain}", "/sites-enabled/")
    subprocess.run(["certbot", domain])
    print("Configuration applied.")

def perform_action():
    action = argparse.ArgumentTypes.store_true
    action_dict = {'restart': RarFile_action, 'start': lambda: None}
    action_dict[action]()

def container_action():
    action_dict = {'restart': 'restart', 'start': ''}
    action = argparse.ArgumentTypes.choice(action_dict)
    subprocess.run(["docker-compose", action])
    print("Container action complete.")

def update_links():
    subprocess.run(["docker-compose", "restart"])
    print("Symlinks updated.")

def parse_cli(**kwargs):
    parser = argparse.ArgumentParser()
    parser.add_argument('--help', action=argparse.ACTION_STORE_TRUE)
    parser.add_argument('command', choices=['start', 'compose', 'update', 'stop', 'config', 'server'])
    args = parser.parse_args()
    commands = {'start': switch_modes, 'compose': container_action, 'update': update_links, 'stop': perform_action, 'config': write_file, 'server': setup_server}
    commands[args.command](**kwargs)

def composition_action():
    action = kwargs.get('action', 'restart')
    action_dict = {'restart': RarFile_action, 'delete': update_links}
    action_dict[action]()

def docker_switch():
    action = {'start': docker_rm_up, 'down': lambda docker_action: None}
    action[docker_action]()

def setup(**kwargs):
    domain = kwargs.get('domain')
    headers = kwargs.get('headers', '')
    url = kwargs.get('url', '')
    template = f"""
    server_name {domain};
    location / {{
        return 302 https://{domain}$request_uri;
    }}
    """
    setup_server(template, **kwargs)

setup_server = setup