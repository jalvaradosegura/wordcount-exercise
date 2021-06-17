.DEFAULT_GOAL = help

run:
	python3 wordcount_client.py -f document.txt
black:
	black . -l 79 --color -S

isort:
	isort .  -m 3 --color
help:
	@echo "=============="
	@echo "===Commands==="
	@echo "=============="
	@echo "run"
	@echo "    Run the client code."
	@echo "black"
	@echo "    Apply black to the whole project"
	@echo "isort"
	@echo "    Apply isort to the whole project"
