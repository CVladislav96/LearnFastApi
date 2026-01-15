from fastapi import APIRouter, HTTPException, status, Depends
from schemas.task import STask, STaskAdd
from database import SessionDep

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.post("", response_model=STask, status_code=status.HTTP_201_CREATED)
async def create_task(task: STaskAdd, session: SessionDep):
    return {"ok": True}

@router.get("", response_model=STask, status_code=status.HTTP_200_OK)
async def get_task(task_id: int, session: SessionDep):
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Task with id {task_id} not found'
    )

    return {"ok": True}



@router.delete("{task_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: int):
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks.pop(index)
            return

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Task with id {task_id} not found'
    )

