.DEFAULT_GOAL = help

run:
	docker-compose up --build
detach-run:
	docker-compose up -d --build
stop:
	docker-compose down
help:
	@echo "=============="
	@echo "===Commands==="
	@echo "=============="
	@echo "run"
	@echo "    Run the server and the client. The client will make a post request after 10s."
	@echo "detach-run"
	@echo "    Run the server and the client in detached mode. The client will make a post request after 10s."
	@echo "stop"
	@echo "    Stop the containers"
