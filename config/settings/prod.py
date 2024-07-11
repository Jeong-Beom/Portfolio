from .base import *
from pathlib import Path

# Add for using .env info
import environ
import os

env = environ.Env(
    DEBUG=(bool, False)
)

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

ALLOWED_HOSTS = [os.environ.get('IP'), os.environ.get('DOMAIN')]
STATIC_ROOT = BASE_DIR / 'static/'
STATICFILES_DIRS = []
DEBUG = env('DEBUG', default=False)