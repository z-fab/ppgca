import os
from typing import List
from fastapi import APIRouter, HTTPException
from models.news import News
from pymongo import MongoClient
import logging

router = APIRouter(prefix="/news", tags=["news"])

MONGODB_URI = os.getenv("MONGODB_HOST")
client = MongoClient(f"mongodb://{MONGODB_URI}:27017/")
db = client["projeto-finance"]
collection = db["news"]

LOGGER = logging.getLogger("projeto-finance")


@router.get("/", response_model=List[News])
def get_all_news():
    try:
        news_list = []
        for news in collection.find():
            news_list.append(
                News(
                    _id=str(news["_id"]),
                    id=str(news["_id"]),
                    title=news["title"],
                    link=news["link"],
                    sentiment=news["sentiment"],
                    sentiment_score=news["sentiment_score"],
                    scrapped_at=news["scrapped_at"],
                )
            )
        return news_list
    except Exception as e:
        LOGGER.error(f"Erro ao obter notícias: {e}")
        raise HTTPException(status_code=500, detail="Erro interno do servidor")
