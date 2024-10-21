from pydantic import BaseModel

class Film(BaseModel):
    id: int
    title: str
    description: str
    views: int