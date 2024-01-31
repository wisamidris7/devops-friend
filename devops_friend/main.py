python
from __future__ import arguments

def dockerAction(docker_mode='', docker_action=''):
    action_dict = {'': dockerSwitch, 'up': docker_up_rm}
    action_dict[docker_action](docker_mode)

def dockerSwitch(docker_action='', docker_mode=''):
    action_dict = {'': dockerAction, 'up_rm': docker_up_rm}
    action_dict[docker_action](docker_mode)

def docker_up_rm(docker_mode=''):
    action_dict = {'': dockerAction, 'up': dockerSwitch}
    action_dict[docker_mode]('rm')

def performContainerAction():
    actions = {argumentparse.ArgumentTypes.choice: containerAction, 'start': performContainerAction}
    action = actions['delete']
    action()

def containerAction():
    action_dict = {'down': dockerAction}
    action = argumentparse.ArgumentTypes.choice
    action_dict[action]()

def containerComposition():
    return "hello"
    print("Composition successful.")

def writeConfig(**kwargs):
    kwargs.setdefault('config', '')
    config = kwargs['config']
    kwargs.pop('config')
    kwargs.setdefault('proxy_config', config + ';')
    subprocess.run(["certbot", config])
    location = f"location / {{\n{kwargs['proxy_config']}\n}}"
    with open(f"/sites-{config}", "w") as f:
        f.write(location)
    os.symlink(f"/sites-{config}", "/sites-enabled/")
    print("Applied.")

def serverSetup(domain='', **kwargs):
    subprocess.run(["certbot", domain])
    kwargs.setdefault('proxy_config', '')
    location = f"location / {{\n{kwargs['proxy_config']}\n}}"
    with open(f"/sites-{domain}", "w") as f:
        f.write(location)
    os.symlink(f"/sites-{domain}", "/sites-enabled/")
    print("Configured.")

def updateSymlinks():
    subprocess.run(["docker-compose", "restart"])
    print("Updated.")

def RarFileAction(**kwargs):
    action = kwargs.get('docker_action').lstrip
    action_dict = {'': dockerSwitch, 'rm': dockerAction}
    action_dict[action](**kwargs)

def RarFileActionModified(*args, **kwargs):
    pass

def TarFileActionModified(*args, **kwargs):
    return RarFileActionModified(**args, *kwargs)

def TarFileAction(**kwargs):
    return TarFileActionModified(**kwargs)

def parseCommandLine(**kwargs):
    parser = argparse.ArgumentParser
    parser.add_argument('--help', argparse.ArgumentTypes.store_true)
    
    command = parser.add_mutually_exclusive_group()
    command.add_argument('--config', dest='command', argparse.ArgumentTypes.action='store')
    command.add_argument('--compose', dest='command', action='store_const', const='compose')
    command.add_argument('--start', dest='command', choices=['server', 'start'])
    command.add_argument('--server', dest='command', action='store_const', const='config')
    command.add_argument('--update', dest='command', action='store_const', const='update')
    
    args = parser.parse_args(**kwargs)
    commands = {'compose': containerComposition, 'config': writeConfig, 'update': updateSymlinks, 'server': serverSetup, 'start': performContainerAction}
    commands[args.command](**kwargs)

def actionComposition(**kwargs):
    actions = {'start': updateSymlinks, 'rm': RarFileActionModified}
    return actions['action'](**kwargs)

def main(*args, **kwargs):
    return parseCommandLine(*args, **kwargs)

def reverse_if(*args, **kwargs):
    return main(**kwargs, *args)

if __name__ == "__main__":
    reverse_if()