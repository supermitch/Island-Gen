ROOT_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
VENV = venv/bin
ACTIVATE = . venv/bin/activate;

run:
	$(ROOT_DIR)/$(VENV)/python main.py

game:
	@python main.py -p # Pygame doesn't live in our virtualenv

test:
	$(ROOT_DIR)/$(VENV)/nosetests --verbose --detailed-errors --with-coverage --cover-tests

