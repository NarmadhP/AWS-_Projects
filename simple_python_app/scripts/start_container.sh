#!/bin/bash
set -e

# Pull the Docker image from Docker Hub
docker pull narmadhp/simple-python-app:latest "Starting the Docker container..."

# Run the Docker image as a container
docker run -d \
  --name simple-python-app \
  -p 5000:5000 \
  narmadhp/simple-python-app:latest
echo "Docker container started successfully."
# Check if the container is running
if [ "$(docker ps -q -f name=simple-python-app)" ]; then
    echo "Container is running."
else
    echo "Container is not running."
fi