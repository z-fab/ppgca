import argparse

from services import consumer_service as consumer_s
from services import producer_service as producer_s
from repository import ibovespa_repository as ibov
from dotenv import load_dotenv
import logging

load_dotenv()

logger = logging.getLogger("projeto-finance")
logging.basicConfig(level=logging.DEBUG)

formatter = logging.Formatter(
    "\n[%(levelname)s] %(asctime)s :: %(filename)s (%(funcName)s)\n%(message)s"
)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "action", choices=["consumer", "producer", "ibov"], help="Ação a ser executada"
    )

    args = parser.parse_args()

    if args.action == "consumer":
        consumer_s.start()
    elif args.action == "producer":
        producer_s.start()
    elif args.action == "ibov":
        ibov.get_ibovespa()


if __name__ == "__main__":
    main()
