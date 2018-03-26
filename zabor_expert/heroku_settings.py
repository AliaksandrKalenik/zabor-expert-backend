from zabor_expert.settings import *


import django_heroku
django_heroku.settings(locals())
BROKER_URL = os.environ.get('REDIS_URL', 'amqp://guest:guest@localhost//')
