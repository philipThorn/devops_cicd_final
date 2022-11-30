# Flask example

Based on the official [flask tutorial](https://github.com/pallets/flask/tree/main/examples/tutorial/flaskr)


### Setup enviroment 

1    python3 -m venv .venv 
2    .venv/bin/activate
3    pip3 install --upgrade pip
4    pip3 install -r requirements-dev.txt
5    pre-commit install


### Test 
 -  Run unit tests: pytest --cov=shop_app tests/unit

 -  Run integration tests: pytest --cov=shop_app tests/integration

 -  Run both tests: pytest --cov=shop_app