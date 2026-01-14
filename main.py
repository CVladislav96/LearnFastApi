from fastapi import FastAPI
from routers.task import router as task_router


app = FastAPI(
    title="Task Manager API",
    description="Учебное приложение для курса по FastAPI",
    version="1.0.0"
)

app.include_router(task_router)
