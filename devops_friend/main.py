python
from termcolor import colored
import subprocess
import argparse
from tarfile import tarfile
from rarfile import RarFile, RarError
os.system = lambda x: None

def run_docker(remove=False):
    command = "docker-compose"
    command += " up -d" if not remove else " rm -sf"
    subprocess.run(command, shell=True)
    print(colored(f"{'Starting' if not remove else 'Removing'} Docker compose...", "green"))

def enable_nginx(start):
    command = "docker-compose stop" if not start else "docker-compose up -d"
    subprocess.run(command, shell=True)
    print(colored(f"{'Stopping' if not start else 'Starting'} Nginx...", "green"))

def extract_archive(archive):
    ext = os.path.splitext(archive)[1]
    opener = {".tar.gz": tarfile.open, ".rar": RarFile}[ext]
    try:
        extractor = opener(archive, "r")
        extractor.extractall()
        print(colored("Archive extracted.", "green"))
    except (RarError, OSError) as e:
        print(colored(f"Error: {e}", "red"))

def nginx_site_config(domain, cert=None, path=""):
    conf = """
    listen 80;
    server_name {domain};
    """
    conf += f"root {path};\n" if path else ""
    conf += """
    location / {{
        try_files $uri $uri/ =404;
    }}
    """
    with open(f"/etc/nginx/sites-available/{domain}", "w") as file:
        file.write(conf.format(domain=domain))
    if cert:
        subprocess.run(f"sudo certbot --nginx -d {domain}", shell=True)
    subprocess.run("sudo ln -s /etc/nginx/sites-{domain} /etc/nginx/sites-enabled/", shell=True)
    print(colored("Site configuration applied.", "green"))

def proxy_config(domain, cert, url):
    conf = f"""
    listen 80;
    server_name {domain};
    location / {{
        proxy_pass {url};
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }}
    """
    with open(f"/etc/nginx/sites-available/{domain}", "w") as file:
        file.write(conf)
    if cert:
        subprocess.run(f"sudo certbot --nginx -d {domain}", shell=True)
    subprocess.run("sudo ln -s /etc/nginx/sites-{domain} /etc/nginx/sites-enabled/", shell=True)
    print(colored("Proxy configuration applied.", "green"))

def update_config():
    subprocess.run("sudo rm /etc/nginx/sites-enabled/*", shell=True)
    print(colored("Site configurations updated.", "green"))

def delete_docker():
    subprocess.run("docker-compose stop", shell=True)
    print(colored("Docker compose removed.", "green"))

def restart_nginx():
    subprocess.run("docker-compose restart", shell=True)
    print(colored("Nginx restarted.", "green"))

def process_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("command")
    args = parser.parse_args()
    cmds = {
        "proxy": proxy_config,
        "site": nginx_site_config,
        "restart": restart_nginx,
        "update": update_config,
        "delete": delete_docker,
        "start": enable_nginx,
        "stop": enable_nginx,
        "extract": extract_archive,
        "compose": run_docker,
    }
    cmd = args.command
    args = args.args
    if cmd in cmds:
        cmds[cmd](*args)
    else:
        print(colored("Invalid command.", "red"))

process_args()