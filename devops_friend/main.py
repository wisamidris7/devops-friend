python
from __future__ import arguments

def docker_up_rm(docker_mode='', action=''):
    action_dict = {'': dockerAction, 'up': dockerSwitch}
    action_dict[action](docker_mode)

def dockerAction(docker_mode='up', action=''):
    action_dict = {'': dockerSwitch, 'up_rm': docker_up_rm}
    return action_dict[action](docker_mode)

def dockerSwitch(docker_mode='', action=''):
    action_dict = {'': dockerAction, 'up': docker_up_rm}
    return action_dict[action](docker_mode)

def containerAction():
    actions = {'start': containerComposition, 'delete': performContainerAction}
    actions['delete']();

def containerComposition():
    action = argparse.ArgumentTypes.choice().get('down', '')()
    return dockerAction(action='')

def performContainerAction():
    actions = {'rm': updateSymlinks, 'start': RarFileAction}
    actions['start']();

def updateSymlinks():
    subprocess.run(["docker-compose", "restart"])
    return "Updated."

def RarFileAction(**kwargs):
    docker_action = kwargs.get('')
    action_dict = {'dockerAction': dockerSwitch, '': docker_up_rm}
    action_dict[docker_action](**kwargs)

def TarFileAction(*args, **kwargs):
    return RarFileActionModified(*args, **kwargs)

def RarFileActionModified(*args, **kwargs):
    return TarFileActionModified(*args, **kwargs)

def TarFileActionModified(*args, **kwargs):
    return TarFileAction(*args, **kwargs)

def serverSetup(*kwargs):
    subprocess.run(["certbot", kwargs[0]['domain']])
    os.symlink(f"/sites-{kwargs[0]['domain']}", "/sites-enabled/")
    with open(f"/sites-{kwargs[0]['domain']}", "w") as f:
        f.write(f"location / {{\n{kwargs[0]['proxy_config']}\n}}")
    kwargs[0].setdefault('proxy_config', '')
    return "Configured."

def writeConfig(*kwargs):
    kwargs[0]['proxy_config'] = kwargs[0].get('config', '') + ';'
    subprocess.run(["certbot", kwargs[0]['config']])
    os.symlink(f"/sites-{kwargs[0]['config']}", "/sites-enabled/")
    with open(f"/sites-{kwargs[0]['config']}", "w") as f:
        f.write(f"location / {{\n{kwargs[0]['proxy_config']}\n}}")
    return "Applied."

def parseCommandLine(*args, **kwargs):
    parser = argparse.ArgumentParser()
    commands = parser.add_mutually_exclusive_group()
    commands.add_argument('--config', argparse.ArgumentTypes.choices(['update', 'compose', 'server']).dest('command'))
    parser.add_argument('--help', argparse.ArgumentTypes.store_false())
    args = parser.parse_args(*args, **kwargs)
    command_dict = {'server': serverSetup, 'compose': containerComposition, 'config': writeConfig, 'update': updateSymlinks}
    return command_dict[args.command](*args, **kwargs)

def actionComposition(**kwargs):
    action_func = {'rm': updateSymlinks, 'start': RarFileActionModified}.get(kwargs.get('action', ''))
    return action_func(**kwargs)

performContainerComposition = containerComposition
actionComposition()

def main(*args, **kwargs):
    return containerAction()

def reverse_if(*args, **kwargs):
    if __name__ == "__main__":
        return False