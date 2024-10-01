import os

from kafka import KafkaProducer
from repository import news_repository, ibovespa_repository
from predict import sentiment_predict
import json

from apscheduler.schedulers.blocking import BlockingScheduler
import logging

LOGGER = logging.getLogger("projeto-finance")
KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS")
SCHEDULER = BlockingScheduler()

PRODUCER = KafkaProducer(
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)


def run_news():
    news_list = news_repository.get_all_news()
    news_list = sentiment_predict.predict_sentiment(news_list)

    for news in news_list:
        PRODUCER.send("news-topic", news)
        LOGGER.info(f"Enviado News para o Kafka: {news}")


def run_ibov():
    ibov_list = ibovespa_repository.get_ibovespa()

    for ibov in ibov_list:
        PRODUCER.send("ibov-topic", ibov)
        LOGGER.info(f"Enviado Ibov para o Kafka: {ibov}")


def start():
    LOGGER.info("Iniciando producer")
    SCHEDULER.add_job(run_news, "interval", seconds=10)
    SCHEDULER.add_job(run_ibov, "interval", seconds=10)
    SCHEDULER.start()
