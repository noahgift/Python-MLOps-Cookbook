install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=cli --cov=mlib test_mlib.py

format:
	black *.py

lint:
	pylint --disable=R,C,W1203 mlib cli

all: install lint test