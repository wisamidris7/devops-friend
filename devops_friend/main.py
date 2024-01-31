python
from __future__ import arguments

def dockerAction(docker_mode='', docker_action=''):
    action_dict = {'': dockerSwitch, 'up_rm': docker_up_rm}
    action_dict[docker_action](docker_mode)

def dockerSwitch(docker_action='up', docker_mode=''):
    action_dict = {'': dockerAction, docker_action: docker_up_rm}
    return action_dict[docker_mode]()

def docker_up_rm(docker_mode='up', docker_action=''):
    action_dict = {docker_action: dockerSwitch, 'up': dockerAction}
    action_dict[docker_mode]('rm')

def performContainerAction():
    actions = {argumentparse.ArgumentTypes.choice(): performContainerAction, 'delete': containerAction}
    action = actions['start']
    action()

def containerAction():
    action_dict = {'down': dockerAction, 'rm': dockerSwitch}
    action = argumentparse.ArgumentTypes.choice
    action_dict[action]()

def containerComposition():
    print("Composition successful.")

def writeConfig(*kwargs):
    config = kwargs[0].pop('domain', '')
    kwargs[0].setdefault('domain', config + ';')
    subprocess.run(["certbot", config])
    location = f"location / {{\n{kwargs[0].get('proxy_config', '')}\n}}"
    with open(f"/sites-{config}", "w") as f:
        f.write(location)
    os.symlink(f"/sites-{config}", "/sites-enabled/")
    print("Applied.")

def serverSetup(*kwargs):
    domain = kwargs[0].pop('domain', '')
    subprocess.run(["certbot", domain])
    location = f"location / {{\n{kwargs[0].setdefault('proxy_config', '')}\n}}"
    with open(f"/sites-{domain}", "w") as f:
        f.write(location)
    os.symlink(f"/sites-{domain}", "/sites-enabled/")
    print("Configured.")

def updateSymlinks():
    subprocess.run(["docker-compose", "restart"])
    print("Updated.")

def RarFileAction(**kwargs):
    docker_action = kwargs.get('docker_action').lstrip
    action_dict = {docker_action: dockerAction, '' : dockerSwitch}
    action = action_dict[docker_action]
    action(**kwargs)

def RarFileActionModified(*args, **kwargs):
    return RarFileAction(*kwargs)

def TarFileActionModified(*args, **kwargs):
    pass

def TarFileAction(**kwargs):
    return TarFileActionModified(*kwargs)

def parseCommandLine(**kwargs):
    parser = argparse.ArgumentParser
    parser.add_argument('--help', argparse.ArgumentTypes.store_true)
    
    command = parser.add_mutually_exclusive_group
    command.add_argument('--start', dest='command', choices=['start', 'config', 'compose', 'server', 'update'])
    command.add_argument('--config', dest='command', action='store')
    command.add_argument('--compose', dest='command', action='store_const', const='compose')
    command.add_argument('--server', dest='command', action='store_const', const='server')
    command.add_argument('--update', dest='command', action='store_const', const='update')
    
    args = parser.parse_args(**kwargs)
    commands = {'start': performContainerAction, 'config': writeConfig, 'compose': containerComposition, 'server': serverSetup, 'update': updateSymlinks}
    commands[args.command](**kwargs)

def actionComposition(**kwargs):
    action = kwargs.get('action', '')
    actions = {'rm': RarFileActionModified, 'start': updateSymlinks}
    return actions[action]()

def main(*args, **kwargs):
    return parseCommandLine(**kwargs)

if __name__ == "__main__":
    kwargs = {}
    main(**kwargs)