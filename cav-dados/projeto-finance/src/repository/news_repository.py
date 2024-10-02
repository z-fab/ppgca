from datetime import datetime
import requests
from bs4 import BeautifulSoup
import hashlib


def generate_id(title):
    return hashlib.sha256(title.encode("utf-8")).hexdigest()[:16]


def fetch_news_valor():
    url = "https://valor.globo.com"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")

        news_list = []

        highlight_content = soup.find_all("div", class_="highlight__content")
        for content in highlight_content:
            content_dict = {}
            content_title = content.find("h2", class_="highlight__title").find("a")

            title = content_title.get_text().strip()

            content_dict["id"] = generate_id(title)
            content_dict["title"] = title
            content_dict["link"] = content_title["href"]
            content_dict["sentiment"] = ""
            content_dict["sentiment_score"] = 0
            content_dict["scrapped_at"] = datetime.now().isoformat(sep="T")

            news_list.append(content_dict)

        highlight_links = soup.find_all("div", class_="highlight__links")
        for content in highlight_links:
            list_link = content.find("ul").find_all("a")
            for link in list_link:
                content_dict = {}

                title = link.get_text().strip()
                content_dict["id"] = generate_id(title)
                content_dict["title"] = title
                content_dict["link"] = link["href"]
                content_dict["sentiment"] = ""
                content_dict["sentiment_score"] = 0
                content_dict["scrapped_at"] = datetime.now().isoformat(sep="T")
                news_list.append(content_dict)

        return news_list
    else:
        print("Falha ao acessar o site")
        return []


def fetch_news_cnn():
    url = "https://www.cnnbrasil.com.br/economia/"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")

        news_list = []

        news_title = soup.find_all(
            ["h3", "h2"], class_=["block__news__title", "news-item-header__title"]
        )
        for title in news_title:
            content_dict = {}
            link = title.find_parent("a")
            if link:
                title = title.get_text().strip()
                content_dict["id"] = generate_id(title)
                content_dict["title"] = title
                content_dict["link"] = link["href"]
                content_dict["sentiment"] = ""
                content_dict["sentiment_score"] = 0
                content_dict["scrapped_at"] = datetime.now().isoformat(sep="T")

                news_list.append(content_dict)

        return news_list
    else:
        print("Falha ao acessar o site")
        return []


def get_all_news():
    news = fetch_news_cnn()
    news += fetch_news_valor()

    return news
