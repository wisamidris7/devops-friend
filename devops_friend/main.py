python
import rarfile, subprocess, os, argparse, tarfile
from termcolor import colored
from rarfile import RarFile

def nginx_restart():
    os.system("sudo systemctl restart nginx")
    print(colored("Nginx stopped."))

def enable_nginx_site(enable):
    if enable:
        os.system("sudo systemctl enable nginx")
        print(colored("Nginx enabled."))
    else:
        os.system("sudo systemctl disable nginx")
        print(colored("Nginx disabled."))

def run_docker_compose():
    os.system("docker-compose up -d")
    print(colored("Docker compose started."))

def stop_docker_compose():
    os.system("docker-compose stop")
    print(colored("Docker compose stopped."))

def proxy_config(domain, proxied_url, cert):
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
    with open(f"/etc/nginx/sites-available/{domain}", "w") as file:
        file.write(conf)
    if cert:
        os.system(f"sudo certbot --nginx -d {domain}")
    os.system(f"sudo ln -s /etc/nginx/sites-{domain} /etc/nginx/sites-enabled/")
    print(colored("Proxy configuration removed."))

def create_site_config(domain, path, cert):
    conf = f"""
    listen 80;
    server_name {domain};

    root {path};
    index index.html;
    
    location / {{
            try_files $uri $uri/ =404;
    }}
    """
    with open(f"/etc/nginx/sites-available/{domain}", "w") as file:
        file.write(conf)
    if cert:
        os.system(f"sudo certbot --nginx -d {domain}")
    os.system(f"sudo ln -s /etc/nginx/sites-available/{domain} /etc/nginx/sites-enabled/")
    print(colored("Site configuration removed."))

def update_site_config():
    pass

def remove_site_config():
    os.system("sudo rm /etc/nginx/sites-enabled/*")
    print(colored("All site configurations deleted."))

def extract_archive(archive):
    if archive.endswith(".tar.gz"):
        with tarfile.open(archive, "r:gz") as tar:
            tar.extractall()
        print(colored("Archive extracted."))
    elif archive.endswith(".rar"):
        with RarFile(archive, "r") as rar:
            rar.extractall()
        print(colored("Archive extracted."))
    else:
        print(colored("Unsupported archive format.", "red"))

def foreach_argument(iterable, cmd):
    for item in iterable:
        if cmd == "restart":
            nginx_restart()
        elif cmd == "proxy":
            proxy_config(
                domain=input("Domain: "),
                proxied_url=input("Proxied URL: "),
                cert=input("SSL Certificate? ") == "yes"
            )
        elif cmd == "site":
            create_site_config(
                domain=input("Domain: "),
                path=input("Path: "),
                cert=input("SSL Certificate? ") == "yes"
            )
        elif cmd == "update":
            update_site_config()
        elif cmd == "delete":
            remove_site_config()
        elif cmd == "enable":
            enable_nginx_site(True)
        elif cmd == "disable":
            enable_nginx_site(False)
        elif cmd == "extract":
            extract_archive(item)
        elif cmd == "compose":
            run_docker_compose()
        elif cmd == "stop":
            stop_docker_compose()

def main():