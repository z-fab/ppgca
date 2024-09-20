# Análise de Sentimento de Notícias Financeiras e IBovespa

Este projeto coleta notícias da área financeira e analisa como o sentimento das notícias se reflete no índice IBovespa. O objetivo é extrair notícias, rotulá-las automaticamente usando Machine Learning e prever como o sentimento das notícias pode impactar o mercado financeiro.

## Estrutura do Projeto

O projeto consiste em dois arquivos principais:

### 1. `scraping.py`

Este arquivo é responsável por extrair as notícias financeiras do site da B3. Ele usa bibliotecas de scraping, como `BeautifulSoup` e `requests`, para coletar as manchetes mais recentes e preparar os dados para análise de sentimento.

**Principais Funções:**
- `fetch_news_from_b3()`: Coleta as notícias diretamente do site da B3 e retorna uma lista de manchetes.

### 2. `main.py`

Este arquivo contém o fluxo principal de execução do projeto. Ele faz o seguinte:
1. Coleta as notícias usando o arquivo `scraping.py`.
2. Pré-processa as notícias para remover caracteres especiais e padronizar o texto.
3. Usa a biblioteca **Hugging Face** para classificar automaticamente o sentimento das notícias em positivo ou negativo.
4. Treina um modelo de Random Forest para prever sentimentos futuros com base em novas notícias.
5. Avalia o modelo com uma divisão de dados de treino e teste.

**Principais Funções:**
- `preprocess_text(text)`: Realiza o pré-processamento do texto, removendo caracteres especiais.
- `analyze_sentiment_huggingface(text)`: Classifica o sentimento da notícia (positivo ou negativo) usando o pipeline da Hugging Face.
- `main()`: Controla o fluxo principal de execução, desde a coleta das notícias até a avaliação do modelo.

## Como Executar o Projeto

### Pré-requisitos
- Python 3.8+
- As bibliotecas listadas em `requirements.txt`

### Instalação

1. Clone este repositório.
2. Instale as dependências executando:
   ```bash
   pip install -r requirements.txt
