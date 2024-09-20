# Scraper de Notícias e API

Este projeto consiste em dois componentes principais: um scraper de notícias que coleta artigos do Globo.com e uma API que serve os dados de notícias coletados.

## Estrutura do Projeto

```
.
├── api/
│   ├── controllers/
│   │   └── data_controller.py
│   ├── models/
│   │   └── news.py
│   ├── routers/
│   │   ├── category.py
│   │   └── root.py
│   └── main.py
├── data/
│   └── news.csv
├── src/
│   ├── controllers/
│   │   └── scrapping.py
│   └── main.py
├── poetry.lock
└── pyproject.toml
```

## Funcionalidades

1. **Scraper de Notícias**: Extrai artigos de notícias do Globo.com, coletando título, categoria e link para cada artigo.
2. **Armazenamento de Dados**: Salva os dados de notícias extraídos em um arquivo CSV no diretório `data/`.
3. **API**: Fornece endpoints para recuperar todas as notícias ou filtrá-las por categoria.

## Configuração

1. Certifique-se de ter o Python 3.12 ou posterior instalado.
2. Instale o Poetry se ainda não o tiver:
   ```
   pip install poetry
   ```
3. Instale as dependências do projeto:
   ```
   poetry install
   ```

## Uso

### Executando o Scraper

Para executar o scraper de notícias:

```
poetry run python src/main.py
```

Isso irá extrair as últimas notícias do Globo.com e salvá-las em `data/news.csv`.

### Iniciando a API

Para iniciar o servidor FastAPI:

```
poetry run fastapi run api/main.py
```

A API estará disponível em `http://localhost:8000`.

## Endpoints da API

1. **Obter Todas as Notícias**
   - URL: `/`
   - Método: GET
   - Descrição: Recupera todos os artigos de notícias extraídos.

2. **Obter Notícias por Categoria**
   - URL: `/category/{categoria}`
   - Método: GET
   - Descrição: Recupera artigos de notícias filtrados pela categoria especificada.
