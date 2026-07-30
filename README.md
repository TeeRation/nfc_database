# NFC Database

Учебный проект по разработке базы данных и REST API для учета NFC-меток, сотрудников, устройств, локаций и задач.

---

## Используемые технологии

- Python 3.14+
- FastAPI
- SQLAlchemy
- Alembic
- PostgreSQL
- Pydantic

---

## Структура проекта

```
app/                # FastAPI приложение
migrations/         # миграции Alembic
schema/             # SQL-скрипты создания таблиц
seed/               # тестовые данные
queries/            # примеры SQL-запросов
data/csv/           # исходные CSV-данные
docs/uml/           # UML-диаграммы
```

---

## Создание виртуального окружения

```powershell
python -m venv venv
```

Активация:

```powershell
venv\Scripts\activate
```

---

## Установка зависимостей

```powershell
python -m pip install -r requirements.txt
```

---

## Настройка переменных окружения

Создать файл `.env` в корне проекта.

Пример:

```env
DATABASE_URL=postgresql+psycopg2://nfc_user:nfc_password@localhost:5432/nfc_database
```

---

## Применение миграций

```powershell
python -m alembic upgrade head
```

---

## Заполнение тестовыми данными

```powershell
python -m app.seed
```

---

## Запуск приложения

```powershell
python -m uvicorn app.main:app --reload
```

---

## Swagger UI

После запуска API документация доступна по адресу:

```
http://127.0.0.1:8000/docs
```

---

## Проверка работы

Главная страница:

```
GET /
```

Проверка состояния сервиса:

```
GET /health
```

---

## Особенности проекта

- UUID используются в качестве первичных ключей.
- Управление структурой базы выполняется через Alembic.
- Строка подключения хранится в `.env`.
- PostgreSQL используется как основная СУБД.