from fastapi import FastAPI
from schemas import STaskAdd

app = FastAPI(
    title="Task Manager API",
    description="Учебное приложение для курса по FastAPI",
    version="1.0.0"
)

tasks = []



@app.post("/tasks")
async def add_task(task: STaskAdd):
    tasks.append(task.model_dump())
    return {"ok": True, "message": "Задача добавлена"}












