import os
from kafka import KafkaConsumer
from pymongo import MongoClient
import json
import logging
import threading

LOGGER = logging.getLogger("projeto-finance")

KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS")
MONGODB_HOST = os.getenv("MONGODB_HOST")
CLIENT_MONGO = MongoClient(f"mongodb://{MONGODB_HOST}:27017/")


CONSUMER_NEWS = KafkaConsumer(
    "news-topic",
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="news-consumers",
)

CONSUMER_IBOV = KafkaConsumer(
    "ibov-topic",
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="ibov-consumers",
)


def run_news():
    db = CLIENT_MONGO["projeto-finance"]
    collection = db["news"]

    for message in CONSUMER_NEWS:
        content = message.value.decode("utf-8")
        dict_content = json.loads(content)

        # Check if the id is already in the collection
        if not collection.find_one({"id": dict_content["id"]}):
            collection.insert_one(dict_content)
            LOGGER.info(f"Salvo News no MongoDB: {dict_content}")
        else:
            LOGGER.info(f"ID {dict_content['id']} já existe no MongoDB")


def run_ibov():
    db = CLIENT_MONGO["projeto-finance"]
    collection = db["ibov"]

    for message in CONSUMER_IBOV:
        content = message.value.decode("utf-8")
        dict_content = json.loads(content)

        if not collection.find_one({"date": dict_content["date"]}):
            collection.insert_one(dict_content)
            LOGGER.info(f"Salvo Ibov no MongoDB: {dict_content}")
        else:
            LOGGER.info(f"Date {dict_content['date']} já existe no MongoDB")


def start():
    LOGGER.info("Iniciando consumer")

    # Cria threads para rodar os consumidores em paralelo
    news_thread = threading.Thread(target=run_news)
    ibov_thread = threading.Thread(target=run_ibov)

    # Inicia as threads
    news_thread.start()
    ibov_thread.start()

    # Aguarda as threads terminarem (teoricamente elas nunca terminam)
    news_thread.join()
    ibov_thread.join()
