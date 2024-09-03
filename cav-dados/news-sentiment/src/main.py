import logging
from controllers import scrapping

logger = logging.getLogger("news-sentiment")

if __name__ == "__main__":
    scrapping.start()
