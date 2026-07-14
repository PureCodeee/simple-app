# Simple App

REST API приложение на **FastAPI**, разработанное в рамках тестового задания.

* REST API на FastAPI;
* Docker и Docker Compose;
* GitHub Actions (CI);
* автоматическое тестирование с pytest;
* статический анализ кода с Ruff;
* Bash-скрипт для диагностики сервера.

---

# Требования

* Python 3.12+
* Docker
* Docker Compose
* Ansible

---

# Быстрый старт

## Локальный запуск

```bash
git clone <repository-url>
cd simple-app

cd app
uv sync

uv run uvicorn app.main:app --host 0.0.0.0 --port 5000
```

Приложение будет доступно по адресу:

```
http://localhost:5000
```

Swagger UI:

```
http://localhost:5000/docs
```

---

## Запуск через Docker

Сборка образа:

```bash
docker build -t simple-app:latest .
```

Запуск контейнера:

```bash
docker run -p 5000:5000 simple-app:latest
```

---

## Запуск через Docker Compose

```bash
docker compose up --build
```

или

```bash
docker compose up -d --build
```

---

# API

## GET /

Возвращает приветственное сообщение.

```bash
curl http://localhost:5000/
```

Ответ:

```json
{
  "message": "Hello, World!"
}
```

---

## GET /health

Проверка состояния приложения.

```bash
curl http://localhost:5000/health
```

Ответ:

```json
{
  "status": "ok"
}
```

---

## GET /api/users

Получить список пользователей.

```bash
curl http://localhost:5000/api/users/
```

---

## POST /api/users

Создать пользователя.

```bash
curl -X POST \
-H "Content-Type: application/json" \
-d '{"name":"John"}' \
http://localhost:5000/api/users/
```

---

## GET /api/users/{id}

Получить пользователя по идентификатору.

```bash
curl http://localhost:5000/api/users/1
```

---

## DELETE /api/users/{id}

Удалить пользователя.

```bash
curl -X DELETE http://localhost:5000/api/users/1
```

---

# Bash-скрипт

Скрипт `scripts/server-info.sh` предназначен для диагностики сервера.

Возможности:

* вывод информации о системе;
* отображение использования CPU, RAM и дискового пространства;
* вывод списка Docker-контейнеров;
* проверка HTTP endpoint'ов;
* запись результатов в лог-файл.

## Пример использования

Только информация о системе:

```bash
./scripts/server-info.sh
```

Проверка приложения:

```bash
./scripts/server-info.sh http://localhost:5000/health
```

Справка:

```bash
./scripts/server-info.sh --help
```

---

# Тестирование

Запуск всех тестов:

```bash
uv run python -m pytest
```

или

```bash
pytest app/tests -v
```

---

# Проверка качества кода

```bash
uv run ruff check .
```

---

# GitHub Actions

При каждом `push` и `pull request` автоматически выполняются:

* установка зависимостей;
* проверка Ruff;
* запуск тестов.

---

# Ansible

Развертывание выполняется командой:

```bash
ansible-playbook -i ansible/inventory.ini ansible/playbook.yml
```

---

# Структура проекта

```
.
├── app
│   ├── main.py
│   ├── models.py
│   ├── routes.py
│   └── tests
├── scripts
│   └── server-info.sh
├── .github
│   └── workflows
│       └── ci.yml
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
├── requirements.txt
└── README.md
```

---

# Troubleshooting

### Приложение недоступно

Проверьте, что порт 5000 свободен.

```bash
docker ps
```

---

### Docker не запускается

Убедитесь, что Docker Desktop запущен.

---

### Не проходят тесты

Установите зависимости:

```bash
uv sync
```

После этого повторно выполните:

```bash
uv run python -m pytest
```

---

# Используемые технологии

* Python
* FastAPI
* Uvicorn
* Pydantic
* Pytest
* Ruff
* Docker
* Docker Compose
* GitHub Actions
* Bash
