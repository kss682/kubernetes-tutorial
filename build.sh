#!/bin/bash
echo "Preparing minikube..."

eval $(minikube docker-env)

docker pull mysql:8.0
docker build . -t flask-sample:latest

# kubectl
kubectl apply -f secrets.yml
kubectl apply -f deployment.yml
kubectl apply -f flask-deployment.yml
kubectl apply -f hpa.yml
