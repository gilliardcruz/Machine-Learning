# Análises E-commerce

Este projeto fornece um dashboard interativo para análise de vendas de e-commerce, incluindo segmentação de clientes e previsão de vendas.

## Visão Geral

O projeto inclui:
- Geração de dados fictícios de vendas.
- Segmentação de clientes usando RFM e K-Means.
- Previsão de vendas com Prophet.
- Dashboard interativo com Streamlit.

## Instalação

1. Clone o repositório.
2. Instale as dependências: `pip install -r requirements.txt` ou `uv sync`.
3. Execute o gerador de dados: `python src/gerador_dados.py`.
4. Execute o dashboard: `streamlit run src/dashboard.py`.

## Como Usar

- Gere dados com o script `gerador_dados.py`.
- Abra o dashboard para visualizar métricas, segmentação e previsões.
- Use os filtros para explorar dados específicos.

## Funcionalidades

- **Métricas**: Total de vendas, média por compra, número de compras.
- **Segmentação**: Análise RFM com clustering.
- **Previsão**: Forecasting de vendas diárias.

## Dependências

- pandas
- numpy
- scikit-learn
- prophet
- streamlit
- faker
- matplotlib
- seaborn
