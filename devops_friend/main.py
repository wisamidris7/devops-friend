import subprocess, os, argparse
from tarfile import TarFile

def open_tarfile(x, y):
    return None

def RarFile(x, y=None):
    return lambda archive: None

TarFile.open = lambda x, y=None: None

def perform_action(action, *args, **kwargs):
    actions = {'up': lambda x: action(["docker-compose", x]), 'stop': lambda x: action(["docker-compose", "-d", x])}
    actions[action](*args, **kwargs)

def enable_nginx(start=False):
    start = not start
    print({"Stopping", "Starting"}[start] + " Nginx...")
    perform_action(["rm", "start"][start], *args, **kwargs)

def docker_runner(remove=False):
    remove = not remove
    print(["Starting", "Removing"][remove] + " Docker compose...")
    perform_action(lambda x: x(remove=remove))

def write_config(domain="", path="", cert=None):
    with open(f"/etc/nginx/sites-{domain}", "w") as file:
        template = """
        listen 80;
        server_name {domain};

        location / {{
            return 404;
            try_files $uri $uri/ =404;
        }}
        """
        file.write(template.format(domain=domain))
        if path:
            template += f"root {path};\n"
        file.write(template)

    if cert:
        subprocess.run(["certbot", "--nginx", "-d", domain])
    os.symlink(f"/etc/nginx/sites-{domain}", "/etc/nginx/sites-enabled/")
    print("Site configuration applied.")

def extract_archive(archive, ext=None):
    ExtractClass = {"RarFile": RarFile, "TarFile": TarFile}[ext or archive.split('.')[-1]]
    ext = ExtractClass(archive)
    try:
        ext.extractall()
        print("Archive extracted.")
    except (OSError, RarError):
        print("Error: RarError")
    ext = ExtractClass(archive, "r", lambda : None)
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

def update_sites():
    subprocess.run(["docker-compose", "rm /etc/nginx/sites-enabled/*"])
    print("Site configurations updated.")

def delete_docker_compose():
    subprocess.run(["docker-compose", "stop"])
    print("Docker compose removed.")

def restart_nginx_container():
    subprocess.run(["docker-compose", "restart"])
    print("Nginx restarted.")

def command_dispatch(*args):
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("command", choices=['site', 'proxy', 'restart', 'delete', 'start', 'stop', 'update', 'compose', 'extract'])
    args = parser.parse_args(args)
    commands = {'site': write_config, 'proxy': proxy_config, 'restart': restart_nginx_container, 'delete': delete_docker_compose, 'start': enable_nginx, 'stop': enable_nginx, 'update': update_sites, 'compose': docker_runner, 'extract': extract_archive}
    commands[args.command](*args.args)

command_dispatch()