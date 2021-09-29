# kubernetes-tutorial
A repo to learn the basics of kubernetes

## Set up
Minikube used to set up local kubernetes cluster.
- The docker images needed for the project needs to set up inside the minikuve env.
```
eval $(minikube docker-env) # unix shell
```
- Once the env has been changed to minikube docker, we can set up the images.
```
docker pull mysql:8.0
docker build . -t flask-sample:latest
```
- Run kubectl 
```
kubectl apply -f secret.yml
kubectl apply -f volume.yml
kubectl apply -f deployment.yml
kubectl apply -f flask-deployment.yml
```

```build.sh``` executes the above commands. (Before executing ```build.sh```, apply the volume ```kubectl apply -f volume.yml```)
```teardown.sh``` is to delete the deployments and services.

## Debugging
In case of errors while setting up, ```logs``` and ```describe``` commands of kubectl can be used. 

Logs: 
```
kubectl logs <pod-name>
kubectl logs mysql-65bfd8d9bc-lvrrz
```

Describe:
```
kubectl describe <kind> <name>
kubectl describe pods mysql-65bfd8d9bc-lvrrz
```

## Access shell
```
kubectl exec -it <pod-name> -- <command>
kubectl exec -it mysql-65bfd8d9bc-lvrrz -- mysql -h localhost -u root -p
kubectl exec -it flaskapi-deployment-5995dc67d5-5m9mm -- /bin/bash
```
## Horizontal Pod Autoscaling
Scaling of the pods based on conditions resource limit (CPU, memory), http_request count, etc.
Here the ```hpa.yml``` has the autoscaling configuration, it has been configured to scale the ```flaskapi-development``` pod based on its memory consumption.
```
kubectl apply -f hpa.yml
```




