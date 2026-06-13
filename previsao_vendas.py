import pandas as pd
from prophet import Prophet

def preparar_dados_vendas(df: pd.DataFrame) -> pd.DataFrame:
    """Prepara os dados de vendas para o modelo Prophet."""
    vendas_diarias = df.set_index("data_hora").resample("D")["valor_total"].sum().reset_index()
    vendas_diarias = vendas_diarias.rename(columns={"data_hora": "ds", "valor_total": "y"})
    return vendas_diarias

def treinar_modelo(vendas_diarias: pd.DataFrame) -> Prophet:
    """Treina o modelo Prophet com os dados de vendas."""
    model = Prophet()
    model.fit(vendas_diarias)
    return model

def prever_vendas(model: Prophet, periods: int = 30) -> pd.DataFrame:
    """Faz previsão de vendas para os próximos 'periods' dias."""
    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)
    return forecast

if __name__ == "__main__":
    df = pd.read_csv("../data/vendas_ecommerce.csv", parse_dates=["data_hora"])
    vendas_diarias = preparar_dados_vendas(df)
    model = treinar_modelo(vendas_diarias)
    forecast = prever_vendas(model)
    print(forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]].tail())
