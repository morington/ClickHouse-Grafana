NETWORK_NAME = xcvzv97opkje

all: build

_create_network:
	@echo "Создание сети Docker, если она не существует..."
	docker network inspect $(NETWORK_NAME) >/dev/null 2>&1 || docker network create $(NETWORK_NAME)

build:
	make up
	make logs_clickhouse

restart:
	make down
	make

up:
	make _create_network
	@echo "Запуск..."
	docker compose up -d
	@echo "Успешно!"
	clear
	@echo "Выводим логи ClickHouse..."
	docker compose logs -f vector

down:
	@echo "Останавливаем..."
	docker compose down
	@echo "Успешно!"

test:
	docker compose up -d --force-recreate vector
	#docker exec -it vector cat /etc/vector/vector.toml
	docker compose logs -f vector

rtest:
	make down
	clear
	make test
