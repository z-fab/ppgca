# Coletor e Analisador de Notícias Econômicas

Este script Python coleta notícias econômicas dos sites Valor Econômico e CNN Brasil, realiza análise de sentimento nos títulos das notícias e salva os resultados em um arquivo CSV.

## Funcionalidades

- Coleta notícias do Valor Econômico e CNN Brasil
- Realiza análise de sentimento nos títulos das notícias usando um modelo pré-treinado
- Gera IDs únicos para cada notícia
- Salva os resultados em um arquivo CSV

## Requisitos

Para executar este script, você precisará das seguintes bibliotecas Python:

- requests
- beautifulsoup4
- transformers
- torch
- numpy

Você pode instalar estas dependências usando o pip:

```bash
pip install requests beautifulsoup4 transformers torch numpy
```

## Como usar

1. Clone este repositório ou baixe o arquivo `main.py`.
2. Certifique-se de que todas as dependências estão instaladas.
3. Execute o script:

```bash
python main.py
```

O script irá:
1. Coletar notícias do Valor Econômico e CNN Brasil
2. Realizar análise de sentimento nos títulos
3. Salvar os resultados em um arquivo CSV no formato `news_YYYY-MM-DD_HH.csv`

## Estrutura do arquivo CSV

O arquivo CSV gerado terá as seguintes colunas:

- id: ID único da notícia
- title: Título da notícia
- link: URL da notícia
- sentiment: Sentimento previsto (Negativo, Neutro ou Positivo)
- sentiment_score: Pontuação de confiança do sentimento previsto
- scrapped_at: Data e hora em que a notícia foi coletada

## Notas

- O script usa o modelo "pysentimiento/bertweet-pt-sentiment" para análise de sentimento.
- As notícias são coletadas das páginas principais das seções de economia dos sites mencionados.
- O script pode ser facilmente estendido para coletar notícias de outras fontes.