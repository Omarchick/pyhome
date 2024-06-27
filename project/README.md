# Django Project

Этот проект использует Django и PostgreSQL для управления сущностями. 

## Установка

1. Установите зависимости:
    ```bash
    pip install django psycopg2-binary
    ```

2. Настройте базу данных в файле `project/settings.py`.

3. Примените миграции:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

4. Запустите сервер:
    ```bash
    python manage.py runserver
    ```

## Функционал

- Регистрация и авторизация пользователей
- Управление сущностями (создание, редактирование, просмотр, удаление)
- Страница с аналитикой

## Структура проекта

- `app/`: Основное приложение
  - `models.py`: Определение моделей
  - `forms.py`: Определение форм
  - `views.py`: Определение представлений
  - `templates/app/`: Шаблоны приложения
- `project/`: Основной проект
  - `settings.py`: Настройки проекта
  - `urls.py`: Маршрутизация URL
- `templates/registration/`: Шаблоны для регистрации и авторизации
