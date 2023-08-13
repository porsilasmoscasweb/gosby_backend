# Gosby Backend

The goal of this exercise is to create a restful API in Python.

## Task

- Return all currency rates
- Return a currency rate by currency code
- Return all transactions giving a currency code
- Return all transactions by sku and currency code

## TO START

cd gosby_backend

### INSTALL VIRTUAL ENVIROMENT

sudo pip3 install virtualenv
virtualenv --version

### CREATE ENVIROMENT

virtualenv gosby_backend
cd gosby_backend

### ACTIVATE ENVIROMENT

source bin/activate

### INSTALL LIB's

pip3 install Flask && pip3 install flask-requests

### SET THE FLASK_APP

appexport FLASK_APP=app.py

### RUN

flask run

### RUN on DEV MODE

flask --app app.py --debug run
