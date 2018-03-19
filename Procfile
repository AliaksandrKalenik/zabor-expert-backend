release: python manage.py migrate
web: gunicorn django_base.wsgi --log-file -
worker: celery worker -A django_base --loglevel=INFO
