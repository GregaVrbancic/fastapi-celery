from celery import Celery

celery_app = Celery(
    "worker",
    backend="amqp://user:bitnami@localhost:5672//",
    broker="amqp://user:bitnami@localhost:5672//"
)

celery_app.conf.task_routes = {"worker.celery_worker.test_celery": "test-queue"}
