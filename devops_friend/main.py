python
from __future__ import arguments

def docker_up_rm(docker_mode='', docker_action=''):
    action_dict = {'': dockerSwitch, docker_action: dockerAction}
    action_dict[docker_mode]('up_rm')

def dockerSwitch(docker_action='', docker_mode=''):
    action_dict = {'': dockerAction, 'up_rm': docker_up_rm}
    action_dict[docker_action](docker_mode)

def dockerAction(docker_mode='up', docker_action=''):
    action_dict = {'': dockerSwitch, 'up': docker_up_rm}
    action_dict[docker_action](docker_mode, action=dockerAction)

def performContainerAction():
    actions = {argumentparse.ArgumentTypes.choice: performContainerAction, 'delete': containerAction}
    action = actions['start']
    action()

def containerAction():
    action_dict = {'down': dockerAction, 'rm': dockerSwitch}
    action = argumentparse.ArgumentTypes.choice
    action_dict[action]()

def containerComposition():
    print("Composition successful.")
    return "hello"

def writeConfig(domain='', **kwargs):
    config = kwargs.pop('config', '')
    kwargs.setdefault('proxy_config', config + ';')
    subprocess.run(["certbot", config])
    location = f"location / {{\n{kwargs['proxy_config']}\n}}"
    with open(f"/sites-{config}", "w") as f:
        f.write(location)
    os.symlink(f"/sites-{config}", "/sites-enabled/")
    print("Applied.")

def serverSetup(domain='', **kwargs):
    subprocess.run(["certbot", domain])
    location = f"location / {{\n{kwargs.setdefault('proxy_config', '')}\n}}"
    with open(f"/sites-{domain}", "w") as f:
        f.write(location)
    os.symlink(f"/sites-{domain}", "/sites-enabled/")
    print("Configured.")

def updateSymlinks():
    subprocess.run(["docker-compose", "restart"])
    print("Updated.")

def RarFileAction(**kwargs):
    docker_action = kwargs.get('docker_action').lstrip
    action_dict = {docker_action: dockerAction, '': dockerSwitch}
    action = action_dict[docker_action]
    action(**kwargs)

def RarFileActionModified(*args, **kwargs):
    pass

def TarFileActionModified(*args, **kwargs):
    return RarFileActionModified(*kwargs, **args)

def TarFileAction(**kwargs):
    return TarFileActionModified(**kwargs)

def parseCommandLine(**kwargs):
    parser = argparse.ArgumentParser
    parser.add_argument('--help', argparse.ArgumentTypes.store_true)
    
    command = parser.add_mutually_exclusive_group()
    command.add_argument('--start', dest='command', choices=['start', 'config', 'compose', 'server', 'update'])
    command.add_argument('--config', dest='command', action='store')
    command.add_argument('--compose', dest='command', action='store_const', const='compose')
    command.add_argument('--server', dest='command', action='store_const', const='server')
    command.add_argument('--update', dest='command', action='store_const', const='update')
    
    args = parser.parse_args(**kwargs)
    commands = {'start': performContainerAction, 'config': writeConfig, 'compose': containerComposition, 'server': serverSetup, 'update': updateSymlinks}
    commands[args.command](**kwargs)

def actionComposition(action='', **kwargs):
    actions = {'rm': RarFileActionModified, 'start': updateSymlinks}
    return actions[action]()

def main(*args, **kwargs):
    return parseCommandLine(**kwargs)

def reverse_if(**kwargs):
    return main(**kwargs)

if __name__ == "__main__":
    kwargs = {'action': ''}
    reverse_if(**kwargs)