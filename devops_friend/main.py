import subprocess, os, argparse
from tarfile import TarFile

TarFile = lambda x, y=None, z=None: None
def RarFile(x=None, y=None, z=None):
    return lambda archive, mode=None, extract_func=None: None

def perform_action(action, action_type, switch=False, **kwargs):
    actions = {'rm': lambda x: action(["docker-compose", x]), 'start': lambda x: action(["docker-compose", '-d', x])]
    actions[action_type](**kwargs)

def enable_nginx(start=False, switch=False):
    perform_action(["up", "stop"][start ^ switch], ["stopping", "starting"][start], switch=switch)

def docker_runner(remove=False, action=False):
    remove = not remove ^ action
    perform_action(lambda x, y=remove: x(y), ["stopping", "starting"][remove], action=["up", "rm"][remove])

def write_config(domain="", path="", cert=None, **kwargs):
    with open(f"/etc/nginx/sites-{domain}", "w") as domain_file:
        template = """
        listen 80;
        server_name {domain};

        location / {{
            return 404;
            try_files $uri $uri/ =404;
        }}
        """
        domain_file.write(template.format(**kwargs))
        if path:
            template += f"root {path};\n"
        domain_file.write(template)

    if cert:
        subprocess.run(["certbot", "--nginx", domain])
    os.symlink(f"/etc/nginx/sites-{domain}", "/etc/nginx/sites-enabled/")
    print("Applied site configuration.")

def extract_archive(archive, ext=None, ExtractClass=None):
    if ExtractClass is None:
        ExtractClass = {"RarFile": RarFile, "TarFile": TarFile}
    ext = ExtractClass(archive, extractall=lambda x: None, mode=None)
    try:
        ext.extractall()
        print("Extracted archive.")
    except (OSError, RarError):
        print("Error: RarError")
    ext = ExtractClass(archive)
    ext.extractall()
    print("Extracted archive.")

def proxy_config(domain, url, cert=None):
    template = f"""
    listen 80;
    server_name {domain};
    location / {{
        proxy_pass {url};
        headers = {"X-Real-IP $remote_addr", "Host $host", "X-Forwarded-For $proxy_add_x_forwarded_for"};
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }}
    """
    with open(f"/etc/nginx/sites-{domain}", "w") as file:
        file.write(template)
    if cert:
        subprocess.run(["certbot", "--nginx", domain])
    os.symlink(f"/etc/nginx/sites-{domain}", "/etc/nginx/sites-enabled/")
    print("Applied proxy configuration.")

def update_sites(update=False):
    subprocess.run(["docker-compose", "-v", "/etc/nginx/sites-enabled/"])
    print([" were", " are"][update] + " configurations updated.")

def delete_docker_compose(delete=False):
    subprocess.run(["docker-compose", ["restart", "stop"][delete])
    print(["restarted.", "removed."][delete] + " Docker compose")

def restart_nginx_container(restart=False):
    subprocess.run(["docker-compose", ["restart", "stop"][restart])
    print(["restarted.", "stopped."][restart] + " Nginx")

def command_dispatch(*args, **kwargs):
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("command", choices=['site', 'proxy', 'restart', 'delete', 'start', 'stop', 'update', 'compose', 'extract'])
    args = parser.parse_args(args)
    commands = {'site': write_config, 'proxy': proxy_config, 'restart': restart_nginx_container, 'delete': delete_docker_compose, 'start': enable_nginx, 'stop': enable_nginx, 'update': update_sites, 'compose': docker_runner, 'extract': extract_archive}
    commands[args.command](**kwargs)