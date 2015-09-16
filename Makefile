ROOT_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
ACTIVATE = . venv/bin/activate;

run:
	$(ACTIVATE) python gen.py

game:
	@python gen.py -p # Pygame doesn't live in our virtualenv

test:
	$(ACTIVATE) nosetests --verbose --detailed-errors --with-coverage --cover-tests

