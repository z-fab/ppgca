# Projeto Finance - Coleta e Disponibilização de Dados Financeiros

**Integrantes do Grupo**:

- Daniel Mangabeira (RA 10729073)
- Fabricio Zillig (RA 10241726)
- Messias de Oliveira (RA 10310225)

**Link para Artigo**: [Coletor_e_Analisador_de_Notícias_Econômicas.pdf](Coletor_e_Analisador_de_Notícias_Econômicas.pdf)

**Link API**: http://ppgca.zfab.me/projeto-finance/api/docs

**Link Kibana**: http://ppgca.zfab.me/projeto-finance/kibana
*Login: admin / mackrogerio*

---

O projeto Finance tem como objetivo responder a seguinte pergunta: "As notícias financeiras afetam o valor do IBovespa?".

Este projeto tem como objetivo coletar notícias financeiras de fontes específicas, prever o "mood" da notícia (se é positiva, negativa ou neutra) e coletar o valor do índice financeiro de hora em hora. Os dados coletados são disponibilizados via uma API para consumo e análise.


## Funcionalidades

- Coleta de notícias financeiras de fontes específicas utilizando `web scraping` (via BeautifulSoup).
- Coleta do valor do índice financeiro de hora em hora utilizando a biblioteca `yfinance`.
- Registro das informações coletadas no banco de dados `MongoDB` e `ElasticSearch` através de `Streaming` usando `Kafka`.
- Visualização dos dados coletados através do `Kibana`.
- Agendamento de tarefas para coleta automática utilizando `APScheduler`.
- Disponibilização dos dados via uma API construída com `FastAPI`.

## Requisitos

- Python 3.10+
- Docker

## Tecnologias Utilizadas

- **MongoDB**: Banco de dados para armazenar as notícias e valores coletados.
- **Elasticsearch**: Banco de dados para armazenar as notícias e valores coletados.
- **Kibana**: Ferramenta de visualização de dados para o Elasticsearch.
- **Pytorch** e **Transformers**: Para realizar a classificação de sentimento das notícias.
- **Kafka**: Para processamento e comunicação entre serviços.
- **BeautifulSoup**: Utilizado para fazer scraping de notícias financeiras.
- **yfinance**: Para buscar os valores do índice financeiro de hora em hora.
- **APScheduler**: Agendador de tarefas para garantir a coleta periódica dos dados.
- **FastAPI**: Framework utilizado para disponibilizar uma API que permite o consumo dos dados coletados.
- **Uvicorn**: Servidor ASGI utilizado para rodar a aplicação FastAPI.
- **Docker**: Utilizado para encapsular todo o ambiente do projeto em containers.

## Instalação

### Usando Docker (Recomendado)

Clone este repositório:

```bash
git clone <url-do-repositorio>
cd projeto-finance
```

Crie o arquivo .env baseado no arquivo .env.example, e configure suas variáveis de ambiente.

Para construir e iniciar os serviços, utilize os seguintes comandos:

```bash
make build
make up
````
Para destruir os containers e volumes criados:

```bash
make destroy
```

Para visualizar os logs dos serviços:

```bash
make logs
```