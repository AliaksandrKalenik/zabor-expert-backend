release: python manage.py migrate; python manage.py collectstatic --no-post-process --noinput
web: gunicorn zabor_expert.wsgi --log-file -
worker: celery worker -A zabor_expert --loglevel=INFO
