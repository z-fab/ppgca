from pydantic import BaseModel


class News(BaseModel):
    _id: str
    id: str
    title: str
    link: str
    sentiment: str
    sentiment_score: float
    scrapped_at: str
