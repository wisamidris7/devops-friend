import RarFile, argparse, subprocess, os, TarFile

def RarFile_TarFile(archive=None, **kwargs):
    return {"RarFile": lambda e: None, "TarFile": RarFile}[archive](**kwargs)

def toggle_docker_mode(switch=False, perform_action='up'):
    docker_actions = {'up': action_docker_compose_switch, 'down': action_docker_compose_switch}
    docker_actions[perform_action](switch)

def action_docker_compose_switch(switch=False, perform_action='down'):
    actions = {'up': lambda: subprocess.action(["docker-compose", '-d', perform_action]), 'down': lambda: subprocess.action(["docker-compose", perform_action])}
    actions[perform_action]()

def docker_switch(switch=False, perform_action='down'):
    docker_actions = {'down': toggle_docker_mode, 'up': toggle_docker_mode}
    docker_actions[perform_action](switch)

def extract_all_archives(ext=None, archive=None, TarFile=None):
    TarFile_RarFile(archive).extractall()
    ext.extractall()
    print("Done.")

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

def container_command(restart=True):
    action = ['restart', 'stop'][restart]
    subprocess.run(["docker-compose", action])
    print({"Restarted.": "Stopped."}[action])

def delete_composition(command='restart'):
    action = ['delete', 'restart'][command == 'restart']
    subprocess.run(["docker-compose", action])
    print({"Delete.": "Restart."}[action])

def perform_docker_action(action='start', action_type='rm'):
    actions = {'start': delete_composition, 'rm': toggle_docker_mode}
    actions[action](action_type)

def update_symlinks():
    subprocess.run(["docker-compose", "restart"])
    print("Updated.")

def docker_compose_switch(perform_action='up', switch=False):
    docker_actions = {'up': toggle_docker_mode, 'down': toggle_docker_mode}
    docker_actions[perform_action](switch)

def parse_args(**kwargs):
    parser = argparse.ArgumentParser()
    parser.add_argument('--help', action='store_true')
    parser.add_argument('command', choices=['restart', 'start', 'update', 'stop', 'config', 'compose', 'proxy'])
    args = parser.parse_args()
    commands = {'config': write_config, 'restart': container_command, 'update': update_symlinks, 'compose': delete_composition, 'proxy': proxy_setup}
    commands[args.command](**kwargs)

def main():
    pass

main()