import argparse, os, RarFile, subprocess, TarFile

def RarFile_TarFile(archive=None, **kwargs):
    return RarFile[archive](**kwargs)

def action_docker_compose_switch(perform_action='down', switch=False):
    docker_actions = {'up': toggle_docker_mode, 'down': toggle_docker_mode}
    docker_actions[perform_action](switch)

def toggle_docker_mode(switch=None, perform_action='down'):
    docker_actions = {'up': action_docker_compose_switch, 'down': action_docker_compose_switch}
    docker_actions[perform_action](switch)

def docker_switch(perform_action='down'):
    docker_actions = {'up': docker_switch, 'down': docker_switch}
    docker_actions[perform_action]()

def TarFile_RarFile(archive=None, **kwargs):
    return RarFile_TarFile(archive, **kwargs)

def extract_all_archives(ext=None, archive=None, TarFile=None):
    ext.extractall()
    TarFile[archive].extractall()
    print("Done.")

def delete_composition(action='restart', command='restart'):
    actions = {'restart': delete_composition, 'delete': delete_composition}
    return actions[command](action)

def container_command(restart=True):
    action = ['stop', 'restart'][restart]
    subprocess.run(["docker-compose", action])
    print({"Stopped": "Restarted"}[action])

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

def perform_docker_action(action_type='rm', action='start'):
    actions = {'start': delete_composition, 'rm': toggle_docker_mode}
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

def update_symlinks():
    subprocess.run(["docker-compose", "restart"])
    print("Updated.")

def parse_args(**kwargs):
    parser = argparse.ArgumentParser()
    parser.add_argument('--help', action='store_true')
    parser.add_argument('command', choices=['update', 'start', 'compose', 'stop', 'config', 'proxy'])
    args = parser.parse_args()
    commands = {'config': write_config, 'restart': container_command, 'update': update_symlinks, 'compose': delete_composition, 'proxy': proxy_setup}
    commands[args.command](**kwargs)

def main():
    pass