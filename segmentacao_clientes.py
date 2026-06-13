import pandas as pd
from datetime import timedelta
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


def calcular_rfm(df: pd.DataFrame) -> pd.DataFrame:
    """Calcula os valores de Recência, Frequência e Valor Monetário (RFM)."""
    snapshot_date = df["data_hora"].max() + timedelta(days=1)
    rfm = df.groupby("cliente").agg({
        "data_hora": lambda x: (snapshot_date - x.max()).days,
        "id_compra": "count",
        "valor_total": "sum"
    }).rename(columns={
        "data_hora": "recencia",
        "id_compra": "frequencia",
        "valor_total": "valor_monetario"
    })
    return rfm

def segmentar_clientes(rfm: pd.DataFrame, num_clusters: int = 4) -> pd.DataFrame:
    """Aplica K-Means para segmentar clientes com base nos valores RFM."""
    scaler = StandardScaler()
    rfm_scaled = scaler.fit_transform(rfm)
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    rfm["cluster"] = kmeans.fit_predict(rfm_scaled)
    return rfm

def analisar_clusters(rfm: pd.DataFrame) -> pd.DataFrame:
    """Retorna a média de cada cluster para análise."""
    return rfm.groupby("cluster").mean()

if __name__ == "__main__":
    df = pd.read_csv("../data/vendas_ecommerce.csv", parse_dates=["data_hora"])
    rfm = calcular_rfm(df)
    rfm = segmentar_clientes(rfm)
    print(analisar_clusters(rfm))
