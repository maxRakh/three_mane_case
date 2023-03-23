# Древовидное меню
Django-app, который позволяет вносить в БД меню (одно или несколько) через админку, и нарисовать на любой нужной странице меню по названию.

При выполнении задания из библиотек использованы только Django и стандартная библиотека Python.



### Установка и запуск:

1. Создайте виртуальное окружение и активируйте его

`virtualenv venv`

`source venv/bin/activate`

2. Установите зависимости

`pip install -r requirements.txt`

3. Создайте и проведите миграции

`python manage.py makemigrations`

`python manage.py migrate`

4. Создайте суперюзера

`python manage.py createsuperuser`

5. Запустите сервер

`python manage.py runserver`

6. Перейдите по ссылке 

http://127.0.0.1:8000/menu
