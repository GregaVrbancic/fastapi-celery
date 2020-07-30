# FastAPI with Celery

> Minimal example utilizing FastAPI and Celery with RabbitMQ for task queue, Redis for Celery backend and flower for monitoring the Celery tasks.

## Requirements

- Docker
  - [docker-compose](https://docs.docker.com/compose/install/)

## Run example

1. Run command ```docker-compose up```to start up the RabbitMQ, Redis, flower and our application/worker instances.
2. Navigate to the [http://localhost:8000/docs](http://localhost:8000/docs) and execute test API call. You can monitor the execution of the celery tasks in the console logs or navigate to the flower monitoring app at [http://localhost:5555](http://localhost:5555) (username: user, password: test).

## Run application/worker without Docker?

### Requirements/dependencies

- Python >= 3.7
  - [poetry](https://python-poetry.org/docs/#installation)
- RabbitMQ instance
- Redis instance

> The RabbitMQ, Redis and flower services can be started with ```docker-compose -f docker-compose-services.yml up```

### Install dependencies

Execute the following command: ```poetry install --dev```

### Run FastAPI app and Celery worker app

1. Start the FastAPI web application with ```poetry run hypercorn app/main:app --reload```.
2. Start the celery worker with command ```poetry run celery worker -A app.worker.celery_worker -l info -Q test-queue -c 1```
3. Navigate to the [http://localhost:8000/docs](http://localhost:8000/docs) and execute test API call. You can monitor the execution of the celery tasks in the console logs or navigate to the flower monitoring app at [http://localhost:5555](http://localhost:5555) (username: user, password: test).