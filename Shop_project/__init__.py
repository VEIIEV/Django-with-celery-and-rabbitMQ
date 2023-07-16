from .celery import app as celery_app

# делается для того что бы модуль celery
# загружался при запуске Django
__all__ = ['celery_app']
