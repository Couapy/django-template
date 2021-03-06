import os

from project.settings.base.constants import BASE_DIR

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'var/db.sqlite3'),
    }
}
