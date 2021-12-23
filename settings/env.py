from os import getenv


SECRET_KEY = getenv('SECRET_KEY', 'secret')
DEBUG = getenv('DEBUG', 'True') == 'True'
