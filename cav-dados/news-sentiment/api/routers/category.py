from fastapi import APIRouter
from typing import List
from api.models.news import News
from api.controllers import data_controller

router = APIRouter()


@router.get("/{category}", response_model=List[News])
async def read_news_by_category(category: str):
    return data_controller.get_news_by_category(category)
