import csv
from datetime import datetime
import requests
from bs4 import BeautifulSoup
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import numpy as np
import hashlib


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

            title = content_title.get_text().strip()

            content_dict['id'] = generate_id(title)
            content_dict['title'] = title
            content_dict['link'] = content_title['href']
            content_dict['sentiment'] = ''
            content_dict['sentiment_score'] = 0
            content_dict['scrapped_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            news_list.append(content_dict)

        
        highlight_links = soup.find_all('div', class_='highlight__links')
        for content in highlight_links:
            list_link = content.find('ul').find_all('a')
            for link in list_link:
                content_dict = {}

                title = link.get_text().strip()
                content_dict['id'] = generate_id(title)
                content_dict['title'] = title
                content_dict['link'] = link['href']
                content_dict['sentiment'] = ''
                content_dict['sentiment_score'] = 0
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

        news_title = soup.find_all(['h3', 'h2'], class_=['block__news__title', 'news-item-header__title'])
        for title in news_title:
            content_dict = {}
            link = title.find_parent('a')
            if link:
                title = title.get_text().strip()    
                content_dict['id'] = generate_id(title)
                content_dict['title'] = title
                content_dict['link'] = link['href']
                content_dict['sentiment'] = ''
                content_dict['sentiment_score'] = 0
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

def generate_id(title):
    return hashlib.sha256(title.encode('utf-8')).hexdigest()[:16]

def predict_sentiment(news_list):
    print("Predizendo sentimento...")
    tokenizer = AutoTokenizer.from_pretrained("pysentimiento/bertweet-pt-sentiment", clean_up_tokenization_spaces=True)
    bert = AutoModelForSequenceClassification.from_pretrained("pysentimiento/bertweet-pt-sentiment")

    labels = {0: "Negativo", 1: "Neutro", 2: "Positivo"}
    with torch.no_grad():
        for news in news_list:
            print(f"Sentimento da notícia: {news['title']}", end="... ")
            inputs = tokenizer(news['title'], return_tensors="pt", truncation=True)
            outputs = bert(**inputs)

            probabilities = torch.softmax(outputs.logits, dim=1).cpu().numpy()
            
            sentiment = labels[np.argmax(probabilities)]
            sentiment_score = np.max(probabilities)

            news['sentiment'] = sentiment
            news['sentiment_score'] = sentiment_score

            print(f"Sentimento: {sentiment}, Score: {sentiment_score}")


    return news_list

def main():
    news = fetch_news_cnn()
    news += fetch_news_valor()
    news = predict_sentiment(news)
    save_csv(news, f'news_{datetime.now().strftime("%Y-%m-%d_%H")}.csv')


if __name__ == "__main__":
    main()
