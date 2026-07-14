.PHONY: help install lint test run server-info \
docker-build docker-run compose-up compose-down compose-logs \
ansible-check ansible-dry ansible-run

help:
	@echo "Available commands:"
	@echo "  install        Install dependencies"
	@echo "  lint           Run Ruff and ShellCheck"
	@echo "  test           Run tests"
	@echo "  run            Run FastAPI application"
	@echo "  server-info    Run server diagnostics"
	@echo "  docker-build   Build Docker image"
	@echo "  docker-run     Run Docker container"
	@echo "  compose-up     Start Docker Compose"
	@echo "  compose-down   Stop Docker Compose"
	@echo "  compose-logs   Show Docker Compose logs"
	@echo "  ansible-check  Validate Ansible playbook"
	@echo "  ansible-dry    Dry run Ansible"
	@echo "  ansible-run    Run Ansible playbook"

install:
	cd app && uv sync

lint:
	cd app && uv run ruff check .
	shellcheck scripts/server-info.sh

test:
	cd app && uv run python -m pytest

run:
	cd app && uv run uvicorn app.main:app --host 0.0.0.0 --port 5000

server-info:
	./scripts/server-info.sh

docker-build:
	docker build -t simple-app:latest .

docker-run:
	docker run -p 5000:5000 simple-app:latest

compose-up:
	docker compose up --build

compose-down:
	docker compose down

compose-logs:
	docker compose logs -f

ansible-check:
	ansible-playbook --syntax-check ansible/playbook.yml

ansible-dry:
	ansible-playbook -i ansible/inventory.ini ansible/playbook.yml --check

ansible-run:
	ansible-playbook -i ansible/inventory.ini ansible/playbook.yml