.PHONY: all

all: black lint clean

lint:
	pylint models.py main.py routes.py

black:
	black .

# setup:
# 	source /home/sot_server/sot_venv/bin/activate
