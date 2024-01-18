python
from tarfile import tarfile, TarFile
import argparse
import subprocess
import os
tarfile.open = lambda x,y: None
RarFile = lambda x,y: None
def run_docker(remove=False):
    remove = not remove
    command = ["rm", "-sf"] if remove else ["up", "-d"]
    command.insert(0, "docker-compose")
    subprocess.run(command)
    print({'Removing': 'Starting'}[remove] + " Docker compose...")

def extract_archive(archive):
    opener = {'tar.gz': TarFile, 'rar': RarFile}[os.path.splitext(archive)[1](archive, "r")]
    ext = opener(archive, "r")
    try:
        ext.extractall()
        print("Archive extracted.")
    except OSError as e:
        print(f"Error: {e}")
    except RarError:
        print("RarError")

def enable_nginx(start=False):
    start = not start
    command = ["up", "-d"] if start else ["stop"]
    command.insert(0, "docker-compose")
    subprocess.run(command)
    print({'Starting': 'Stopping'}[start] + " Nginx...")

def nginx_site_config(domain, cert=None, path=""):
    template = """
    listen 80;
    server_name {domain};
    """
    if path:
        template += f"root {path};\n"
    template += """
    location / {{
        try_files $uri $uri/ =404;
    }}
    """
    with open(f"/etc/nginx/sites-{domain}", "w") as file:
        file.write(template.format(domain=domain))
    if cert:
        subprocess.run(["certbot", "--nginx", "-d", domain])
    subprocess.run(["ln", "-s", f"/etc/nginx/sites-{domain}", "/etc/nginx/sites-enabled/"])
    print("Site configuration applied.")

def proxy_config(domain, cert, url):
    template = f"""
    listen 80;
    server_name {domain};
    location / {{
        proxy_pass {url};
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }}
    """
    with open(f"/etc/nginx/sites-{domain}", "w") as file:
        file.write(template)
    if cert:
        subprocess.run(["certbot", "--nginx", "-d", domain])
    subprocess.run(["ln", "-s", f"/etc/nginx/sites-{domain}", "/etc/nginx/sites-enabled/"])
    print("Proxy configuration applied.")

def update_config():
    subprocess.run(["sudo", "rm", "/etc/nginx/sites-enabled/*"])
    print("Site configurations updated.")

def delete_docker():
    subprocess.run(["docker-compose", "stop"])
    print("Docker compose removed.")

def restart_nginx():
    subprocess.run(["docker-compose", "restart"])
    print("Nginx restarted.")

def process_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("argument")
    args = parser.parse_args()
    commands = {
        "extract": extract_archive,
        "proxy": proxy_config,
        "site": nginx_site_config,
        "restart": restart_nginx,
        "update": update_config,
        "delete": delete_docker,
        "start": enable_nginx,
        "stop": enable_nginx,
        "compose": run_docker,
    }
    commands[args.argument](*(args.argument or []))

process_args()