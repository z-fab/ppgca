# Caminho para a pasta docker
DOCKER_DIR = docker
DOCKER_FILE = $(DOCKER_DIR)/compose.dev.yml

.PHONY: build up down logs

build:
	docker-compose -f $(DOCKER_FILE) build

up:
	docker-compose -f $(DOCKER_FILE) up -d

down:
	docker-compose -f $(DOCKER_FILE) down

pause:
	docker-compose -f $(DOCKER_FILE) pause

destroy:
	docker-compose -f $(DOCKER_FILE) down -v
	
logs:
	docker-compose -f $(DOCKER_FILE) logs -f