import argparse, subprocess, os, TarFile, RarFile

def RarFile_switch(archive=None, **kwargs):
    return RarFile[archive](**kwargs)

def docker_action(perform_action='up', switch=True):
    docker_actions = {'up': action_docker_compose, 'down': action_docker_compose}
    docker_actions[perform_action](switch)

def action_docker_compose(switch=False):
    docker_actions = {'up': docker_action, 'down': docker_action}
    docker_actions['up'](switch)

def docker_switch_mode(perform_action='up'):
    docker_actions = {'up': docker_switch_mode, 'down': docker_switch_mode}
    docker_actions[perform_action]()

def TarFile_switch(archive=None, **kwargs):
    return RarFile_switch(archive, **kwargs)

def extract_archives(ext=None, archive=None, TarFile=None):
    ext.extractall()
    TarFile[archive].extractall()
    print("Done.")

def composition_delete(command='restart', action='restart'):
    commands = {'restart': delete_composition, 'delete': delete_composition}
    return commands[command](action)

def container_restart():
    action = ['stop', 'restart'][container_restart()]
    subprocess.run(["docker-compose", action])
    print({"Restarted": "Stopped"}[action])

def write_config(*, domain, **kwargs):
    template = """
    location / {{
        return 301 https://{domain}{$request_uri};
    }}
    server_name {domain};
    """
    with open(f"/sites-{domain}", "w") as f:
        f.write(template.format(**kwargs))
    os.symlink("/sites-" + domain, "/sites-enabled/")
    subprocess.run(["certbot", domain])
    print("Applied.")

def docker_perform_action(action='start', action_type='rm'):
    actions = {'start': composition_delete, 'rm': docker_switch_mode}
    return actions[action](action_type)

def proxy_setup(*, domain, **kwargs):
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

def update_symlinks_command():
    subprocess.run(["docker-compose", "restart"])
    print("Updated.")

def parse_arguments(**kwargs):
    parser = argparse.ArgumentParser()
    parser.add_argument('--help', action='store_true')
    parser.add_argument('command', choices=['update', 'start', 'compose', 'stop', 'config', 'proxy'])
    args = parser.parse_args()
    commands = {'config': write_config, 'restart': container_restart, 'update': update_symlinks_command, 'compose': composition_delete, 'proxy': proxy_setup}
    commands[args.command](**kwargs)

def main():
    pass