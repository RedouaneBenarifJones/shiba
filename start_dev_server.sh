#!/usr/bin/bash

# export PYTHONPATH="src"
# fastapi dev src/main.py

PYTHONPATH=src
DOCKER_IMAGE=users-service-image
DOCKER_CONTAINER=users-service-container
DOCKER_CONTAINER_PORT=80
HOST_PORT=8080

# clean
docker stop ${DOCKER_CONTAINER}
docker rm ${DOCKER_CONTAINER}
docker rmi ${DOCKER_IMAGE}

# docker build image
docker build \
  -t ${DOCKER_IMAGE} \
  -f Dockerfile \
  .

# docker run container
docker run \
  --name ${DOCKER_CONTAINER} \
  --mount type=bind,source=./src/,target=/app/src \
  -p ${HOST_PORT}:${DOCKER_CONTAINER_PORT} \
  -e PYTHONPATH=${PYTHONPATH} \
  ${DOCKER_IMAGE}
