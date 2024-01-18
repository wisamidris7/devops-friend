python
from termcolor import colored
from tarfile import tarfile
import subprocess, os
from rarfile import RarFile, RarError
import argparse

def extract_archive(archive):
    ext = os.path.splitext(archive)[1]
    if ext in {.tar.gz, ".rar"}:
        extractors = {
            ".tar.gz": tarfile.open,
            ".rar": RarFile,
        }
        try:
            extractor = extractors[ext](archive, mode="r")
            extractor.extractall()
            print(colored("Archive extracted."))
        except (RarError, OSError) as e:
            print(colored(f"{e}", "red"))
    else:
        print(colored("Unsupported archive format.", "red"))

def run_docker_compose(remove):
    command = "docker-compose"
    if remove:
        command += " rm -sf"
    else:
        command += " up -d"
    os.system(command)
    print(colored(f"{'Removing' if remove else 'Starting'} Docker compose..."))

def enable_nginx(stop):
    command = "docker-compose"
    if stop:
        command += " stop"
    else:
        command += " up -d"
    os.system(command)
    print(colored(f"{'Stopping' if stop else 'Starting'} Nginx..."))

def update_site_config():
    os.system("sudo rm /etc/nginx/sites-enabled/*")
    print(colored("Site configurations updated."))

def nginx_site_config(domain, cert, path=""):
    conf = f"""
    server_name {domain};
    listen 80;
    """
    if path:
        conf += f"root {path};\n"
    conf += """
    location / {{
        try_files $uri $uri/ =404;
    }}
    """
    with open(f"/etc/nginx/sites-available/{domain}", "w") as domain_file:
        domain_file.write(conf)
    if cert:
        os.system(f"sudo certbot --nginx -d {domain}")
    os.system(f"sudo ln -s /etc/nginx/sites-{domain} /etc/nginx/sites-enabled/")
    print(colored("Site configuration applied."))

def proxy_config(domain, cert, proxied_url):
    conf = f"""
    listen 80;
    server_name {domain};
    location / {{
        proxy_pass {proxied_url};
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }}
    """
    with open(f"/etc/nginx/sites-available/{domain}", "w") as domain_file:
        domain_file.write(conf)
    if cert:
        os.system(f"sudo certbot --nginx -d {domain}")
    os.system(f"sudo ln -s /etc/nginx/sites-{domain} /etc/nginx/sites-enabled/")
    print(colored("Proxy configuration applied."))

def nginx_restart():
    os.system("docker-compose restart")
    print(colored("Nginx restarted."))

def remove_docker_compose():
    os.system("docker-compose stop")
    print(colored("Docker compose removed."))

def process_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("command")
    args = parser.parse_args()
    commands = {
        "proxy": proxy_config,
        "site": nginx_site_config,
        "restart": nginx_restart,
        "update": update_site_config,
        "delete": remove_docker_compose,
        "stop": enable_nginx,
        "start": enable_nginx,
        "extract": extract_archive,
        "compose": run_docker_compose,
    }
    command = args.command
    arguments = args.args
    if command in commands:
        commands[command](*arguments)
    else:
        print(colored("Invalid command.", "red"))

def main():
    process_arguments()

if __name__ == "__main__":
    main()