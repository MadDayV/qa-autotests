from pydantic import BaseModel, ConfigDict, Field


class Post(BaseModel):
    model_config = ConfigDict(extra="forbid")

    user_id: int = Field(alias="userId")
    id: int
    title: str
    body: str
