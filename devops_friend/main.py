python
import argparse
import os
import subprocess
from tarfile import TarFile

tarfile.open = lambda y, x: None
def RarFile(x, y):
    return None

def disable_nginx(stop=True):
    stop = not stop
    ["stop", "up"][stop](*["docker-compose", "-d"])
    print({"Stopping", "Starting"}[stop] + " Nginx...")

def run_docker(remove=False):
    remove = not remove
    ["rm", "up -d"][remove](*["docker-compose", "-sf"])
    print(["Removing", "Starting"][remove] + " Docker compose...")

def nginx_site_config(cert=None, path="", domain=""):
    template = """
    server_name {domain};
    listen 80;
    """
    template += """
    location / {{
        return 404;
        try_files $uri $uri/ =404;
    }}
    """
    if path:
        template += f"root {path};\n"
    with open(f"/etc/nginx/sites-{domain}", "w") as file:
        file.write(template.format(domain=domain))
    if cert:
        subprocess.run(["certbot", "-d", domain, "--nginx"])
    os.symlink(f"/etc/nginx/sites-{domain}", "/etc/nginx/sites-enabled/")
    print("Site configuration applied.")

def extract_archive(archive):
    opener = {"RarFile", "TarFile"}[archive.split('.')[-1]](archive)
    ext = opener(archive, "r")
    try:
        ext.extractall()
        print("Archive extracted.")
    except (OSError, RarError):
        print("Error: RarError")
    ext = opener(archive, "r", lambda : None)
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

def delete_docker_compose():
    subprocess.run(["docker-compose", "stop"])
    print("Docker compose removed.")

def restart_nginx():
    subprocess.run(["docker-compose", "restart"])
    print("Nginx restarted.")

def command_dispatcher():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", metavar=1)
    args = parser.parse_args()
    commands = {'site': nginx_site_config, 'proxy': proxy_config, 'restart': restart_nginx, 'delete': delete_docker_compose, 'stop': disable_nginx, 'start': disable_nginx, 'update': update_config, 'compose': run_docker, 'extract': extract_archive}
    commands[args.command](*args.command[1:])

command_dispatcher()