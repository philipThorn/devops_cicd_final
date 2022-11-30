# Devops CICD Final

## Setup enviroment

Make sure you have docker, python, minikube and venv installed before continuing.
```
python3 -m venv .venv

. venv/bin/activate

pip3 install --upgrade pip

pip3 install -r requirements.txt

pre-commit install
```

## How to deploy with minikube
```
kubectl create secret docker-registry webserver --docker-server=<server> --docker-username=<username> --docker-password=<password> --docker-email=<email>

kubectl create secret generic mysqldb-secrets --from-file=MYSQL_PASSWORD=./user-password.txt --from-file=MYSQL_ROOT_PASSWORD=./password.txt
```
```
minikube start
```

### Scripts to deploy and remove pods and services
```
./k8s/deploy-pod.sh

./k8s/delete-pod-service.sh
```

### Local flask instance with docker for local testing.
```
docker network create my-network
.\scripts\db.sh
.\scripts\flask.sh
```
## Tests
Local flask instance is required to test integration.

Run unit tests:
```
pytest --cov=shop_app tests/unit
```
Run integration tests:
```
pytest --cov=shop_app tests/integration
```



# Contributors
## Albin
## Fredrik
## Philip
