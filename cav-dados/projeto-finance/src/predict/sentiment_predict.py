from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import numpy as np


def predict_sentiment(news_list):
    print("Predizendo sentimento...")
    tokenizer = AutoTokenizer.from_pretrained(
        "pysentimiento/bertweet-pt-sentiment", clean_up_tokenization_spaces=True
    )
    bert = AutoModelForSequenceClassification.from_pretrained(
        "pysentimiento/bertweet-pt-sentiment"
    )

    labels = {0: "Negativo", 1: "Neutro", 2: "Positivo"}
    with torch.no_grad():
        for news in news_list:
            print(f"Sentimento da notícia: {news['title']}", end="... ")
            inputs = tokenizer(news["title"], return_tensors="pt", truncation=True)
            outputs = bert(**inputs)

            probabilities = torch.softmax(outputs.logits, dim=1).cpu().numpy()

            sentiment = labels[np.argmax(probabilities)]
            sentiment_score = np.max(probabilities)

            news["sentiment"] = sentiment
            news["sentiment_score"] = float(sentiment_score)

    return news_list
