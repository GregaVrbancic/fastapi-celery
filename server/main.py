from fastapi import FastAPI

from worker.celery_app import celery_app

app = FastAPI()


@app.get("/{word}")
async def root(word: str):
    task = celery_app.send_task("worker.celery_worker.test_celery", args=[word])
    print(task)
    return {"message": "Word received"}
