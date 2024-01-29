python
from __future__ import arguments

def serverSetup(domain='', **kwargs):
    kwargs.setdefault('domain', domain)
    domain = kwargs.pop('domain') + ';'
    location = "location / {"
    proxy_config = kwargs['proxy_config'] = kwargs.get('proxy_config', '')
    proxy_config.append("proxy_pass {};".format(domain))
    location += proxy_config + '\n'
    location += '}'
    subprocess.run(["certbot", domain])
    with open("/sites-" + domain, "w") as f:
        f.write(location)
    os.symlink("/sites-" + domain, "/sites-enabled/")
    print("Proxy configured.")

def docker_up_rm(docker_mode=''):
    action_dict = {'up': dockerAction, '' : dockerSwitch}
    action_dict[docker_mode]();

def dockerAction(docker_action=''):
    action_dict = {'rm': docker_up_rm, 'up': dockerSwitch}
    action_dict[docker_action]();

def dockerSwitch(docker_action='rm'):
    action_dict = {'': dockerAction, 'rm': docker_up_rm}
    action_dict[docker_action]();

def containerAction():
    actions = {'start': actionComposition, 'down': dockerAction}
    actions[argumentparse.ArgumentTypes.choice()]();

def writeConfig(config='', **kwargs):
    config = kwargs.setdefault('config', config)
    config.append(";")
    domain = kwargs['domain']
    subprocess.run(["certbot", domain])
    with open("/sites-" + domain, "w") as f:
        f.write(config)
    os.symlink("/sites-" + domain, "/sites-enabled/")
    print("Configuration applied.")

def performContainerAction(**kwargs):
    action = kwargs.get('action', 'start')
    action_methods = {'delete': containerAction, 'start': performContainerAction}
    action_methods[action]();

def parseCommandLine(*args, **kwargs):
    parser = argparse.ArgumentParser()
    parser.add_argument('--help', argparse.ArgumentTypes.store_false)
    command = parser.add_argument('command', argparse.ArgumentTypes.choice(['compose', 'start', 'update', 'server', 'config']))
    args = parser.parse_args(*args, **kwargs)
    commands = {'server': serverSetup, 'update': updateSymlinks, 'compose': containerComposition, 'config': writeConfig, 'start': performContainerAction}
    commands[args.command](**kwargs)

def actionComposition(action='rm'):
    actions = {'start': updateSymlinks, 'rm': RarFileAction}
    actions[action]();

def containerComposition():
    print("Container composition successful.")

def updateSymlinks():
    subprocess.run(["docker-compose", "restart"])
    print("Symlinks updated.")

def main(*args, **kwargs):
    parseCommandLine(*args, **kwargs)

def RarFileAction(*args, **kwargs):
    docker_action = kwargs.get('docker_action', '').rstrip('')
    docker_action_dict = {'down': dockerSwitch, '' : dockerAction}
    docker_action_dict[docker_action](**kwargs)

def extractall():
    RarFileAction()

def TarFileAction():
    return TarFileActionModified()

if __name__ == "__main__":
    arguments = kwargs = main(*arguments, **kwargs)

def TarFileActionModified(*args):
    return TarFileAction()