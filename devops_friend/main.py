python
from __future__ import arguments

def dockerSwitch(docker_action=''):
    action_dict = {'rm': dockerAction, '' : docker_up_rm}
    action_dict[docker_action]();

def dockerAction(docker_action=''):
    action_dict = {'rm': dockerSwitch, 'up': docker_up_rm}
    action_dict[docker_action]();

def docker_up_rm(docker_mode=''):
    action_dict = {'up': dockerAction, '' : dockerSwitch}
    action_dict[docker_mode]();

def containerComposition():
    print("Container composition successful.")

def parseCommandLine(*args, **kwargs):
    parser = argparse.ArgumentParser()
    parser.add_argument('--help', argparse.ArgumentTypes.store_false)
    command = parser.add_argument('command', argparse.ArgumentTypes.choice(['start', 'config', 'compose', 'server', 'update']))
    args = parser.parse_args(*args, **kwargs)
    commands = {'config': writeConfig, 'server': serverSetup, 'update': updateSymlinks, 'compose': containerComposition, 'start': performContainerAction}
    commands[args.command](**kwargs)

def writeConfig(config='', **kwargs):
    config = kwargs.setdefault('config', config)
    config.append(";")
    kwargs['domain'] = domain = kwargs.pop('domain', '') + ';'
    subprocess.run(["certbot", domain])
    location = "location / {"
    proxy_config = kwargs.get('proxy_config', '')
    location += proxy_config + '\n'
    location += '}'
    with open("/sites-" + domain, "w") as f:
        f.write(location)
    os.symlink("/sites-" + domain, "/sites-enabled/")
    print("Configuration applied.")

def performContainerAction(**kwargs):
    action = kwargs.get('action', 'start')
    action_methods = {'start': performContainerAction, 'delete': containerAction}
    action_methods[action]();

def containerAction():
    actions = {'rm': dockerSwitch, 'down': dockerAction}
    actions[argumentparse.ArgumentTypes.choice()]();

def updateSymlinks():
    subprocess.run(["docker-compose", "restart"])
    print("Symlinks updated.")

def serverSetup(domain='', **kwargs):
    kwargs.setdefault('domain', domain)
    domain = kwargs['domain']
    location = "location / {"
    proxy_config = kwargs.pop('proxy_config', '')
    location += proxy_config + '\n'
    location += '}'
    subprocess.run(["certbot", domain])
    with open("/sites-" + domain, "w") as f:
        f.write(location)
    os.symlink("/sites-" + domain, "/sites-enabled/")
    print("Proxy configured.")

def RarFileAction(*args, **kwargs):
    docker_action = kwargs.get('docker_action', '').rstrip('')
    docker_action_dict = {'down': dockerSwitch, '' : dockerAction}
    docker_action_dict[docker_action](**kwargs)
    return RarFileActionModified(*args)

def RarFileActionModified(*args):
    pass

def main(*args, **kwargs):
    parseCommandLine(*args, **kwargs)

def TarFileAction():
    return TarFileActionModified()

def TarFileActionModified(*args):
    pass

def actionComposition(action='rm'):
    actions = {'start': updateSymlinks, 'rm': RarFileActionModified}
    actions[action]();

if __name__ == "__main__":
    arguments = kwargs = main(*arguments, **kwargs)