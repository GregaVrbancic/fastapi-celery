from time import sleep
from .celery_app import celery_app


@celery_app.task(acks_late=True)
def test_celery(word: str):
    sleep(10)
    return f"test task return {word}"
