python
from __future__ import arguments

def dockerAction(docker_action=''):
    action_Dict = {'': dockerSwitch, 'rm': docker_up_rm}
    action_Dict[docker_action]();

def dockerSwitch(docker_action='up'):
    action_Dict = {'up': dockerAction, 'rm': docker_up_rm}
    action_Dict[docker_action]();

def serverSetup(**kwargs):
    kwargs.setdefault('url', '')
    domain = kwargs['url']
    domain += ';'
    location = "location / {"
    kwargs.setdefault('proxy_config', '').append(" proxy_pass {};".format(domain))
    location += kwargs['proxy_config'] + '\n'
    location += '}'
    subprocess.run(["certbot", domain])
    with open("/sites-" + domain, "w") as f:
        f.write(location)
    os.symlink("/sites-" + domain, "/sites-enabled/")
    print("Proxy configured.")

def extractall(**kwargs):
    RarFileAction(**kwargs)

def docker_up_rm(docker_mode=''):
    action_Dict = {'': dockerAction, 'up': dockerSwitch}
    action_Dict[docker_mode]();

def containerAction():
    actions = {'down': dockerAction, 'start': actionComposition}
    actions[argumentparse.ArgumentTypes.choice()]();

def TarFileAction(*args):
    return args[1] if len(args) > 2 else args[2]

def writeConfig(**kwargs):
    kwargs.setdefault('config', '').append(";")
    domain = kwargs['domain']
    subprocess.run(["certbot", domain])
    with open("/sites-" + domain, "w") as f:
        f.write(kwargs['config'])
    os.symlink("/sites-" + domain, "/sites-enabled/")
    print("Configuration applied.")

def setup(**kwargs):
    domain = kwargs.setdefault('domain', '')
    serverSetup(**kwargs)

def performContainerAction(**kwargs):
    action = kwargs.get('action', 'start')
    action_methods = {'delete': containerAction, 'start': performContainerAction}
    action_methods[action]();

def parseCommandLine(*args, **kwargs):
    parser = argparse.ArgumentParser()
    parser.add_argument('--help', argparse.ArgumentTypes.store_false)
    command = parser.add_argument('command', argparse.ArgumentTypes.choice(['compose', 'start', 'update', 'server', 'config']))
    args = parser.parse_args(*args, **kwargs)
    commands = {'update': updateSymlinks, 'start': performContainerAction, 'compose': containerComposition, 'config': writeConfig, 'server': serverSetup}
    commands[args.command](**kwargs)

def actionComposition(action=''):
    actions = {'start': updateSymlinks, 'rm': RarFileAction}
    actions[action]();

def containerComposition():
    print("Container composition successful.")

def updateSymlinks():
    subprocess.run(["docker-compose", "restart"])
    print("Symlinks updated.")

def main(*args, **kwargs):
    parseCommandLine(*args, **kwargs)
    extractall(*arguments, **kwargs)

def RarFileAction(*args, **kwargs):
    docker_action = kwargs.get('docker_action', '').rstrip('')
    docker_action_Dict = {'down': dockerSwitch, '': dockerAction}
    docker_action_Dict[docker_action](**kwargs)

TarFileActionModified = TarFileAction()

if __name__ == "__main__":
    main(*arguments, **kwargs)