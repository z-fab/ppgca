import csv
from datetime import datetime
import requests
from bs4 import BeautifulSoup

def fetch_news_valor():
    
    url = "https://valor.globo.com"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        news_list = []
        
        highlight_content = soup.find_all('div', class_='highlight__content')
        for content in highlight_content:
            content_dict = {}
            content_title = content.find('h2', class_='highlight__title').find('a')

            content_dict['title'] = content_title.get_text().strip()
            content_dict['link'] = content_title['href']
            content_dict['scrapped_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            news_list.append(content_dict)

        
        highlight_links = soup.find_all('div', class_='highlight__links')
        for content in highlight_links:
            list_link = content.find('ul').find_all('a')
            for link in list_link:
                print
                content_dict = {}
                content_dict['title'] = link.get_text().strip()
                content_dict['link'] = link['href']
                content_dict['scrapped_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                news_list.append(content_dict)

        return news_list
    else:
        print("Falha ao acessar o site")
        return []

def fetch_news_cnn():
    url = "https://www.cnnbrasil.com.br/economia/"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        news_list = []
        
        highlight_content = soup.find_all('div', class_='highlight__content')
        for content in highlight_content:
            content_dict = {}
            content_title = content.find('h2', class_='highlight__title').find('a')

            content_dict['title'] = content_title.get_text().strip()
            content_dict['link'] = content_title['href']
            content_dict['scrapped_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            news_list.append(content_dict)


        return news_list
    else:
        print("Falha ao acessar o site")
        return []

def save_csv(lista, filename):
    headers = list(lista[0].keys())

    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers, delimiter='|')
            
            writer.writeheader()
            
            for row in lista:
                writer.writerow(row)
        
        print(f"Arquivo '{filename}' criado com sucesso.")
    except IOError as e:
        print(f"Erro ao criar o arquivo: {e}")

# Exemplo de chamada da função
if __name__ == "__main__":
    fetch_news_cnn()
    news = fetch_news_valor()
    save_csv(news, 'news.csv')
    
