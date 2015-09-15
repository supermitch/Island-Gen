ROOT_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
VENV:=venv/bin

run:
	@python gen.py  # Pygame doesn't live in our virtualenv

test:
	$(ROOT_DIR)/$(VENV)/nosetests --verbose --detailed-errors --with-coverage --cover-tests

