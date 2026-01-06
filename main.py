from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI(
    title="Task Manager API",
    description="Учебное приложение для курса по FastAPI",
    version="1.0.0"
)


@app.get("/")
async def root():
    return FileResponse("index.html")