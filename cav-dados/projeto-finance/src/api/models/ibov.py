from pydantic import BaseModel


class Ibov(BaseModel):
    _id: str
    date: str
    close: float
