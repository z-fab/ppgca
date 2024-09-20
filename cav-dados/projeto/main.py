import re
from transformers import pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from scraping import fetch_news_from_b3

# Função para pré-processar o texto
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'\W', ' ', text)  # Remove caracteres especiais
    text = re.sub(r'\s+', ' ', text)  # Remove espaços extras
    return text

# Análise de sentimento usando Hugging Face
def analyze_sentiment_huggingface(text):
    classifier = pipeline('sentiment-analysis')  # Carregar o pipeline de análise de sentimentos
    result = classifier(text)[0]  # Classificar o texto
    return 1 if result['label'] == 'POSITIVE' else 0  # Retornar 1 para positivo e 0 para negativo

# Função principal para executar o pipeline
def main():
    # Coletar as notícias do site da B3
    news_data = fetch_news_from_b3()

    if news_data:
        # Pré-processar as notícias
        processed_news = [preprocess_text(news) for news in news_data]

        # Rotulação automática usando Hugging Face
        labels = [analyze_sentiment_huggingface(news) for news in processed_news]

        # Transformação TF-IDF
        tfidf_vectorizer = TfidfVectorizer(max_features=5000)
        X = tfidf_vectorizer.fit_transform(processed_news).toarray()

        # Divisão dos dados em treino e teste
        X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2, random_state=42)

        # Treinando o modelo
        classifier = RandomForestClassifier(n_estimators=100, random_state=42)
        classifier.fit(X_train, y_train)

        # Avaliação do modelo
        y_pred = classifier.predict(X_test)
        print(classification_report(y_test, y_pred))

        # Função para prever sentimento de novas notícias
        def predict_sentiment(new_text):
            new_text_preprocessed = preprocess_text(new_text)
            new_text_vectorized = tfidf_vectorizer.transform([new_text_preprocessed]).toarray()
            prediction = classifier.predict(new_text_vectorized)
            return prediction

        # Testando uma nova previsão
        new_text = "A bolsa caiu hoje devido a incertezas no mercado."
        print(f"Sentimento da nova notícia: {predict_sentiment(new_text)}")
    else:
        print("Nenhuma notícia foi encontrada.")

if __name__ == "__main__":
    main()
