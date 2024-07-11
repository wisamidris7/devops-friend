import os
import subprocess
import tarfile
import rarfile
import argparse
from termcolor import colored

# Function to restart Nginx
def restart_nginx():
    os.system("sudo systemctl restart nginx")
    print(colored("Nginx restarted successfully.", "green"))

# Function to create a reverse proxy
def create_reverse_proxy():
    domain = input("Enter the domain: ")
    proxied_url = input("Enter the proxied URL: ")
    generate_cert = input("Do you want to generate an SSL certificate (yes/no)? ").lower() == 'yes' if domain else False

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
    
    os.system(f"sudo ln -s /etc/nginx/sites-available/{domain} /etc/nginx/sites-enabled/")
    if generate_cert:
        os.system(f"sudo certbot --nginx -d {domain}")
    
    print(colored(f"Reverse proxy created for domain {domain} pointing to {proxied_url}.", "green"))

# Function to create a site for a given path
def create_for_path():
    path = input("Enter the path: ")
    domain = input("Enter the domain: ")
    generate_cert = input("Do you want to generate an SSL certificate (yes/no)? ").lower() == 'yes' if domain else False

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
    
    os.system(f"sudo ln -s /etc/nginx/sites-available/{domain} /etc/nginx/sites-enabled/")
    if generate_cert:
        os.system(f"sudo certbot --nginx -d {domain}")
    
    print(colored(f"Site created for path {path} with domain {domain}.", "green"))

# Function to update a site
def update_site():
    # List available sites
    available_sites = os.listdir("/etc/nginx/sites-available")
    print("Available Sites:")
    for site in available_sites:
        print(f"{site} {' ✓' if os.path.islink('/etc/nginx/sites-enabled/' + site) else ''}")

    site_name = input("Enter the site name to update: ")

    os.system(f"sudo nano /etc/nginx/sites-available/{site_name}")
    os.system(f"sudo rm /etc/nginx/sites-enabled/{site_name}")
    os.system(f"sudo ln -s /etc/nginx/sites-available/{site_name} /etc/nginx/sites-enabled/{site_name}")

    print(colored(f"Site {site_name} updated successfully.", "green"))

# Function to delete a site
def delete_site():
    # List available sites
    available_sites = os.listdir("/etc/nginx/sites-available")
    print("Available Sites:")
    for site in available_sites:
        print(f"{site} {' ✓' if os.path.islink('/etc/nginx/sites-enabled/' + site) else ''}")

    site_name = input("Enter the site name to delete: ")

    os.system(f"sudo rm /etc/nginx/sites-available/{site_name}")
    os.system(f"sudo rm /etc/nginx/sites-enabled/{site_name}")

    print(colored(f"Site {site_name} deleted successfully.", "green"))

# Function to enable/disable a site
def enable_site(enable):
    # List available sites
    available_sites = os.listdir("/etc/nginx/sites-available")
    print("Available Sites:")
    for site in available_sites:
        print(f"{site} {' ✓' if os.path.islink('/etc/nginx/sites-enabled/' + site) else ''}")

    site_name = input("Enter the site name to enable/disable: ")

    if enable:
        os.system(f"sudo ln -s /etc/nginx/sites-available/{site_name} /etc/nginx/sites-enabled/")
        print(colored(f"Site {site_name} enabled.", "green"))
    else:
        os.system(f"sudo rm /etc/nginx/sites-enabled/{site_name}")
        print(colored(f"Site {site_name} disabled.", "green"))

# Function to extract tar files
def extract_tar(file):
    with tarfile.open(file) as tar:
        tar.extractall(file[:-4])
    print(colored(f"Tar file {file} extracted.", "green"))

# Function to extract rar files
def extract_rar(file):
    with rarfile.RarFile(file) as rar:
        rar.extractall(file[:-4])
    print(colored(f"Rar file {file} extracted.", "green"))

# Function to run docker compose
def up_compose():
    compose_file = input("Enter the docker-compose file path: ")
    process = subprocess.Popen(["docker-compose", "-f", compose_file, "up", "-d"])
    with open("compose_pids.txt", "a") as f:
        f.write(str(process.pid) + "\n")
    print(colored(f"Docker compose started with PID {process.pid}.", "green"))

# Function to stop docker compose
def down_compose():
    with open("compose_pids.txt", "r") as f:
        pids = f.readlines()
    print("Active Docker Compose PIDs:")
    for i, pid in enumerate(pids):
        print(f"{i}: {pid.strip()}")
    pid_index = int(input("Enter the index of the process to stop: "))
    pid = pids[pid_index].strip()
    os.system(f"kill {pid}")
    print(colored(f"Docker compose with PID {pid} stopped.", "green"))

# Main function to parse arguments and execute the corresponding function
def main():         
    """Main function of devops-friend."""                     
    print(colored("     ___            ___                ___     _                _ ", "yellow"))
    print(colored("   /   \\_____   __/___\\_ __  ___     / __\\ __(_) ___ _ __   __| |", "red"))
    print(colored("  / /\\ / _ \\ \\ / //  // '_ \\/ __|   / _\\| '__| |/ _ \\ '_ \\ / _` |", "yellow"))
    print(colored(" / /_//  __/\\ V / \\_//| |_) \\__ \\  / /  | |  | |  __/ | | | (_| |", "red"))
    print(colored("/___,' \\___| \\_/\\___/ | .__/|___/  \\/   |_|  |_|\\___|_| |_|\\__,_|", "yellow"))
    print(colored("                      |_|                                        ", "red"))
    parser = argparse.ArgumentParser(description=colored("Nginx and Docker Helper Tool", "red"))
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("restart", help="Restart Nginx")

    subparsers.add_parser("create-reverse-proxy", help="Create a reverse proxy")

    subparsers.add_parser("create-for-path", help="Create a site for a given path")

    subparsers.add_parser("update", help="Update a site")

    subparsers.add_parser("delete", help="Delete a site")

    enable_parser = subparsers.add_parser("enable", help="Enable or disable a site")
    enable_parser.add_argument("enable", type=bool, help="True to enable, False to disable")

    extract_tar_parser = subparsers.add_parser("extract-tar", help="Extract a tar file")
    extract_tar_parser.add_argument("file", type=str, help="Tar file to extract")

    extract_rar_parser = subparsers.add_parser("extract-rar", help="Extract a rar file")
    extract_rar_parser.add_argument("file", type=str, help="Rar file to extract")

    subparsers.add_parser("up-compose", help="Run docker compose")

    subparsers.add_parser("down-compose", help="Stop docker compose")

    args = parser.parse_args()

    if args.command == "restart":
        restart_nginx()
    elif args.command == "create-reverse-proxy":
        create_reverse_proxy()
    elif args.command == "create-for-path":
        create_for_path()
    elif args.command == "update":
        update_site()
    elif args.command == "delete":
        delete_site()
    elif args.command == "enable":
        enable_site(args.enable)
    elif args.command == "extract-tar":
        extract_tar(args.file)
    elif args.command == "extract-rar":
        extract_rar(args.file)
    elif args.command == "up-compose":
        up_compose()
    elif args.command == "down-compose":
        down_compose()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
