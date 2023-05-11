#!/bin/bash
echo "Container Started"

cd /workspace/server

python3 main.py &
echo "Server Started, version 0.1.0"

cd /
jupyter lab --allow-root --no-browser --port=8888 --ip=* \
        --ServerApp.terminado_settings='{"shell_command":["/bin/bash"]}' \
        --ServerApp.token=$JUPYTER_PASSWORD --ServerApp.allow_origin=* --ServerApp.preferred_dir=/workspace
echo "Jupyter Lab Started"

sleep infinity
