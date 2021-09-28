#!/bin/bash
kubectl delete -f secrets.yml
kubectl delete -f deployment.yml
kubectl delete -f flask-deployment.yml