INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

PROJECT_APPS = [
]

EXTRA_APPS = [
    'ninja',
]

INSTALLED_APPS += PROJECT_APPS
INSTALLED_APPS += EXTRA_APPS

LOCAL_MIGRATIONS = [app_path.split('.')[1] for app_path in PROJECT_APPS]
MIGRATION_MODULES = {app_name: f'migrations.{app_name}' for app_name in LOCAL_MIGRATIONS}
