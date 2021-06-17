.DEFAULT_GOAL = help

run:
	python manage.py runserver
tests:
	python manage.py test
parallel-tests:
	python manage.py test --parallel
reverse-tests:
	python manage.py test --reverse
check-deploy:
	python manage.py check --deploy
coverage:
	coverage run manage.py test
	coverage report
black:
	black . -l 79 --color -S

isort:
	isort .  -m 3 --color
help:
	@echo "=============="
	@echo "===Commands==="
	@echo "=============="
	@echo "run"
	@echo "    Run the Django server"
	@echo "tests"
	@echo "    Run all the tests"
	@echo "parallel-tests"
	@echo "    Run tests in parallel"
	@echo "reverse-tests"
	@echo "    Run tests in reverse"
	@echo "check-deploy"
	@echo "    Deployment checklist"
	@echo "coverage"
	@echo "    Run coverage + report"
	@echo "black"
	@echo "    Apply black to the whole project"
	@echo "isort"
	@echo "    Apply isort to the whole project"
