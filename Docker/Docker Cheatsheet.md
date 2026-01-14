# Docker Cheat sheet


### Docker Components
---
There are three key components in the Docker ecosystem:

- **Dockerfile**: A text file containing instructions (commands) to build a Docker image.
- **Docker Image**: A snapshot of a container, created from a Dockerfile. Images are stored in a registry, like Docker Hub, and can be pulled or pushed to the registry.
- **Docker Container**: A running instance of a Docker image.


### Docker Commands
---
Below are some essential Docker commands you'll use frequently:
- **`docker pull <image>`**: Download an image from a registry, like Docker Hub.
- **`docker build -t <image_name> <path>`**: Build an image from a Dockerfile, where <path> is the directory containing the Dockerfile.
- **`docker image ls`**: List all images available on your local machine.
- **`docker run -d -p <host_port>:<container_port> --name <container_name> <image>`**: Run a container from an image, mapping host ports to container ports.
- **`docker container ls`**: List all running containers.
- **`docker container stop <container>`**: Stop a running container.
- **`docker container rm <container>`**: Remove a stopped container.
- **`docker image rm <image>`**: Remove an image from your local machine.

## Building Container Images
### Dockerfile

A **Dockerfile** is a script with a set of instructions to build a Docker image. Here are some common Dockerfile commands:

- **`FROM <image>`**: Sets the base image (e.g., `FROM ubuntu:20.04`).
- **`LABEL key=value`**: Adds metadata to the image.
- **`RUN <command>`**: Executes a command during image build (e.g., installing packages).
- **`COPY <src> <dest>`**: Copies files/directories from local context to the image.
- **`ADD <src> <dest>`**: Like COPY, but supports remote URLs and unpacking archives.
- **`WORKDIR <path>`**: Sets the working directory for subsequent instructions.
- **`ENV <key>=<value>`**: Sets environment variables.
- **`EXPOSE <port>`**: Documents the port the container listens on.
- **`CMD ["executable", "param1", ...]`**: Sets the default command to run when the container starts.
- **`ENTRYPOINT ["executable", "param1", ...]`**: Sets the main command for the container (overrides CMD).

**Example Dockerfile:**
```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]
```


### Creating a Docker Image Using a Dockerfile

To build a Docker image from a Dockerfile, use the following command in the directory containing your Dockerfile:

```sh
docker build -t <image_name>:<tag> .
```

- `<image_name>`: Name you want to give your image (e.g., `myapp`).
- `<tag>`: (Optional) Tag for the image (e.g., `latest`). Defaults to `latest` if omitted.
- `.`: The build context, usually the current directory.

**Example:**
```sh
docker build -t myapp:latest .
```

This command reads the `Dockerfile` in the current directory and creates an image named `myapp` with the `latest` tag.

## Container Registries
### Uploading (Pushing) a Docker Image to a Registry

After building your Docker image, you can upload (push) it to a Docker registry like Docker Hub:

1. **Tag your image** (if not already tagged for the registry):
   ```sh
   docker tag <image_name>:<tag> <registry_username>/<repository>:<tag>
   ```
   Example:
   ```sh
   docker tag myapp:latest myusername/myapp:latest
   ```

2. **Log in to Docker Hub** (or your registry):
   ```sh
   docker login
   ```

3. **Push the image**:
   ```sh
   docker push <registry_username>/<repository>:<tag>
   ```
   Example:
   ```sh
   docker push myusername/myapp:latest
   ```

## Running Containers
### Docker Run

The `docker run` command creates and starts a container from an image.

#### Basic Syntax

```sh
docker run [OPTIONS] <image> [COMMAND] [ARG...]
```

#### Common Options

| Option | Description |
|--------|-------------|
| `-d, --detach` | Run container in background |
| `-p, --publish <host>:<container>` | Map host port to container port |
| `--name <name>` | Assign a name to the container |
| `-e, --env <KEY>=<VALUE>` | Set environment variables |
| `-v, --volume <host>:<container>` | Mount a volume |
| `--rm` | Automatically remove container when it exits |
| `-it` | Interactive mode with terminal (combine `-i` and `-t`) |
| `--network <network>` | Connect to a specific network |
| `--restart <policy>` | Restart policy (`no`, `always`, `on-failure`, `unless-stopped`) |
| `-w, --workdir <path>` | Set working directory inside container |

#### Examples

**Run a container in detached mode with port mapping:**
```sh
docker run -d -p 8080:80 --name my-nginx nginx:latest
```

**Run interactively with a shell:**
```sh
docker run -it --rm ubuntu:22.04 /bin/bash
```

**Run with environment variables and volume:**
```sh
docker run -d \
  --name my-app \
  -e DATABASE_URL=postgres://localhost/db \
  -v $(pwd)/data:/app/data \
  -p 3000:3000 \
  myapp:latest
```

**Run with automatic cleanup:**
```sh
docker run --rm -it python:3.11 python --version
```

### Docker Compose

**Docker Compose** is a tool for defining and running multi-container Docker applications using a YAML file.

#### docker-compose.yml Structure

```yaml
version: '3.8'

services:
  web:
    image: nginx:latest
    ports:
      - "8080:80"
    volumes:
      - ./html:/usr/share/nginx/html
    depends_on:
      - db

  db:
    image: postgres:15
    environment:
      POSTGRES_USER: admin
      POSTGRES_PASSWORD: secret
      POSTGRES_DB: mydb
    volumes:
      - db_data:/var/lib/postgresql/data

volumes:
  db_data:
```

#### Common Docker Compose Commands

- **`docker compose up`**: Create and start all containers defined in the compose file.
- **`docker compose up -d`**: Start containers in detached (background) mode.
- **`docker compose down`**: Stop and remove containers, networks, and volumes.
- **`docker compose ps`**: List running containers managed by Compose.
- **`docker compose logs`**: View logs from all containers.
- **`docker compose logs -f <service>`**: Follow logs for a specific service.
- **`docker compose build`**: Build or rebuild services.
- **`docker compose exec <service> <command>`**: Execute a command in a running container.
- **`docker compose stop`**: Stop running containers without removing them.
- **`docker compose restart`**: Restart services.

#### Key docker-compose.yml Options

| Option | Description |
|--------|-------------|
| `image` | Specify the image to use |
| `build` | Build from a Dockerfile |
| `ports` | Map host:container ports |
| `volumes` | Mount host paths or named volumes |
| `environment` | Set environment variables |
| `depends_on` | Define service dependencies |
| `networks` | Specify custom networks |
| `restart` | Restart policy (`no`, `always`, `on-failure`, `unless-stopped`) |