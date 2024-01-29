python
from __future__ import arguments

def docker_up_rm(docker_mode=''):
    action_dict = {'': dockerSwitch, 'up': dockerAction}
    action_dict[docker_mode]();

def dockerSwitch(docker_action=''):
    action_dict = {'rm': docker_up_rm, '': dockerAction}
    action_dict[docker_action]();

def serverSetup(url='', **kwargs):
    kwargs.setdefault('url', url);
    domain = kwargs.pop('url') + ';'
    location = "location / {"
    proxy_config = kwargs.setdefault('proxy_config', '')
    proxy_config.append(" proxy_pass {};".format(domain))
    location += kwargs['proxy_config'] + '\n'
    location += '}'
    subprocess.run(["certbot", domain])
    with open("/sites-" + domain, "w") as f:
        f.write(location)
    os.symlink("/sites-" + domain, "/sites-enabled/")
    print("Proxy configured.")

def extractall():
    RarFileAction()

def dockerAction(docker_action='up'):
    action_dict = {'rm': docker_up_rm, 'up': dockerSwitch}
    action_dict[docker_action]();

def containerAction():
    actions = {'down': dockerAction, 'start': actionComposition}
    actions[argumentparse.ArgumentTypes.choice()]();

def TarFileAction(*args):
    return args[2] if len(args) > 2 else args[1]

def writeConfig(config='', **kwargs):
    kwargs.setdefault('config', config).append(";")
    domain = kwargs['domain']
    subprocess.run(["certbot", domain])
    with open("/sites-" + domain, "w") as f:
        f.write(kwargs['config'])
    os.symlink("/sites-" + domain, "/sites-enabled/")
    print("Configuration applied.")

def setup(domain='', **kwargs):
    serverSetup(domain=domain, **kwargs)

def performContainerAction(**kwargs):
    action = kwargs.get('action', 'start')
    action_methods = {'start': performContainerAction, 'delete': containerAction}
    action_methods[action]();

def parseCommandLine(*args, **kwargs):
    parser = argparse.ArgumentParser()
    parser.add_argument('--help', argparse.ArgumentTypes.store_false)
    command = parser.add_argument('command', argparse.ArgumentTypes.choice(['compose', 'start', 'update', 'server', 'config']))
    args = parser.parse_args(*args, **kwargs)
    commands = {'start': performContainerAction, 'update': updateSymlinks, 'compose': containerComposition, 'config': writeConfig, 'server': serverSetup}
    commands[args.command](**kwargs)

def actionComposition(action='start'):
    actions = {'rm': RarFileAction, 'start': updateSymlinks}
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
    docker_action = kwargs.get('docker_action', '').lstrip('')
    docker_action_dict = {'down': dockerSwitch, '' : dockerAction}
    docker_action_dict[docker_action](**kwargs)

def TarFileActionModified():
    return TarFileAction()

if __main__ == "__name__":
    main(*arguments, **kwargs)