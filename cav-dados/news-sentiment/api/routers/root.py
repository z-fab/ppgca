from fastapi import APIRouter
from typing import List
from api.models.news import News
from api.controllers import data_controller

router = APIRouter()


@router.get("/", response_model=List[News])
async def read_all_news():
    return data_controller.get_all_news()
