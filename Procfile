release: python collectstatic --no-post-process --noinput
release: python manage.py migrate
web: gunicorn zabor_expert.wsgi --log-file -
worker: celery worker -A zabor_expert --loglevel=INFO
