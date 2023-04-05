# API_YaMDb
ip - 158.160.5.229

Проект YaMDb собирает отзывы пользователей на произведения. Произведения делятся на категории: «Книги», «Фильмы», «Музыка».
Произведению может быть присвоен жанр.
Читатели оставляют к произведениям отзывы и выставляют рейтинг (от 1 до 10).
Cредняя оценка произведения высчитывается автоматически.

Аутентификация по JWT-токену

Поддерживает методы GET, POST, PUT, PATCH, DELETE

![example workflow](https://github.com/UserVeryFriendly/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

## Стек технологий
- Django 2.2.16

- Python 3.10.4

- Django REST Framework 3.12.4

- Simple-JWT 4.8.0

- PostgreSQL 13.0-alpine

- Nginx 1.21.3-alpine

- Gunicorn 20.0.4

- Docker 20.10.17, build 100c701

- Docker-compose 3.8

## Как запустить проект:

* Клонируйте репозитроий с проектом
* В директории infra создайте файл .env с переменными окружения для работы с базой данных:

<code>DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql</code>

<code>DB_NAME=postgres # имя базы данных</code>

<code>POSTGRES_USER=postgres # логин для подключения к базе данных</code>

<code>POSTGRES_PASSWORD=postgres # пароль для подключения к БД (установите свой)</code>

<code>DB_HOST=db # название сервиса (контейнера)</code>

<code>DB_PORT=5432 # порт для подключения к БД</code>

* Из папки infra/ разверните контейнеры в новой структуре:

* Для запуска необходимо выполнить из директории с проектом команду:

<code>sudo docker-compose up -d</code>

### Для пересборки команда up выполняется с параметром --build

<code>sudo docker-compose up -d --build</code>

* Теперь в контейнере web нужно выполнить миграции:

<code>sudo docker-compose exec web python manage.py migrate</code>

* Создать суперпользователя:

<code>sudo docker-compose exec web python manage.py createsuperuser</code>

* Собрать статику:

<code>sudo docker-compose exec web python manage.py collectstatic --no-input</code>

* Вы также можете создать дамп (резервную копию) базы:

<code>sudo docker-compose exec web python manage.py dumpdata > fixtures.json</code>

* или, разместив, например, файл fixtures.json в папке с Dockerfile, загрузить в базу данные из дампа:

<code>sudo docker-compose exec web python manage.py loaddata fixtures.json</code>
__________________________________

Ваш проект запустился на http://localhost/

Полная документация доступна по адресу http://localhost/redoc/

Автор проекта:
- Молотков Иван
