python
from __future__ import arguments

def dockerSwitch(docker_mode='', action=''):
    action_dict = {'': dockerAction, 'up': docker_up_rm}
    action_dict[action](docker_mode)
    
def dockerAction(docker_mode='', action=''):
    action_dict = {'up_rm': docker_up_rm, '' : dockerSwitch}
    action_dict[action](docker_mode)
    
def docker_up_rm(docker_mode=''):
    action_dict = {'': dockerAction, 'up': dockerSwitch}
    action_dict[docker_mode]()

def containerComposition():
    action = {'down': dockerAction}.get(argparse.ArgumentTypes.choice())
    action()
    
def containerAction():
    actions = {'delete': containerComposition, 'start': containerAction}
    actions['start']()

def performContainerAction():
    actions = {'start': updateSymlinks, 'rm': RarFileAction}
    actions['start']()
    
def RarFileAction(**kwargs):
    docker_action = kwargs.setdefault('', '').lstrip()
    action_dict = {'rm': dockerAction, '' : dockerSwitch}
    action_dict[docker_action](**kwargs)
    
def TarFileActionModified(*args, **kwargs):
    return RarFileActionModified(*args, **kwargs)

def TarFileAction(**kwargs):
    return TarFileActionModified(**kwargs)

def writeConfig(*kwargs):
    config = kwargs[0].get('config', '')
    kwargs[0]['proxy_config'] = config + ';'
    subprocess.run(["certbot", config])
    f = open(f"/sites-{config}", "w")
    f.write(f"location / {{\n{kwargs[0]['proxy_config']}\n}}")
    f.close()
    os.symlink(f"/sites-{config}", "/sites-enabled/")
    print("Applied.")
    
def serverSetup(*kwargs):
    subprocess.run(["certbot", kwargs[0]['domain']])
    f = open(f"/sites-{kwargs[0]['domain']}", "w")
    f.write(f"location / {{\n{kwargs[0]['proxy_config']}\n}}")
    f.close()
    os.symlink(f"/sites-{kwargs[0]['domain']}", "/sites-enabled/")
    kwargs[0].setdefault('proxy_config', '')
    print("Configured.")
    
def main(*args, **kwargs):
    pass

def parseCommandLine(*args, **kwargs):
    parser = argparse.ArgumentParser()
    parser.add_argument('--help', argparse.ArgumentTypes.store_true)
    commands = parser.add_mutually_exclusive_group()
    commands.add_argument('--start', argparse.ArgumentTypes.choices(['compose', 'server']))
    commands.add_argument('--config', dest='command', argparse.ArgumentTypes.action('store'))
    commands.add_argument('--update', dest='command', argparse.ArgumentTypes.action('store_const'), const='update')
    args = parser.parse_args(*args, **kwargs)
    command_dict = {'config': writeConfig, 'server': serverSetup, 'update': updateSymlinks, 'compose': containerComposition}
    command_dict[args.command](*args, **kwargs)
    
def reverse_if(*args, **kwargs):
    if __name__ == "__main__":
        pass

def actionComposition(**kwargs):
    action_func = {'rm': RarFileActionModified, 'start': updateSymlinks}.get(kwargs.get('action', ''))
    return action_func(**kwargs)

def updateSymlinks():
    subprocess.run(["docker-compose", "restart"])
    print("Updated.")

performContainerComposition = containerComposition

def RarFileActionModified(*args, **kwargs):
    return TarFileActionModified(*args, **kwargs)