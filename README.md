# Funtech Backend

##### Проект является MVP Backend-приложения для IT мероприятий.

## Команда

```Денис``` [@Denmais09](https://t.me/Denmais09)

```Александр``` [@alexeont](https://t.me/alexeont)

```Георгий``` [@SivikGosh](https://t.me/SivikGosh)

## Ссылки на проект

```Frontend``` [Яндекс.Ивенты](http://84.252.73.12/)

```API``` [Swagger UI](http://84.252.73.12/api/schema/swagger-ui/), [Redoc](http://84.252.73.12/api/schema/redoc/)

## Стек технологий

 <img src="https://img.shields.io/badge/python-%233776AB.svg?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge" />
<img src="https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white" alt="Django Badge" />
<img src="https://img.shields.io/badge/gunicorn-%23499848.svg?style=for-the-badge&logo=gunicorn&logoColor=white" alt="Gunicorn Badge" />

## Установка

#### Клонировать репозиторий

```bash
$ git clone git@github.com:Funtech-11/Backend.git
```

#### Создать и активировать виртуальное окружение

###### Windows
```bash
$ python -m venv venv
$ source venv/Scripts/activate
```
###### Linux
```bash
$ python3 -m venv venv
$ source venv/bin/activate
```

#### Установить библиотеки

###### Windows
```bash
(venv) $ cd funtech/
(venv) $ pip-sync requirements.txt
```
###### Linux
```bash
(venv) $ cd funtech/
(venv) $ pip-sync -r requirements.txt
```

#### Запустить проект:

###### Windows
```bash
(venv) $ python manage.py migrate

(venv) $ python manage.py createsuperuser
         Email:
         Username:
         Имя:
         Фамилия:
         Password:
         Password (again):

(venv) $ python manage.py load_data
(venv) $ python manage.py runserver
```
###### Linux
```bash
(venv) $ python3 manage.py migrate

(venv) $ python3 manage.py createsuperuser
         Email:
         Username:
         Имя:
         Фамилия:
         Password:
         Password (again):

(venv) $ python3 manage.py load_data
(venv) $ python3 manage.py runserver
```

##### API будет доступно по адресам:

```Redoc``` http://localhost:8000/api/schema/redoc/

```Swagger UI``` http://localhost:8000/api/schema/swagger-ui/
