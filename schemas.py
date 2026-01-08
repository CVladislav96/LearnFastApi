from pydantic import BaseModel, Field

class STaskAdd(BaseModel):
    name: str = Field(
        ...,
        min_length=2,
        max_length=100,
        description="Название задачи"
    )

    description: str = Field(
        None,
        max_length=300
    )

    priority: int = Field(
        default=1,
        ge=1,
        le=5,
        description="Приоритет задачи от 1 (низкий) до 5 (высокий)"
    )



