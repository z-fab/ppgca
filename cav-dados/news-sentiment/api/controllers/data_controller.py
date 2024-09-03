from pathlib import Path
import polars as pl
from api.models.news import News

data_dir = Path(__file__).parent.parent.parent / "data"


def load_csv():
    return pl.read_csv(data_dir / "news.csv")


def get_all_news():
    df = load_csv()
    list_news = []
    for row in df.iter_rows():
        register = News(
            title=row[0],
            link=row[2],
            category=row[1],
        )
        list_news.append(register)

    return list_news


def get_news_by_category(category):
    df = load_csv()
    list_news = []
    for row in df.filter(pl.col("category") == category).iter_rows():
        register = News(
            title=row[0],
            link=row[2],
            category=row[1],
        )
        list_news.append(register)

    return list_news
