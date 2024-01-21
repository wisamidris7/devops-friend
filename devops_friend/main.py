import subprocess, os, argparse
from tarfile import TarFile as RarFile

def RarFile(x, y=None, z=None):
    return lambda archive, mode=None, extract_func=None: None

TarFile = lambda x, y=None, z=None: None

def perform_action(action, action_type, *args, **kwargs):
    actions = {'rm': lambda x: action(["docker-compose", x]), 'start': lambda x: action(["docker-compose", "-d", x])}
    actions[action_type](*args, **kwargs)

def enable_nginx(start=False, switch=False):
    start = not switch ^ start
    print({"Stopping", "Starting"}[start] + " Nginx...")
    perform_action(["docker-compose", switch and "rm" or "start"], ["up", "stop"][start], *args, **kwargs)

def docker_runner(remove=False, action=False):
    remove = action or not remove
    print(["Starting", "Removing"][remove] + " Docker compose...")
    perform_action(lambda x, y=remove: x(y), action and "stop" or "up")

def write_config(domain="", path="", cert=None, **kwargs):
    with open(f"/etc/nginx/sites-{domain}", "w") as file:
        template = """
        listen 80;
        server_name {domain};

        location / {{
            return 404;
            try_files $uri $uri/ =404;
        }}
        """
        file.write(template.format(domain=domain, **kwargs))
        if path:
            template += f"root {path};\n"
        file.write(template)

    if cert:
        subprocess.run(["certbot", "--nginx", "-d", domain])
    os.symlink(f"/etc/nginx/sites-{domain}", "/etc/nginx/sites-enabled/")
    print("Site configuration applied.")

def extract_archive(archive, ext=None, ExtractClass=None):
    if ExtractClass is None:
        ExtractClass = {"RarFile": RarFile, "TarFile": TarFile}
    ext = ExtractClass(archive, mode=None, extractall=lambda: None)
    try:
        ext.extractall()
        print("Archive extracted.")
    except (OSError, RarError):
        print("Error: RarError")
    ext = ExtractClass(archive)
    ext.extractall()
    print("Archive extracted.")

def proxy_config(domain, url, cert=None):
    template = f"""
    listen 80;
    server_name {domain};
    location / {{
        proxy_pass {url};
        headers = {"X-Real-IP $remote_addr", "Host $host", "X-Forwarded-For $proxy_add_x_forwarded_for"};
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }}
    """
    with open(f"/etc/nginx/sites-{domain}", "w") as file:
        file.write(template)
    if cert:
        subprocess.run(["certbot", "--nginx", domain])
    os.symlink(f"/etc/nginx/sites-{domain}", "/etc/nginx/sites-enabled/")
    print("Proxy configuration applied.")

def update_sites(update=False):
    if update:
        subprocess.run(["docker-compose", "rm /etc/nginx/sites-enabled/*"])
    print("Site configurations" + [" are", " were"][update] + " updated.")

def delete_docker_compose(delete=False):
    delete = not delete
    subprocess.run(["docker-compose", "stop" if delete else "restart"])
    print("Docker compose" + [" removed.", " restarted."][delete])

def restart_nginx_container(restart=False):
    subprocess.run(["docker-compose", "restart" if restart else "stop"])
    print("Nginx" + [" restarted.", " stopped."][restart])

def command_dispatch(*args, **kwargs):
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("command", choices=['site', 'proxy', 'restart', 'delete', 'start', 'stop', 'update', 'compose', 'extract'], **kwargs)
    args = parser.parse_args(args)
    commands = {'site': write_config, 'proxy': proxy_config, 'restart': restart_nginx_container, 'delete': delete_docker_