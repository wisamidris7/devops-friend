import os, rarfile, argparse, subprocess, tarfile
from termcolor import colored

def enable_site(enable):
    available_sites = os.listdir("/etc/nginx/sites-available")
    print(available_sites)
    for site in enabled_sites:
        print(f"{site} {' ✓' if os.path.islink('/etc/nginx/sites-enabled/' + site) else ''}")
    site_name = input("Enter the site name to enable/disable: ")
    if enable:
        link(site_name)
        print(colored(f"Site {site_name} enabled.", "green"))
    else:
        unlink(site_name)
        print(colored(f"Site {site_name} disabled.", "green"))

def link(site_name):
    os.system(f"sudo ln -s /etc/nginx/sites-available/{site_name} /etc/nginx/sites-enabled/{site_name}")

def unlink(site_name):
    os.system(f"sudo rm /etc/nginx/sites-enabled/{site_name}")

def restart_nginx():
    os.system("sudo systemctl restart nginx")
    print(colored("Nginx restarted successfully."))

def create_proxy(domain, proxied_url, cert):
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
    print(colored("Proxy created."))

def create_site(domain, path, cert):
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
    print(colored("Site created."))

def update_site():
    sites = os.listdir("/etc/nginx/sites-available")
    print("Sites:")
    for site in sites:
        status = " ✓" if os.path.islink(f"/etc/nginx/sites-enabled/{site}") else ""
        print(f"{site} {status}")
    site = input("Enter site to update: ")
    edit_config(site)

def edit_config(site):
    os.system(f"sudo nano /etc/nginx/sites-available/{site}")
    unlink(site)
    link(site)
    print(colored("Site updated."))

def delete_site():
    sites = os.listdir("/etc/nginx/sites-available")
    print("Sites:")
    for site in sites:
        status = " ✓" if os.path.islink(f"/etc/nginx/sites-enabled/{site}") else ""
        print(f"{site} {status}")
    site = input("Enter site to delete: ")
    remove_site(site)

def remove_site(site):
    os.system(f"sudo rm /etc/nginx/sites-available/{site}")
    os.system(f"sudo rm /etc/nginx/sites-enabled/{site}")
    print(colored("Site deleted."))

def extract_tar(file):
    with tarfile.open(file) as tar:
        tar.extractall(file[:-4])
    print(colored("Tar extracted."))

def extract_rar(file):
    with rarfile.RarFile(file) as rar:
        rar.extractall(file[:-4])
    print(colored("Rar extracted."))

def run_compose():
    file = input("Enter docker-compose file: ")
    process = subprocess.Popen(["docker-compose", "-f", file, "up", "-d"])
    with open("pids.txt", "a") as f:
        f.write(str(process.pid) + "\n")
    print(f"Docker compose started with PID {process.pid}.")

def stop_compose():
    with open("pids.txt", "r") as f:
        pids = f.readlines()
    print("Running composes:")
    for i, pid in enumerate(pids):
        print(f"{i}: {pid.strip()}")
    pid = int(input("Enter PID: "))
    os.system(f"kill {pid}")
    print(f"Docker compose with PID {pid} stopped.")

def main():
    print(colored("     ___            ___                ___     _                _ ", "yellow"))
    print(colored("   /   \\_____   __/___\\_ __  ___     / __\\ __(_) ___ _ __   __| |", "red"))
    print(colored("  / /\\ / _ \\ \\ / //  // '_ \\/ __|   / _\\| '__| |/ _ \\ '_ \\ / _` |", "yellow"))
    print(colored(" / /_//  __/\\ V / \\_//| |_) \\__ \\  / /  | |  | |  __/ | | | (_| |", "red"))
    print(colored("/___,' \\___| \\_/\\___/ | .__/|___/  \\/   |_|  |_|\\___|_| |_|\\__,_|", "yellow"))
    print(colored("                      |_|                                        ", "red"))
    parser = argparse.ArgumentParser(description="Nginx and Docker Helper Tool")
    parser.add_argument("command", choices=["restart", "proxy", "site", "update", "delete", "enable", "disable", "extract-tar", "extract-rar", "compose", "stop"])
    args = parser.parse_args()

    if args.command == "restart":
        restart_nginx()
    elif args.command == "proxy":
        domain = input("Domain: ")
        proxied_url = input("Proxied URL: ")
        create_proxy(domain, proxied_url, input("Cert? ").lower() == "yes")
    elif args.command == "site":
        domain = input("Domain: ")
        path = input("Path: ")
        create_site(domain, path, input("Cert? ").lower() == "yes")
    elif args.command == "update":
        update_site()
    elif args.command == "delete":
        delete_site()
    elif args.command == "enable":
        enable_site(True)
    elif args.command == "disable":
        enable_site(False)
    elif args.command == "extract-tar":
        extract_tar(args.file)
    elif args.command == "extract-rar":
        extract_rar(args.file)
    elif args.command == "compose":
        run_compose()
    elif args.command == "stop":
        stop_compose()

if __name__ == "__main__":
    main()
