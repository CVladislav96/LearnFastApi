    from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI(
    title="Task Manager API",
    description="Учебное приложение для курса по FastAPI",
    version="1.0.0"
)


fake_tasks_db = [
    {"task_id": 1, "task_name": "Изучить Python"},
    {"task_id": 2, "task_name": "Подключить Базу Данных"},
    {"task_id": 3, "task_name": "Выучить FastAPI"},
]


@app.get("/")
async def root():
    return FileResponse("index.html")

@app.get("/tasks/{task_id}")
async def get_task(task_id: int):
    for task in fake_tasks_db:
        if task["task_id"] == task_id:
            return task
    return {}

@app.get("/hello/{name}")
async def hello_user(name: str):
         return {"message": f"Hello, {name}!"}


@app.get("/product/{product_id}")
async def search_product(product_id: int):
    return {"product_id": product_id}

@app.get("/flights/{from_code}/{to_code}")
async def direct(from_code: int, to_code: int):
    return {"from": from_code, "to": to_code}

