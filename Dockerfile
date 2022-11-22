FROM python:3.11-slim

WORKDIR /devops_cicd/shop_app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY hello_flask hello_flask

EXPOSE 5000/tcp

ENV FLASK_APP=hello_flask

CMD [ "flask", "run", "--host=0.0.0.0"]
