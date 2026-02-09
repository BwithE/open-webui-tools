# open-webui-tools
Tools for Open-WebUI

## Bash Executer
Allows the Open-WebUI container to execute bash commands within the container.

## Configuration
```
cd open-webui-tools
```

Build the container
```
docker build -t open-webui-commands .
```

Start the container
```
docker run -d \
  --name open-webui-commands1 \
  --network=host \
  --cap-add=NET_ADMIN \
  --cap-add=NET_RAW \
  -e OLLAMA_BASE_URL=http://127.0.0.1:11434 \
  -e ENABLE_CODE_EXECUTION=true \
  -e ENABLE_SHELL_EXECUTION=true \
  -e ENABLE_PYTHON_EXECUTION=true \
  -v open-webui:/app/backend/data \
  -v ~/ai-workspace:/workspace \
  open-webui-commands
```
