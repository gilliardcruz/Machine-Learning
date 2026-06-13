import streamlit as st
import pandas as pd
from pathlib import Path
from segmentacao_clientes import calcular_rfm, segmentar_clientes, analisar_clusters
from previsao_vendas import preparar_dados_vendas, treinar_modelo, prever_vendas


@st.cache_data
def carregar_dados() -> pd.DataFrame:
    """Carrega e retorna os dados de vendas."""
    try:
        # Encontrar o caminho do arquivo de dados de forma robusta
        arquivo_dados = Path(__file__).parent.parent / "data" / "vendas_ecommerce.csv"
        return pd.read_csv(arquivo_dados, parse_dates=["data_hora"])
    except FileNotFoundError:
        st.error("Arquivo de dados não encontrado. Execute o gerador de dados primeiro.")
        return pd.DataFrame()
    except Exception as e:
        st.error(f"Erro ao carregar dados: {e}")
        return pd.DataFrame()

def exibir_metricas(df: pd.DataFrame) -> None:
    """Exibe métricas principais no dashboard."""
    st.header("Métricas Principais")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total de Vendas", f"R$ {df['valor_total'].sum():,.2f}")
    col2.metric("Média por Compra", f"R$ {df['valor_total'].mean():,.2f}")
    col3.metric("Número de Compras", df["id_compra"].count())

def exibir_segmentacao(df: pd.DataFrame) -> None:
    """Exibe a segmentação de clientes no dashboard."""
    st.header("Segmentação de Clientes")
    rfm = calcular_rfm(df)
    rfm = segmentar_clientes(rfm)
    st.write(analisar_clusters(rfm))

def exibir_previsao(df: pd.DataFrame) -> None:
    """Exibe a previsão de vendas no dashboard."""
    st.header("Previsão de Vendas")
    vendas_diarias = preparar_dados_vendas(df)
    model = treinar_modelo(vendas_diarias)
    forecast = prever_vendas(model)
    fig = model.plot(forecast)
    st.pyplot(fig)

def main() -> None:
    st.title("Dashboard de Análise de Vendas")
    df = carregar_dados()

    if df.empty:
        return

    st.sidebar.header("Filtros")
    cidade = st.sidebar.selectbox("Selecione a Cidade", df["cidade"].unique())
    produto = st.sidebar.selectbox("Selecione o Produto", df["produto"].unique())

    df_filtered = df[(df["cidade"] == cidade) & (df["produto"] == produto)]

    exibir_metricas(df_filtered)
    exibir_segmentacao(df)
    exibir_previsao(df)

if __name__ == "__main__":
    main()
