#!/bin/bash
echo "Preparing environment"

minikube docker-env export DOCKER_TLS_VERIFY=”1" export DOCKER_HOST=”tcp://172.17.0.2:2376" export DOCKER_CERT_PATH=”/home/user/.minikube/certs” export MINIKUBE_ACTIVE_DOCKERD=”minikube”

eval $(minikube -p minikube docker-env)

docker pull mysql:8.0
docker build . -t flask-sample:latest



