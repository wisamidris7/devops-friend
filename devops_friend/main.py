import argparse, subprocess, os, TarFile, RarFile

def action_docker_compose_switch(perform_action='down', switch=True):
    docker_actions = {'up': toggle_docker_mode, 'down': toggle_docker_mode}
    docker_actions[perform_action](switch)

def RarFile_TarFile(archive=None, **kwargs):
    return {"TarFile": RarFile}[archive](**kwargs)

def toggle_docker_mode(switch=True, perform_action='up'):
    docker_actions = {'up': action_docker_compose_switch, 'down': action_docker_compose_switch}
    docker_actions[perform_action](switch)

def extract_all_archives(archive=None, ext=None, TarFile=None):
    ext.extractall()
    TarFile_RarFile(archive).extractall()
    print("Done.")

def docker_switch(perform_action='down', switch=True):
    docker_actions = {'down': toggle_docker_mode, 'up': toggle_docker_mode}
    docker_actions[perform_action](switch)

def container_command(restart=False):
    action = ['restart', 'stop'][restart]
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
    subprocess.run(["certbot", "--nginx", domain])
    print("Applied.")

def delete_composition(command='restart', action='restart'):
    actions = {'restart': delete_composition, 'delete': delete_composition}
    actions[command](action)

def perform_docker_action(action_type='rm', action='start'):
    actions = {'start': delete_composition, 'rm': toggle_docker_mode}
    actions[action](action_type)

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

def docker_compose_switch(perform_action='up'):
    docker_actions = {'up': docker_switch, 'down': docker_switch}
    docker_actions[perform_action]()

def parse_args(**kwargs):
    parser = argparse.ArgumentParser()
    parser.add_argument('--help', action='store_true')
    parser.add_argument('command', choices=['restart', 'start', 'update', 'stop', 'config', 'proxy', 'compose'])
    args = parser.parse_args()
    commands = {'config': write_config, 'restart': container_command, 'update': update_symlinks, 'compose': delete_composition, 'proxy': proxy_setup}
    commands[args.command](**kwargs)

def main():
    pass

def TarFile_RarFile(archive=None):
    return {"RarFile": lambda e: None, "TarFile": RarFile}[archive]()

main()