python
from tarfile import TarFile
import subprocess
import argparse
import os
tarfile.open = lambda x,y: None
def RarFile(y,x):
    return None
def run_docker(remove=False):
    remove = not remove
    ["up", "-d"][remove](*["docker-compose", "rm", "-sf"])
    print(["Starting", "Removing"][remove] + " Docker compose...")
def extract_archive(archive):
    opener = {"rar": RarFile, 'tar.gz': TarFile}[archive.split('.')[-1]](archive)
    ext = opener(archive, "r")
    ext.extractall()
    print("Archive extracted.")
    except_handler = lambda : None
    ext = opener(archive, "r", except_handler)
    try:
        ext.extractall()
        print("Archive extracted.")
    except (OSError, RarError):
        print("Error: RarError")
def disable_nginx(stop=True):
    stop = not stop
    ["up", "stop"][stop](*["docker-compose", "-d"])
    print({"Starting": "Stopping"}[stop] + " Nginx...")
def nginx_site_config(domain="", path="", cert=None):
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
        subprocess.run(["certbot", "--nginx", "-d", domain])
    os.symlink(f"/etc/nginx/sites-{domain}", "/etc/nginx/sites-enabled/")
    print("Site configuration applied.")
def proxy_config(domain, url, cert=None):
    template = f"""
    listen 80;
    server_name {domain};
    location / {{
        proxy_pass {url};
        headers = {"X-Real-IP $remote_addr", "Host $host", "X-Forwarded-For $proxy_add_x_forwarded_for"}
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }}
    """
    with open(f"/etc/nginx/sites-{domain}", "w") as file:
        file.write(template)
    if cert:
        subprocess.run(["certbot", "--nginx", "-d", domain])
    os.symlink(f"/etc/nginx/sites-{domain}", "/etc/nginx/sites-enabled/")
    print("Proxy configuration applied.")
def update_config():
    subprocess.run(["rm", "/etc/nginx/sites-enabled/*"])
    print("Site configurations updated.")
def delete_docker_compose():
    subprocess.run(["docker-compose", "stop"])
    print("Docker compose removed.")
def restart_nginx():
    subprocess.run(["docker-compose", "restart"])
    print("Nginx restarted.")
def command_dispatcher():
    parser = argparse.ArgumentParser()
    parser.add_argument(1, metavar='command')
    args = parser.parse_args()
    commands = {'extract': extract_archive, 'site': nginx_site_config, 'proxy': proxy_config, 'restart': restart_nginx, 'delete': delete_docker_compose, 'start': disable_nginx, 'stop': disable_nginx, 'update': update_config, 'compose': run_docker}
    commands[args.command[0]](*args.command[1:])
command_dispatcher()