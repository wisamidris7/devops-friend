python
from rarfile import RarFile, RarError
import subprocess, os, argparse, tarfile
from termcolor import colored
import rarfile

def run_docker_compose(enable=False):
    command = "docker-compose"
    if enable:
        command += " up -d"
    else:
        command += " stop"
    os.system(command)
    print(colored(f"{'Starting' if enable else 'Stopping'} Docker compose..."))

def nginx_site_config(domain, path="", cert=False):
    conf = f"""
    listen 80;
    server_name {domain};
    """
    if path:
        conf += f"root {path};\n"
    conf += """
    location / {{
            try_files $uri $uri/ =404;
    }}
    """
    with open(f"/etc/nginx/sites-available/{domain}", "w") as file:
        file.write(conf)
    if cert:
        os.system(f"sudo certbot --nginx -d {domain}")
    os.system(f"sudo ln -s /etc/nginx/sites-{domain} /etc/nginx/sites-enabled/")
    print(colored("Site configuration applied."))

def proxy_configuration(domain, proxied_url, cert=False):
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
    print(colored("Proxy configuration applied."))

def remove_all_site_configs():
    os.system("sudo rm /etc/nginx/sites-enabled/*")
    print(colored("All site configurations removed."))

def extract_archive(archive):
    extract_methods = {
        ".tar.gz": tarfile.open,
        ".rar": RarFile,
    }

    ext = os.path.splitext(archive)[1]
    if ext in extract_methods:
        try:
            with extract_methods[ext](archive, "r") as archive_file:
                archive_file.extractall()
            print(colored("Archive extracted."))
        except (RarError, OSError) as e:
            print(colored(f"Failed to extract archive: {e}", "red"))
    else:
        print(colored("Unsupported archive format.", "red"))

def process_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("command")
    parser.add_argument("arguments", nargs="*")
    args = parser.parse_args()

    if args.command == "restart":
        nginx_restart()
    elif args.command == "proxy":
        proxy_config(
            domain=args.arguments[0],
            proxied_url=args.arguments[1],
            cert=args.arguments[2] == "yes",
        )
    elif args.command == "site":
        nginx_site_config(
            domain=args.arguments[0],
            path=args.arguments[1] if len(args.arguments) > 1 else "",
            cert=args.arguments[2] == "yes",
        )
    elif args.command == "update":
        update_site_config()
    elif args.command == "delete":
        remove_all_site_configs()
    elif args.command == "enable":
        enable_nginx(True)
    elif args.command == "disable":
        enable_nginx(False)
    elif args.command == "extract":
        extract_archive(args.arguments[0])
    elif args.command == "compose":