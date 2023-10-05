.PHONY: all

all: black lint

lint:
	pylint main.py server/models/* server/routes/*

black:
	black .

# setup:
# 	source /home/sot_server/sot_venv/bin/activate
