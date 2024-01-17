python
from termcolor import colored
import subprocess, argparse, os, tarfile, rarfile
from rarfile import RarFile

def main():
    print(colored("     ___            ___                ___     _                _ ", "yellow"))
    print(colored("   /\_\_ \\_\_\_\_\_\_ / __/\_\_ __\_\_ \\_ \\_ \\_____| |__   ____   __| |", "red"))
    print(colored("  / /\\/ / ___/\_\_\_/ / / / \_ `\_ \\/_ \| ___| '_ \\_ / _ \\_ \\_ \\_", "yellow"))
    print(colored(" / /\_/ /_/ /\_\_\_\ \\_\ \\_| | | | \\/ /_/ / |_) |  __/ / / /", "red"))
    print(colored("/_/\_\___/\____/ \_______|_|_|\_\_\___| .__/ \___|_|\__\ ", "yellow"))
    print(colored("                      |_|                |_|            ", "red"))
    parser = argparse.ArgumentParser(description="Nginx and Docker Helper Tool")
    parser.add_argument("cmd", choices=["restart", "proxy", "site", "update", "delete", "enable", "disable", "extract", "compose", "stop"])
    args = parser.parse_args()

    if args.cmd == "restart":
        nginx_restart()
    elif args.cmd == "proxy":
        proxy_config(
            domain=input("Domain: "),
            proxied_url=input("Proxied URL: "),
            cert=input("SSL Certificate? ") == "yes"
        )
    elif args.cmd == "site":
        create_site_config(
            domain=input("Domain: "),
            path=input("Path: "),
            cert=input("SSL Certificate? ") == "yes"
        )
    elif args.cmd == "update":
        update_site_config()
    elif args.cmd == "delete":
        remove_site_config()
    elif args.cmd == "enable":
        enable_nginx_site(True)
    elif args.cmd == "disable":
        enable_nginx_site(False)
    elif args.cmd == "extract":
        extract_archive(args.archive)
    elif args.cmd == "compose":
        run_docker_compose()
    elif args.cmd == "stop":
        stop_docker_compose()

def nginx_restart():
    os.system("sudo systemctl restart nginx")
    print(colored("Nginx restarted."))

def proxy_config(domain, proxied_url, cert):
    conf = f"""
server {{
    listen 80;
    server_name {domain};

    location / {{
        proxy_pass {proxied_url};
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }}
}}
"""
    with open(f"/etc/nginx/sites-available/{domain}", "w") as file:
        file.write(conf)
    if cert:
        os.system(f"sudo certbot --nginx -d {domain}")
    os.system(f"sudo ln -s /etc/nginx/sites-available/{domain} /etc/nginx/sites-enabled/")
    print(colored("Proxy configuration created."))

def create_site_config(domain, path, cert):
    conf = f"""
server {{
    listen 80;
    server_name {domain};

    root {path};
    index index.html;

    location / {{
        try_files $uri $uri/ =404;
    }}
}}
"""
    with open(f"/etc/nginx/sites-available/{domain}", "w") as file:
        file.write(conf)
    if cert:
        os.system(f"sudo certbot --nginx -d {domain}")
    os.system(f"sudo ln -s /etc/nginx/sites-available/{domain} /etc/nginx/sites-enabled/")
    print(colored("Site configuration created."))

def update