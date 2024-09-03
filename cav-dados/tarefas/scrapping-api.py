import requests
from bs4 import BeautifulSoup


def scrapping_wikipedia():
    url = "https://pt.wikipedia.org/wiki/Machado_de_Assis"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    print(soup)


if __name__ == "__main__":
    scrapping_wikipedia()
