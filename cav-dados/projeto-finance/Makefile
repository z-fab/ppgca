# Caminho para a pasta docker
DOCKER_DIR = docker

.PHONY: build up down logs

build:
	docker-compose -f $(DOCKER_DIR)/compose.yml build

up:
	docker-compose -f $(DOCKER_DIR)/compose.yml up -d

down:
	docker-compose -f $(DOCKER_DIR)/compose.yml down

pause:
	docker-compose -f $(DOCKER_DIR)/compose.yml pause

destroy:
	docker-compose -f $(DOCKER_DIR)/compose.yml down -v
	
logs:
	docker-compose -f $(DOCKER_DIR)/compose.yml logs -f