.PHONY: all

all: black lint clean

lint:
	pylint *.py

black:
	black .

# setup:
# 	source /home/sot_server/sot_venv/bin/activate
