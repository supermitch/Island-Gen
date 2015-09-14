ROOT_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
VENV:=venv/bin/

run:
	python gen.py

test:
	$(ROOT_DIR)/$(VENV)/nosetests --verbose --detailed-errors --with-coverage --cover-inclusive --cover-tests

