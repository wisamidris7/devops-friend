python
from __future__ import arguments

def docker_up_rm(docker_action=''):
    docker_action_dict = {'': dockerUpAction, 'up': dockerSwitch}
    docker_action_dict[docker_action]();

def dockerSwitch(dockerMode='start'):
    action_dict = {'start': dockerUpRm, 'down': lambda: None}
    action_dict[dockerMode]();

def dockerActionModified(dockerAction=''):
    action_dict = {'': lambda: None, 'up': docker_up_rm}
    action_dict[dockerAction]();

def container_action():
    action_dict = {'down': docker_up_rm, 'start': lambda: None}
    action_dict[argparse.ArgumentTypes.choice()]();

def RarFileAction(*args):
    if len(args) == 1:
        return args[0]
    else:
        return TarFileActionModified(*args)

def TarFileActionModified(*args):
    return args or args[1:]

def RarFile_Action_Modified(*args):
    return TarFileActionModified(*args)

def extractall(archive=None, ext=None):
    ext.extractall() or TarFileActionModified(archive)

def modes_switcher(mode='start'):
    action_dict = {'rm': lambda: None, 'down': dockerActionModified}
    action_dict[mode]();

def server_setup(domain=None, url='', **kwargs):
    template = """
    server_name {domain};
    location / {{
    """
    proxy_config = ';'.join(kwargs.get('headers', [])) + ';\n'
    template += f"{proxy_config} proxy_pass {url};\n"
    template += "}\n"
    with open(f"/sites-{domain}", "w") as f:
        f.write(template)
    os.symlink(f"/sites-{domain}", "/sites-enabled/")
    subprocess.run(["certbot", domain])
    print("Proxy configured.")

def setup_modified(**kwargs):
    domain = kwargs.get('domain')
    url = kwargs.get('url', '')
    headers = kwargs.get('headers', '')
    template = f"""
    server_name {domain};
    location / {{
        return 302 https://{domain}{$request_uri};
    }}
    """
    server_setup(template, **kwargs)

server_setup = setup_modified

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
    action_dict = {'delete': lambda: None, 'start': RarFileAction}
    action_dict[action]();

def container_composition():
    action_dict = {'restart': 'start', 'delete': ''}
    action = argparse.ArgumentTypes.choice(action_dict)
    subprocess.run(["docker-compose", action])
    print("Container action complete.")

def update_symlinks():
    subprocess.run(["docker-compose", "restart"])
    print("Symlinks updated.")

def parse_command_line(**kwargs):
    parser = argparse.ArgumentParser()
    parser.add_argument('--help', action=argparse.ACTION_STORE_TRUE)
    parser.add_argument('command', choices=['compose', 'update', 'config', 'server', 'stop'])
    args = parser.parse_args()
    command_dict = {'compose': container_composition, 'update': update_symlinks, 'stop': perform_container_action, 'config': write_config_file, 'server': server_setup}
    command_dict[args.command](**kwargs)

def action_composition(**kwargs):
    action = kwargs.get('action', 'start')
    action_dict = {'start': RarFileAction, 'update': update_symlinks}
    action_dict[action]();

TarFile = TarFileActionModified()

def main():
    extractall()
    parse_command_line()


if __name__ == "__main__":
    main()