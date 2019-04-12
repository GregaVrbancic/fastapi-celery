from fastapi import FastAPI

from worker.celery_app import celery_app

app = FastAPI()


def on_message(body):
    print(body)


@app.get("/{word}")
async def root(word: str):
    task = celery_app.send_task(
        "worker.celery_worker.test_celery", args=[word])
    print(task)
    print(task.get(on_message=on_message, propagate=False))
    return {"message": "Word received"}
