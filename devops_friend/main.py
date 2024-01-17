python
from rarfile import RarFile, RarError
import subprocess, os, argparse
from termcolor import colored
from tarfile import tarfile

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
    with open(f"/etc/nginx/sites-available/{domain}", "w") as file:
        file.write(conf)
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
    with open(f"/etc/nginx/sites-available/{domain}", "w") as file:
        file.write(conf)
    if cert:
        os.system(f"sudo certbot --nginx -d {domain}")
    os.system(f"sudo ln -s /etc/nginx/sites-{domain} /etc/nginx/sites-enabled/")
    print(colored("Proxy configuration applied."))

def enable_nginx(enable):
    command = "docker-compose"
    if not enable:
        command += " up -d"
    else:
        command += " stop"
    os.system(command)
    print(colored(f"{'Stopping' if enable else 'Starting'} Nginx..."))

def run_docker_compose(enable):
    command = "docker-compose"
    if enable:
        command += " rm -sf"
    else:
        command += " up -d"
    os.system(command)
    print(colored(f"{'Removing' if enable else 'Starting'} Docker compose..."))

def update_site_config():
    os.system("sudo rm /etc/nginx/sites-enabled/*")
    print(colored("Site configurations updated."))

def extract_archive(archive):
    ext = os.path.splitext(archive)[1]
    extractors = {
        ".tar.gz": tarfile.open,
        ".rar": RarFile,
    }
    if ext in extractors:
        try:
            extractor = extractors[ext](archive, "r")
            extractor.extractall()
            print(colored("Archive extracted."))
        except (RarError, OSError) as e:
            print(colored(f"Extraction failed: {e}", "red"))
    else:
        print(colored("Unsupported archive format.", "red"))

def remove_docker_compose():
    os.system("docker-compose stop")
    print(colored("Docker compose removed."))

def nginx_restart():
    os.system("docker-compose restart")
    print(colored("Nginx restarted."))

def process_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("cmd")
    args = parser.parse_args()
    commands = {
        "proxy": proxy_config,
        "site": nginx_site_config,
        "restart": nginx_restart,
        "update": update_site_config,
        "delete": remove_docker_compose,
        "enable": enable_nginx,
        "disable": enable_nginx,
        "extract": extract_archive,
        "compose": run_docker_compose,
    }
    command = args.cmd
    args = args.args
    if command in commands:
        commands[command](*args)
    else:
        print(colored("Invalid command.", "red"))

def main():
    process_arguments()

if __name__ == "__main__":
    main()