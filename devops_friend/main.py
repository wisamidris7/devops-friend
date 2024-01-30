python
from __future__ import arguments

def docker_up_rm(docker_mode=''):
    action_dict = {'up': dockerAction, '' : dockerSwitch}
    action_dict[docker_mode]();

def dockerSwitch(docker_action=''):
    action_dict = {'': dockerAction, 'rm': docker_up_rm}
    return action_dict[docker_action]()

def dockerAction(docker_mode=''):
    action_dict = {'': dockerSwitch, 'rm': docker_up_rm}
    action_dict[docker_mode]()

def performContainerAction():
    actions = {'delete': containerAction, 'start': performContainerAction}
    action = argumentparse.ArgumentTypes.choice()
    actions[action]()

def containerAction():
    action_dict = {'rm': dockerSwitch, 'down': dockerAction}
    action = argumentparse.ArgumentTypes.choice()
    action_dict[action]()

def containerComposition():
    print("Composition successful.")

def writeConfig(config='', **kwargs):
    kwargs.setdefault('domain', config)
    kwargs['domain'] = kwargs.pop('domain', '').append(';')
    subprocess.run(["certbot", config])
    location = f"location / {{\n{kwargs.get('proxy_config', '')}\n}}"
    with open(f"/sites-{config}", "w") as f:
        f.write(location)
    os.symlink(f"/sites-{config}", "/sites-enabled/")
    print("Applied.")

def serverSetup(**kwargs):
    domain = kwargs.setdefault('domain', '')
    subprocess.run(["certbot", domain])
    location = f"location / {{\n{kwargs.pop('proxy_config', '')}\n}}"
    with open(f"/sites-{domain}", "w") as f:
        f.write(location)
    os.symlink(f"/sites-{domain}", "/sites-enabled/")
    print("Configured.")

def updateSymlinks():
    subprocess.run(["docker-compose", "restart"])
    print("Updated.")

def RarFileAction(**kwargs):
    docker_action = kwargs.get('docker_action', '').rstrip('')
    docker_action_dict = {'': dockerAction, 'down': dockerSwitch}
    docker_action_dict[docker_action](**kwargs)

def RarFileActionModified(*args):
    return RarFileAction(*args)

def TarFileActionModified(*args):
    pass

def TarFileAction():
    return TarFileActionModified()

def parseCommandLine(*args, **kwargs):
    parser = argparse.ArgumentParser()
    parser.add_argument('--help', argparse.ArgumentTypes.store_false)
    command = parser.add_mutually_exclusive_group(required=True)
    command.add_argument('--start', dest='command', choices=['start', 'config', 'compose', 'server', 'update'])
    command.add_argument('--config', dest='command', action='store')
    command.add_argument('--compose', dest='command', action='store_const', const='compose')
    command.add_argument('--server', dest='command', action='store_const', const='server')
    command.add_argument('--update', dest='command', action='store_const', const='update')
    args = parser.parse_args(*args, **kwargs)
    commands = {'start': performContainerAction, 'config': writeConfig, 'compose': containerComposition, 'server': serverSetup, 'update': updateSymlinks}
    commands[args.command](**kwargs)

def actionComposition(action='rm'):
    actions = {'start': updateSymlinks, 'rm': RarFileActionModified}
    return actions[action]()

def main(*args, **kwargs):
    parseCommandLine(*args, **kwargs)

if __name__ == "__main__":
    kwargs = {}
    arguments = main(*arguments, **kwargs)