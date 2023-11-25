# Hospital Project

## Установка

1. Склонируйте репозиторий:

    ```bash
    git clone https://github.com/tebirenn/hospital.git
    ```

2. Создайте виртуальное окружение:

    ```bash
    python -m venv venv
    ```

3. Активируйте виртуальное окружение:

    - Для Windows:

        ```bash
        venv\Scripts\activate
        ```

    - Для macOS и Linux:

        ```bash
        source venv/bin/activate
        ```

4. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

5. Примените миграции:

    ```bash
    python manage.py migrate
    ```

6. Запустите сервер:

    ```bash
    python manage.py runserver
    ```

Приложение будет доступно по адресу http://localhost:8000/

## Использование

- Добавьте свои приложения и начните разрабатывать.
- API доступно по пути `/api/`.

## Структура проекта

- `myproject/` - основной каталог проекта.
  - `myapp/` - пример приложения.
  - `venv/` - виртуальное окружение.
  - `manage.py` - скрипт для управления проектом.
  - `requirements.txt` - список зависимостей проекта.
  - `.gitignore` - файл с правилами для игнорирования файлов системой контроля версий.

## Дополнительные ресурсы

- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework Documentation](https://www.django-rest-framework.org/)

## Лицензия

Этот проект лицензирован под [Лицензией MIT](LICENSE).
