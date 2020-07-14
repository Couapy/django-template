import os

from .constants import PROJECT_DIR

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_DIR, 'var/db.sqlite3'),
    }
}
