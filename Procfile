release: python manage.py migrate
web: python manage.py migrate && gunicorn 'emailVerify.wsgi'