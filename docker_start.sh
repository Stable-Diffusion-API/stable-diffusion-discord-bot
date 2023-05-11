#!/bin/bash

echo "Container Started"

cd /workspace/server

python3 main.py &

echo "Discord Server Started, version 0.1.0"

sleep infinity
