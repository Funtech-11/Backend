# О проекте

Проект является MVP Backend-приложения для IT мероприятий.

# О команде

- Денис - [@Denmais09](https://t.me/Denmais09)
- Александр - [@alexeont](https://t.me/alexeont)
- Георгий - [@Sivikgosh](https://t.me/SivikGosh)

# Ссылка на проект

[Ссылка на проект](http://84.252.73.12/)
[Ссылка на API](http://84.252.73.12/api/schema/redoc/)

# Стек технологий

<div> 
 <img src="https://img.shields.io/badge/Django-%23404d59.svg?style=for-the-badge&logo=django&logoColor=green" alt="Django Badge" />
 <img src="https://img.shields.io/badge/djangorestframework-%23404d59.svg?style=for-the-badge&logo=djangorestframework&logoColor=green" alt="Django Rest Framework Badge" />
 <img src="https://img.shields.io/badge/drf--spectacular-%23404d59.svg?style=for-the-badge&logo=drf&logoColor=green" alt="DRF Spectacular Badge" />
 <img src="https://img.shields.io/badge/django--cors--headers-%23404d59.svg?style=for-the-badge&logo=django&logoColor=green" alt="Django CORS Headers Badge" />
 <img src="https://img.shields.io/badge/psycopg2--binary-%23404d59.svg?style=for-the-badge&logo=postgresql&logoColor=green" alt="Psycopg2 Binary Badge" />
 <img src="https://img.shields.io/badge/asgiref-%23404d59.svg?style=for-the-badge&logo=python&logoColor=green" alt="Asgiref Badge" />
 <img src="https://img.shields.io/badge/gunicorn-%23404d59.svg?style=for-the-badge&logo=python&logoColor=green" alt="Gunicorn Badge" />
 <img src="https://img.shields.io/badge/requests-%23404d59.svg?style=for-the-badge&logo=requests&logoColor=green" alt="Requests Badge" />
 <img src="https://img.shields.io/badge/PyYAML-%23404d59.svg?style=for-the-badge&logo=python&logoColor=green" alt="PyYAML Badge" />
 <img src="https://img.shields.io/badge/pillow-%23404d59.svg?style=for-the-badge&logo=pillow&logoColor=green" alt="Pillow Badge" />
</div>

# Установка локально без Docker

Клонировать репозиторий:

```bash
git clone
```

Создать и активировать виртуальное окружение:

```bash
python3 -m venv venv
source venv/bin/activate
```

Установить библиотеки

```bash
cd funtech/
pip3 install -r requirements.txt
```

Запустить проект:

```bash
python manage.py migrate

python createsuperuser
- назначить логин
- добавить имя
- добавить фамилию
- установить пароль
- добавить email

python manage.py load_data

python manage.py runserver
```

Swagger будет доступен по адресам:
- http://localhost:8000/api/schema/redoc/
- http://localhost:8000/api/schema/swagger-ui/
