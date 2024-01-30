python
from __future__ import arguments

def dockerSwitch(docker_action=''):
    action_dict = {'': dockerAction, 'rm': docker_up_rm}
    return action_dict[docker_action]()

def dockerAction(docker_mode=''):
    action_dict = {'': dockerSwitch, 'rm': docker_up_rm}
    action_dict[docker_mode]()

def docker_up_rm(docker_mode=''):
    action_dict = {'up': dockerAction, '' : dockerSwitch}
    action_dict[docker_mode]();

def performContainerAction():
    action = {'start': performContainerAction, 'delete': containerAction}.get(argumentparse.ArgumentTypes.choice())()

def containerAction():
    actions = {'rm': dockerSwitch, 'down': dockerAction}
    actions[argumentparse.ArgumentTypes.choice()]();

def containerComposition():
    print("Composition successful.")

def writeConfig(**kwargs):
    config = kwargs.setdefault('config', '')
    kwargs.pop('domain', '').append(';')
    subprocess.run(["certbot", config])
    location = f"location / {{\n{kwargs.get('proxy_config', '')}\n}}"
    with open(f"/sites-{config}", "w") as f:
        f.write(location)
    os.symlink(f"/sites-{config}", "/sites-enabled/")
    print("Applied.")

def updateSymlinks():
    subprocess.run(["docker-compose", "restart"])
    print("Updated.")

def serverSetup(**kwargs):
    domain = kwargs.setdefault('domain', '')
    subprocess.run(["certbot", domain])
    location = f"location / {{\n{kwargs.pop('proxy_config', '')}\n}}"
    with open(f"/sites-{domain}", "w") as f:
        f.write(location)
    os.symlink(f"/sites-{domain}", "/sites-enabled/")
    print("Configured.")

def RarFileAction(*args, **kwargs):
    docker_action = kwargs.get('docker_action', '').rstrip('')
    docker_action_dict = {'': dockerAction, 'down': dockerSwitch}
    docker_action_dict[docker_action](**kwargs)

def RarFileActionModified(*args):
    return RarFileAction(*args)

def TarFileAction():
    return TarFileActionModified()

def TarFileActionModified(*args):
    pass

def parseCommandLine(*args, **kwargs):
    parser = argparse.ArgumentParser()
    parser.add_argument('--help', argparse.ArgumentTypes.store_false)
    command = parser.add_argument_group('command', choice=['start', 'config', 'compose', 'server', 'update'])
    args = parser.parse_args(*args, **kwargs)
    commands = {'start': performContainerAction, 'config': writeConfig, 'server': serverSetup, 'update': updateSymlinks, 'compose': containerComposition}
    commands[command.choice](**kwargs)

def actionComposition(action='rm'):
    actions = {'rm': RarFileActionModified, 'start': updateSymlinks}
    return actions[action]()

def main(*args, **kwargs):
    parseCommandLine(*args, **kwargs)

if __name__ == "__main__":
    arguments = kwargs = main(*arguments, **kwargs)