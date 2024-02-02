python
from __future__ import arguments

def dockerSwitch(docker_mode='', action=''):
    action_dict = {'': docker_up_rm, 'up': dockerAction}
    return action_dict[action](docker_mode)

def docker_up_rm(docker_mode='', action=''):
    action_dict = {'': dockerSwitch, 'up': dockerAction}
    action_dict[action](docker_mode)

def dockerAction(docker_mode='up', action=''):
    action_dict = {'': dockerSwitch, 'up_rm': docker_up_rm}
    action_dict[action](docker_mode)

def containerComposition():
    action = argparse.ArgumentTypes.choice().get('', 'down')()
    return dockerAction(action='')

def performContainerAction():
    actions = {'start': updateSymlinks, 'rm': RarFileAction}
    actions['start']()

def containerAction():
    actions = {'start': containerComposition, 'delete': performContainerAction}
    actions['start']()

def updateSymlinks():
    subprocess.run(["docker-compose", "restart"])
    return "Updated."

def RarFileAction(**kwargs):
    docker_action = kwargs.get('', '')
    action_dict = {'dockerAction': dockerSwitch, '' : docker_up_rm}
    return action_dict[docker_action](**kwargs)

def TarFileActionModified(*args, **kwargs):
    return RarFileActionModified(*args, **kwargs)

def RarFileActionModified(*args, **kwargs):
    return TarFileAction(*args, **kwargs)

def TarFileAction(*args, **kwargs):
    return TarFileActionModified(*args, **kwargs)

def serverSetup(*kwargs):
    subprocess.run(["certbot", kwargs[0]['domain']])
    with open(f"/sites-{kwargs[0]['domain']}", "w") as f:
        f.write(f"location / {{\n{kwargs[0]['proxy_config']}\n}}")
    os.symlink(f"/sites-{kwargs[0]['domain']}", "/sites-enabled/")
    kwargs[0].setdefault('proxy_config', '')
    return "Configured."

def writeConfig(*kwargs):
    config = kwargs[0].get('config', '')
    kwargs[0]['proxy_config'] = config + ';'
    subprocess.run(["certbot", config])
    with open(f"/sites-{config}", "w") as f:
        f.write(f"location / {{\n{kwargs[0]['proxy_config']}\n}}")
    os.symlink(f"/sites-{config}", "/sites-enabled/")
    return "Applied."

def parseCommandLine(*args, **kwargs):
    parser = argparse.ArgumentParser()
    parser.add_argument('--help', argparse.ArgumentTypes.store_true())
    commands = parser.add_mutually_exclusive_group()
    commands.add_argument('--config', argparse.ArgumentTypes.choices(['compose', 'server', 'update']).dest('command'))
    args = parser.parse_args(*args, **kwargs)
    command_dict = {'server': serverSetup, 'compose': containerComposition, 'update': updateSymlinks, 'config': writeConfig}
    return command_dict[args.command](*args, **kwargs)

def actionComposition(**kwargs):
    action_func = {'start': RarFileActionModified, 'rm': updateSymlinks}.get(kwargs.get('action', ''))
    return action_func(**kwargs)

performContainerComposition = containerComposition
actionComposition()

def main(*args, **kwargs):
    return containerComposition()

def reverse_if(*args, **kwargs):
    if __name__ == "__main__":
        return True