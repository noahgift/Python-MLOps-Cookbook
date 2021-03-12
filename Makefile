install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=cli --cov=mlib --cov=utilscli test_mlib.py

format:
	black *.py

lint:
	pylint --disable=R,C,W1203 mlib cli utilscli

all: install lint test