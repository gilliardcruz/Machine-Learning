import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta
import logging
import os


logging.basicConfig(level=logging.INFO)

def gerar_dados_vendas(numero_registros: int = 1000) -> pd.DataFrame:
    """Gera um DataFrame com dados fictícios de vendas de e-commerce."""
    fake = Faker()
    random.seed(42)

    produtos = [
        "Smartphone X", "Fone de Ouvido Bluetooth", "Notebook Pro",
        "Smartwatch", "Tablet Mini", "Carregador Portátil",
        "Capinha para Celular", "Mouse Sem Fio", "Teclado Mecânico",
        "Monitor 24\"", "HD Externo 1TB", "SSD 500GB",
        "Câmera Digital", "Caixa de Som", "Roteador Wi-Fi"
    ]
    cidades = [
        "São Paulo", "Rio de Janeiro", "Belo Horizonte", "Porto Alegre",
        "Curitiba", "Brasília", "Salvador", "Recife", "Fortaleza", "Manaus"
    ]

    def _gerar_data_aleatoria() -> datetime:
        start = datetime.now() - timedelta(days=180)
        end = datetime.now()
        return start + timedelta(days=random.randint(0, (end - start).days))

    dados = []
    for _ in range(numero_registros):
        dados.append({
            "id_compra": fake.unique.random_number(digits=8),
            "data_hora": _gerar_data_aleatoria(),
            "produto": random.choice(produtos),
            "preco_unitario": round(random.uniform(50, 2000), 2),
            "quantidade": random.randint(1, 5),
            "cliente": fake.name(),
            "cidade": random.choice(cidades),
            "forma_pagamento": random.choice(["Cartão de Crédito", "Boleto", "Pix", "Débito"]),
            "frete": round(random.uniform(5, 50), 2),
            "avaliacao": random.choice([1, 2, 3, 4, 5, None])
        })

    df = pd.DataFrame(dados)
    df["valor_total"] = df["preco_unitario"] * df["quantidade"] + df["frete"]
    return df
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

valor_str = "10.574,28"
valor = locale.atof(valor_str)

print(valor)

def salvar_dados(df: pd.DataFrame, caminho: str = "../data/vendas_ecommerce.csv") -> None:
    """Salva o DataFrame em um arquivo CSV."""
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    df.to_csv(caminho, index=False, encoding='UTF-8')

if __name__ == "__main__":
    logging.info("Iniciando geração de dados...")
    df = gerar_dados_vendas()
    salvar_dados(df)
    logging.info("Dataset gerado e salvo com sucesso!")
