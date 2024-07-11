# DevOps Friend

**Disclaimer**: This tool is provided as-is. The author assumes no responsibility for any misuse or unethical practices. Use responsibly and in accordance with applicable laws and ethical standards.

## Overview

`devops-friend` is a command-line utility designed to simplify common DevOps tasks related to server management, Docker operations, and file handling. It provides straightforward commands to automate operations typically performed by DevOps engineers and system administrators.

## Features

- **Restart Nginx**: Quickly restarts the Nginx web server.
- **Create Reverse Proxy**: Sets up a reverse proxy configuration.
- **Create Site for Path**: Configures a site for a specific path on the server.
- **Update Site Configuration**: Updates the configuration of an existing site.
- **Delete Site**: Deletes a configured site from the server.
- **Enable/Disable Site**: Enables or disables a site configuration.
- **Extract Tar Archive**: Extracts files from a tar archive.
- **Extract Rar Archive**: Extracts files from a rar archive.
- **Manage Docker Compose**: Starts (`up-compose`) or stops (`down-compose`) Docker Compose services.

## Installation

### Prerequisites

- Python 3.x installed on your system.
- Pip package manager.

### Installation Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/wisamidris7/devops-friend.git
   cd devops-friend
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the tool:

   ```bash
   devops-friend --help
   ```

## Usage

### Command Syntax

```bash
devops-friend <command> [options]
```

### Commands:

- `restart`: Restarts the Nginx server.
- `create-reverse-proxy`: Creates a reverse proxy configuration.
- `create-for-path`: Configures a site for a specific path.
- `update`: Updates the configuration of an existing site.
- `delete`: Deletes a configured site.
- `enable`: Enables or disables a site.
- `extract-tar`: Extracts files from a tar archive.
- `extract-rar`: Extracts files from a rar archive.
- `up-compose`: Starts Docker Compose services.
- `down-compose`: Stops Docker Compose services.

### Example Usage:

Restart Nginx:

```bash
devops-friend restart
```

Create a reverse proxy for a service running on port 8080:

```bash
devops-friend create-reverse-proxy --port 8080
```

Extract files from a tar archive:

```bash
devops-friend extract-tar --file archive.tar.gz
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
