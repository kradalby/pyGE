ENV=./env/bin
SHELL := /bin/bash
PYTHON=$(ENV)/python
PIP=$(ENV)/pip
SETUP=$(PYTHON) setup.py

dev: 
	$(PIP) install -r requirements/development.txt --upgrade

env:
	virtualenv -p `which python3` env

clean:
	pyclean .
	find . -name "*.pyc" -exec rm -rf {} \;
	rm -rf *.egg-info

flake8:
	flake8

lint: flake8

test:
	$(SETUP) test

#run:
#	$(MANAGE) runserver 0.0.0.0:8000

freeze:
	mkdir -p requirements
	$(PIP) freeze > requirements/base.txt
