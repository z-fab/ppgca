import os
from typing import List
from fastapi import APIRouter, HTTPException
from models.ibov import Ibov
from pymongo import MongoClient
import logging

router = APIRouter(prefix="/ibov", tags=["ibov"])

MONGODB_URI = os.getenv("MONGODB_HOST")
client = MongoClient(f"mongodb://{MONGODB_URI}:27017/")
db = client["projeto-finance"]
collection = db["ibov"]

LOGGER = logging.getLogger("projeto-finance")


@router.get("/", response_model=List[Ibov])
def get_all_ibov():
    try:
        ibov_list = []
        for ibov in collection.find():
            ibov_list.append(
                Ibov(_id=str(ibov["_id"]), date=str(ibov["date"]), close=ibov["close"])
            )
        return ibov_list
    except Exception as e:
        LOGGER.error(f"Erro ao obter Ibov: {e}")
        raise HTTPException(status_code=500, detail="Erro interno do servidor")
