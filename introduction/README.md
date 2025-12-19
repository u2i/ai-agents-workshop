
# Quick Start

### Prerequisites
- [Docker](https://www.docker.com/products/docker-desktop/)
- [Task/Taskfile](https://taskfile.dev/docs/installation) (optional, but recommended)


## Option 1: Using Taskfile (Recommended)

1. **Complete setup with one command:**
   ```bash
   task setup
   ```

#### Available Task Commands

Run `task --list` to see all available commands, or use these common ones:

- `task start` - Start all services
- `task stop` - Stop all services
- `task pull-model` - Pull the Llama 3.2 model
- `task setup` - Complete setup (start + pull model)

## Option 2: Manual Docker Setup

1. **Start the services**:
   ```bash
   docker compose up -d
   ```

2. **Pull the Llama model** (after container is running):
   ```bash
   docker exec -it ollama ollama pull llama3.2
   ```

### After Setup is Done, Access Jupyter Notebooks:
   Open your browser and navigate to:
   ```
   http://localhost:8888/tree/introduction
   ```

   _You can also open it within your IDE, using the kernel link_:
   ```
   http://localhost:8888
   ```