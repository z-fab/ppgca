import requests
from bs4 import BeautifulSoup
import polars as pl
from pathlib import Path


def scrapping_globocom():
    url = "https://www.globo.com/"
    response = requests.get(url)

    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    news_title = soup.select(".post__title")
    news_list = []
    for element in news_title:
        title = element.text.strip()

        parent_div_data = element.find_parent(
            "div", attrs={"data-tracking-action": True}
        )
        if not parent_div_data:
            parent_div_data = element.find_parent(
                "div", attrs={"data-traking-action": True}
            )

        category = (
            parent_div_data.get("data-tracking-action")
            or parent_div_data.get("data-traking-action", "sem_categoria")
            if parent_div_data
            else "sem_categoria"
        )

        link_parent = element.find_parent("a")
        link = link_parent["href"] if link_parent else ""

        news_list.append(
            {"title": title, "category": category.split("|")[0], "link": link}
        )

    return news_list


def save_news(news_list):
    data_dir = Path(__file__).parent.parent.parent / "data"

    df = pl.DataFrame(news_list)
    df.write_csv(data_dir / "news.csv")


def start():
    print("Starting scrapping...")
    news_list = scrapping_globocom()
    save_news(news_list)
