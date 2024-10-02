import yfinance as yf
from datetime import datetime, timedelta
import logging

LOGGER = logging.getLogger("projeto-finance")


def get_ibovespa():
    end_time = datetime.now()
    start_time = end_time - timedelta(days=5)

    LOGGER.info(f"Buscando dados da Ibovespa de {start_time} até {end_time}")

    # Obter dados históricos com intervalo de 1 hora
    ibov = yf.download(
        tickers="^BVSP",
        start=start_time.strftime("%Y-%m-%d"),
        end=end_time.strftime("%Y-%m-%d"),
        interval="60m",
        progress=False,
    )

    if ibov.empty:
        LOGGER.warning(
            "Nenhum dado retornado. Verifique o símbolo ou a disponibilidade dos dados."
        )
        return

    # Calcular a média dos preços de fechamento por hora
    ibov["Average"] = ibov[["Open", "High", "Low", "Close"]].mean(axis=1)

    # Resetar o índice para facilitar a manipulação
    ibov.reset_index(inplace=True)
    ibov["Datetime"] = ibov["Datetime"].apply(lambda x: x.isoformat())

    # Selecionar apenas as colunas necessárias
    ibov_hourly_average = ibov[["Datetime", "Average"]].rename(
        columns={"Datetime": "date", "Average": "close"}
    )
    ibov_dict = ibov_hourly_average.to_dict("records")

    LOGGER.info(f"Dados da Ibovespa obtidos com sucesso: {ibov_dict}")

    return ibov_dict
