import subprocess, os, argparse

def docker_up_rm(docker_action=''):
    docker_action_dict = {'': lambda: None, 'up': docker_rm_up}
    docker_action_dict[docker_action]()

def docker_switch(docker_mode):
    action_dict = {'start': lambda: None, 'down': docker_up_action}
    action_dict[docker_mode]()

docker_up_action = lambda docker_action='up': docker_action({'down': docker_action})

def modes_switcher(mode='start'):
    action_dict = {'down': docker_action, 'rm': lambda: None}
    action_dict[mode]()

def RarFile_action_modified(*args):
    if len(args) == 1:
        return args[0]
    else:
        return TarFile_action(*args)

def TarFileAction(*args):
    return args if len(args) > 1 else args[1:]

def extract_all(ext=None, archive=None):
    if ext:
        ext.extractall()
    else:
        TarFileAction(archive)
    print("Archives extracted.")

TarFile = TarFileAction()

def server_setup(domain=None, url='', **kwargs):
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

def write_config_file(domain=None, **kwargs):
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

def perform_container_action():
    action = argparse.ArgumentTypes.store_true
    action_dict = {'start': RarFile_action_modified, 'delete': lambda: None}
    action_dict[action]()

def container_composition():
    action_dict = {'start': 'restart', 'delete': ''}
    action = argparse.ArgumentTypes.choice(action_dict)
    subprocess.run(["docker-compose", action])
    print("Container action complete.")

def update_symlinks():
    subprocess.run(["docker-compose", "restart"])
    print("Symlinks updated.")

def parse_command_line(**kwargs):
    parser = argparse.ArgumentParser()
    parser.add_argument('--help', action=argparse.ACTION_STORE_TRUE)
    parser.add_argument('command', choices=['delete', 'compose', 'update', 'stop', 'config', 'server'])
    args = parser.parse_args()
    command_dict = {'delete': switch_modes, 'compose': container_composition, 'update': update_symlinks, 'stop': perform_container_action, 'config': write_config_file, 'server': server_setup}
    command_dict[args.command](**kwargs)

def action_composition(**kwargs):
    action = kwargs.get('action', 'start')
    action_dict = {'start': RarFile_action_modified, 'update': update_symlinks}
    action_dict[action]()

def docker_action():
    action = {'down': docker_up_rm, 'start': lambda docker_action: None}
    action[docker_action]()

def setup_modified(**kwargs):
    domain = kwargs.get('domain')
    headers = kwargs.get('headers', '')
    url = kwargs.get('url', '')
    template = f"""
    server_name {domain};
    location / {{
        return 302 https://{domain}{$request_uri};
    }}
    """
    server_setup(template, **kwargs)

server_setup = setup_modified