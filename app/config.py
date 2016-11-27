import os

class Config(object):
  CSRF_ENABLED = True
  DEBUG = os.environ.get('DEBUG', False)
  DB_HOST = os.environ['DB_HOST']
  DB_PORT = os.environ['DB_PORT']
