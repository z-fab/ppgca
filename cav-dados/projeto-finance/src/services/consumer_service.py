import os
from elasticsearch import Elasticsearch
from kafka import KafkaConsumer

from pymongo import MongoClient
import json
import logging
import threading

LOGGER = logging.getLogger("projeto-finance")
KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS")

MONGODB_HOST = os.getenv("MONGODB_HOST")
CLIENT_MONGO = MongoClient(f"mongodb://{MONGODB_HOST}:27017/")

ELASTICSEARCH_HOST = os.getenv("ELASTICSEARCH_HOST")
ES = Elasticsearch([{"host": ELASTICSEARCH_HOST, "port": 9200, "scheme": "http"}])

CONSUMER_NEWS_MONGO = KafkaConsumer(
    "news-topic",
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="news-consumers-mongo",
)

CONSUMER_IBOV_MONGO = KafkaConsumer(
    "ibov-topic",
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="ibov-consumers-mongo",
)

CONSUMER_NEWS_ELASTIC = KafkaConsumer(
    "news-topic",
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="news-consumers-elastic",
)

CONSUMER_IBOV_ELASTIC = KafkaConsumer(
    "ibov-topic",
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="ibov-consumers-elastic",
)


def create_index_if_not_exists():
    if not ES.indices.exists(index="news_index"):
        ES.indices.create(
            index="news_index",
            body={
                "mappings": {
                    "properties": {
                        "scrapped_at": {
                            "type": "date",
                            "format": "strict_date_optional_time||epoch_millis",
                        }
                    }
                }
            },
        )

    if not ES.indices.exists(index="ibov_index"):
        ES.indices.create(
            index="ibov_index",
            body={
                "mappings": {
                    "properties": {
                        "date": {
                            "type": "date",
                            "format": "strict_date_optional_time||epoch_millis",
                        }
                    }
                }
            },
        )


def run_news_elasticsearch():
    try:
        create_index_if_not_exists()
        for message in CONSUMER_NEWS_ELASTIC:
            content = json.loads(message.value.decode("utf-8"))
            dict_content = {
                "title": content["title"],
                "link": content["link"],
                "sentiment": content["sentiment"],
                "sentiment_score": content["sentiment_score"],
                "scrapped_at": content["scrapped_at"],
            }

            if not ES.exists(index="news_index", id=content["id"]):
                ES.index(index="news_index", id=content["id"], body=dict_content)
            else:
                LOGGER.warning(f"ID {content['id']} já existe no Elasticsearch")

    except Exception as e:
        LOGGER.error(f"Erro ao enviar documento para o Elasticsearch: {e}")


def run_ibov_elasticsearch():
    try:
        create_index_if_not_exists
        for message in CONSUMER_IBOV_ELASTIC:
            content = json.loads(message.value.decode("utf-8"))
            dict_content = {"date": content["date"], "close": content["close"]}

            if not ES.exists(index="ibov_index", id=content["date"]):
                ES.index(index="ibov_index", id=content["date"], body=dict_content)
            else:
                LOGGER.warning(f"Date {content['date']} já existe no Elasticsearch")

    except Exception as e:
        LOGGER.error(f"Erro ao enviar documento para o Elasticsearch: {e}")


def run_news_mongo():
    db = CLIENT_MONGO["projeto-finance"]
    collection = db["news"]

    for message in CONSUMER_NEWS_MONGO:
        content = message.value.decode("utf-8")
        dict_content = json.loads(content)

        # Check if the id is already in the collection
        if not collection.find_one({"id": dict_content["id"]}):
            collection.insert_one(dict_content)
            LOGGER.info(f"Salvo News no MongoDB: {dict_content}")
        else:
            LOGGER.info(f"ID {dict_content['id']} já existe no MongoDB")


# def run_ibov_mongo():
#     db = CLIENT_MONGO["projeto-finance"]
#     collection = db["ibov"]

#     for message in CONSUMER_IBOV:
#         content = message.value.decode("utf-8")
#         dict_content = json.loads(content)

#         if not collection.find_one({"date": dict_content["date"]}):
#             collection.insert_one(dict_content)
#             LOGGER.info(f"Salvo Ibov no MongoDB: {dict_content}")
#         else:
#             LOGGER.info(f"Date {dict_content['date']} já existe no MongoDB")


def start():
    LOGGER.info("Iniciando consumer")

    # Cria threads para rodar os consumidores em paralelo
    news_mongo_thread = threading.Thread(target=run_news_mongo)
    news_elastic_thread = threading.Thread(target=run_news_elasticsearch)
    ibov_elastic_thread = threading.Thread(target=run_ibov_elasticsearch)
    # ibov_mongo_thread = threading.Thread(target=run_ibov_mongo)

    # Inicia as threads
    news_mongo_thread.start()
    news_elastic_thread.start()
    # ibov_mongo_thread.start()
    ibov_elastic_thread.start()

    news_mongo_thread.join()
    news_elastic_thread.join()
    # ibov_mongo_thread.join()
    ibov_elastic_thread.join()
