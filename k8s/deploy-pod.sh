#!/bin/bash

kubectl apply -f ./k8s/create_pod.yaml
kubectl expose pod flask-server-pod --selector "app=my_flask" --type=LoadBalancer --port=5000
kubectl apply -f ./k8s/createdb.yml
kubectl apply -f ./k8s/createdbimage.yml
kubectl apply -f ./k8s/createdbservice.yml
sleep 3
minikube service flask-server-pod
