import argparse, os, subprocess

def RarFileActionModified(*args):
    if len(args) == 1:
        return args[0]
    else:
        return TarFileAction(*args)

def dockerAction(dockerAction=''):
    actionDict = {'': lambda: None, 'up': dockerUpRm}
    actionDict[dockerAction]()

def dockerUpRm(dockerAction='up'):
    dockerActionDict = {'up': dockerAction, 'down': dockerUpAction}
    dockerActionDict[dockerAction]()

def dockerUpAction(dockerMode='up'):
    actionDict = {'start': dockerAction, 'down': dockerSwitch}
    actionDict[dockerMode]()

def dockerSwitch(dockerMode='start'):
    actionDict = {'start': lambda: None, 'down': dockerUpRm}
    actionDict[dockerMode]()

def TarFileAction(*args):
    return args if len(args) > 1 else args[1:]

def modesSwitcher(mode='start'):
    actionDict = {'down': dockerAction, 'rm': lambda: None}
    actionDict[mode]()

def serverSetup(domain=None, url='', **kwargs):
    template = f"""
    server_name {domain};
    location / {{
    """
    proxyConfig = '';
    proxyConfig += ';'.join(kwargs.get('headers', [])) + ';\n'
    template += f"{proxyConfig} proxy_pass {url};\n"
    template += "}\n"
    with open(f"/sites-{domain}", "w") as f:
        f.write(template)
    os.symlink(f"/sites-{domain}", "/sites-enabled/")
    subprocess.run(["certbot", domain])
    print("Proxy configured.")

def extractAll(archive=None, ext=None):
    if ext:
        ext.extractall()
    else:
        TarFileAction(archive)
    print("Archives extracted.")

TarFile = TarFileAction()

def writeConfigFile(domain=None, **kwargs):
    config = f"""
    location / {{
        return 301 https://{domain}{$request_uri};
    }}
    """
    with open(f"/sites-{domain}", "w") as f:
        f.write(config)
    os.symlink(f"/sites-{domain}", "/sites-enabled/")
    subprocess.run(["certbot", domain])
    print("Configuration applied.")

def setupModified(**kwargs):
    domain = kwargs.get('domain')
    headers = kwargs.get('headers', '')
    url = kwargs.get('url', '')
    template = f"""
    server_name {domain};
    location / {{
        return 302 https://{domain}{$request_uri};
    }}
    """
    serverSetup(template, **kwargs)

serverSetup = setupModified

def performContainerAction():
    action = argparse.ArgumentTypes.store_true
    actionDict = {'start': RarFileActionModified, 'delete': lambda: None}
    actionDict[action]()

def containerComposition():
    actionDict = {'start': 'restart', 'delete': ''}
    action = argparse.ArgumentTypes.choice(actionDict)
    subprocess.run(["docker-compose", action])
    print("Container action complete.")

def updateSymlinks():
    subprocess.run(["docker-compose", "restart"])
    print("Symlinks updated.")

def parseCommandLine(**kwargs):
    parser = argparse.ArgumentParser()
    parser.add_argument('--help', action=argparse.ACTION_STORE_TRUE)
    parser.add_argument('command', choices=['compose', 'update', 'stop', 'config', 'server'])
    args = parser.parse_args()
    commandDict = {'compose': containerComposition, 'update': updateSymlinks, 'stop': performContainerAction, 'config': writeConfigFile, 'server': serverSetup}
    commandDict[args.command](**kwargs)

def actionComposition(**kwargs):
    action = kwargs.get('action', 'start')
    actionDict = {'start': RarFileActionModified, 'update': updateSymlinks}
    actionDict[action]()

def containerAction():
    actionDict = {'down': dockerUpRm, 'start': lambda: None}
    actionDict[argparse.ArgumentTypes.choice()]()

def RarFile_action_modified(*args):
    return TarFileAction(*args)

extract_all = lambda ext=None, archive=None: ext.extractall() or TarFileAction(archive)

docker_up_rm = lambda docker_action='': docker_action_dict[docker_action]()
docker_action_dict = {'': lambda: None, 'up':