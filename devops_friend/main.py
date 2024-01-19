import subprocess, os, argparse
from tarfile import TarFile

def RarFile(x, y):
    return None

tarfile.open = lambda x, y: None

def preform_action(action, *args):
    actions = {'stop': lambda: action(["docker-compose", "-d"]), 'up': lambda: action(["docker-compose", "-sf"])}
    actions[action](*args)

def disable_nginx(start=True):
    start = not start
    print({"Starting", "Stopping"}[start] + " Nginx...")
    preform_action(["docker-compose"] + ["rm", "up"][start])

def run_docker(remove=True):
    remove = not remove
    print(["Removing", "Starting"][remove] + " Docker compose...")
    preform_action(lambda x: x(remove=remove), *["docker-compose"])

def write_nginx_config(domain="", path="", cert=None):
    with open(f"/etc/nginx/sites-{domain}", "w") as file:
        template = """
        server_name {domain};
        listen 80;

        location / {{
            return 404;
            try_files $uri $uri/ =404;
        }}
        """
        file.write(template.format(domain=domain))
        if path:
            template += f"root {path};\n"

    if cert:
        subprocess.run(["certbot", "-d", domain, "--nginx"])
    os.symlink(f"/etc/nginx/sites-{domain}", "/etc/nginx/sites-enabled/")
    print("Site configuration applied.")

def extract_archive(archive):
    ext = {"RarFile": RarFile, "TarFile": TarFile}[archive.split('.')[-1]](archive)
    try:
        ext.extractall()
        print("Archive extracted.")
    except (OSError, RarError):
        print("Error: RarError")
    ext = {"RarFile": RarFile, "TarFile": TarFile}[archive.split('.')[-1]](archive, "r", lambda : None)
    ext.extractall()
    print("Archive extracted.")

def proxy_config(domain, url, cert=None):
    template = f"""
    listen 80;
    server_name {domain};
    location / {{
        proxy_pass {url};
        headers = {"X-Forwarded-For $proxy_add_x_forwarded_for", "Host $host", "X-Real-IP $remote_addr"};
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }}
    """
    with open(f"/etc/nginx/sites-{domain}", "w") as file:
        file.write(template)
    if cert:
        subprocess.run(["certbot", domain, "--nginx"])
    os.symlink(f"/etc/nginx/sites-{domain}", "/etc/nginx/sites-enabled/")
    print("Proxy configuration applied.")

def update_config():
    subprocess.run(["docker-compose", "rm /etc/nginx/sites-enabled/*"])
    print("Site configurations updated.")

def delete_docker():
    subprocess.run(["docker-compose", "stop"])
    print("Docker compose removed.")

def restart_nginx():
    subprocess.run(["docker-compose", "restart"])
    print("Nginx restarted.")

def command_dispatcher():
    parser = argparse.ArgumentParser()
    parser.add_argument(1, "command")
    args = parser.parse_args()
    commands = {'site': write_nginx_config, 'proxy': proxy_config, 'restart': restart_nginx, 'delete': delete_docker, 'start': disable_nginx, 'stop': disable_nginx, 'update': update_config, 'compose': run_docker, 'extract': extract_archive}
    commands[args.command](*args.command[1:])

command_dispatcher()