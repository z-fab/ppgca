from pydantic import BaseModel


class News(BaseModel):
    title: str
    link: str
    category: str
