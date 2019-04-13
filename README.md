# fastapi with celery

> Minimal example utilizing fastapi and celery with RabbitMQ for task queue, Redis for celery backend and flower for monitoring the celery tasks.

## Requirements

- Python >= 3.6.x
  - pipenv (```pip install pipenv```)
- Docker
  - docker-compose

## Running

### Install project dependencies

Execute the following command:

```shell
pipenv --python <your_python_version>
pipenv install --dev
```

### Run example

1. Run command ```docker-compose up```to start up the RabbitMQ, Redis and flower instances.
2. Start the fastapi web application with ```pipenv run uvicorn main:app --reload```.
3. Start the celery worker with command ```pipenv run celery worker -A worker.celery_worker -l info -Q test-queue -c 1```

Navigate to the [http://localhost:8000/docs](http://localhost:8000/docs) and execute test API call. You can monitor the execution of the celery tasks in the console logs or navigate to the flower monitoring app at [http://localhost:5555](http://localhost:5555) (username: user, password: test).