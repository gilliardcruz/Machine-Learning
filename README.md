# 📊 Previsão de Vendas E-commerce
Uma aplicação de aprendizado de máquina para prever o valor total de vendas em um e-commerce com base em características temporais.
## 📋 Descrição do Projeto
Este projeto implementa um modelo de regressão usando Random Forest para prever vendas futuras em um e-commerce. O modelo utiliza características temporais (dia, mês e dia da semana) como entrada para prever o valor total de vendas.
### Características
- ✅ Pipeline robusto de preprocessamento de dados
- ✅ Treinamento de modelo com Random Forest
- ✅ Validação cruzada com 5-fold cross-validation
- ✅ Métricas detalhadas (R², MAE, RMSE, MSE)
- ✅ Interface web interativa com Streamlit
- ✅ CLI (Command Line Interface) funcional e intuitiva
- ✅ Modularização limpa do código
- ✅ Logging centralizado e configurável
- ✅ Validação robusta de entrada
- ✅ Testes unitários com pytest
- ✅ Documentação completa com docstrings
## 🚀 Início Rápido
### Pré-requisitos
- Python 3.9 ou superior
- pip
### Instalação
1. Clone ou navegue até o repositório:
```bash
cd previsao-vendas-e-commerce
```
2. Crie um ambiente virtual (recomendado):
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```
3. Instale as dependências:
```bash
pip install -r requirements.txt
```
Para desenvolvimento com testes:
```bash
pip install -r requirements.txt
pip install pytest pytest-cov black flake8 mypy
```
## 📖 Uso
### 1. Treinar o Modelo
```bash
python main.py train
```
**Saída esperada:**
- Logs detalhados do treinamento
- Métricas de desempenho (R², RMSE, MAE)
- Feature importance
- Cross-validation scores
- Modelo salvo em `model.pkl`
### 2. Fazer uma Previsão via CLI
```bash
python main.py predict --day 15 --month 3 --dow 2
```
**Parâmetros:**
- `--day`: Dia do mês (1-31)
- `--month`: Mês (1-12)
- `--dow`: Dia da semana (0=Segunda, 1=Terça, ..., 6=Domingo)
**Exemplo:**
```bash
python main.py predict --day 25 --month 12 --dow 5
# Prevê vendas para 25/12 (Sábado)
```
### 3. Executar a Aplicação Web
```bash
python main.py app
```
A aplicação abrirá automaticamente em `http://localhost:8501`
Interface interativa para:
- Selecionar data e dia da semana
- Visualizar previsão em tempo real
- Formatar resultado em moeda brasileira
### 4. Ver Ajuda
```bash
python main.py --help
python main.py train --help
python main.py predict --help
python main.py app --help
```
## 🧪 Executar Testes
```bash
# Todos os testes
pytest
# Com cobertura
pytest --cov=src --cov-report=html
# Testes específicos
pytest tests/test_predict.py -v
pytest tests/test_preprocess.py -v
```
**Cobertura de testes:**
- ✅ Validação de entrada (make_prediction)
- ✅ Casos limite (min/max values)
- ✅ Tratamento de erro
- ✅ Preprocessamento de dados
- ✅ Extração de features temporais
## 📁 Estrutura do Projeto
```
previsao-vendas-e-commerce/
├── main.py                      # Entry point com CLI
├── requirements.txt             # Dependências
├── pyproject.toml              # Configuração do projeto
├── pytest.ini                  # Configuração do pytest
├── .gitignore                  # Git ignore
├── README.md                   # Este arquivo
├── data/
│   └── ecommerce_dataset.csv   # Dataset de treinamento
├── src/
│   ├── __init__.py
│   ├── config.py               # Configurações centralizadas
│   ├── logger.py               # Sistema de logging
│   ├── preprocess.py           # Preprocessamento de dados
│   ├── train.py                # Script de treinamento
│   └── predict.py              # Funções de previsão
├── app/
│   ├── __init__.py
│   └── app.py                  # Aplicação Streamlit
├── tests/
│   ├── __init__.py
│   ├── test_predict.py         # Testes de previsão
│   └── test_preprocess.py      # Testes de preprocessamento
├── logs/                       # Logs da aplicação
│   └── previsao.log            # Log detalhado
└── model.pkl                   # Modelo treinado (gerado após train)
```
## 📊 Dataset
O dataset contém dados de transações de e-commerce com as seguintes características:
- **data_hora**: Data e hora da transação
- **valor_total**: Valor total da venda (TARGET)
- Outras colunas: produto, preço, quantidade, cliente, etc.
O projeto automaticamente detecta colunas com nomes alternativos:
- Sales: `Total_Amount` ou `valor_total`
- Data: `Date` ou `data_hora`
## 🤖 Modelo
### Algoritmo
- **Random Forest Regressor** com 100 estimadores
### Features (Entradas)
1. `day` - Dia do mês (1-31)
2. `month` - Mês (1-12)
3. `day_of_week` - Dia da semana (0-6, 0=Segunda)
### Target (Saída)
- `sales` - Valor total previsto em R$
### Métricas de Desempenho
- **R² Score**: Coeficiente de determinação
- **RMSE**: Raiz do erro quadrático médio
- **MAE**: Erro absoluto médio
- **MSE**: Erro quadrático médio
- **Cross-validation**: 5-fold cross-validation
## 📝 Logging
O projeto implementa logging centralizado:
- **Arquivo**: `logs/previsao.log` (rotating, máx 10MB)
- **Console**: Saída em tempo real
- **Nível**: Configurável via variável `LOG_LEVEL`
```python
from src.logger import get_logger
logger = get_logger(__name__)
logger.info("Mensagem de informação")
logger.error("Mensagem de erro")
```
## ⚙️ Configuração
Todas as configurações centralizadas em `src/config.py`:
```python
# Diretórios
DATA_PATH = "data/ecommerce_dataset.csv"
MODEL_PATH = "model.pkl"
LOGS_PATH = "logs"
# Parâmetros do modelo
MODEL_CONFIG = {
    'n_estimators': 100,
    'random_state': 42,
    'n_jobs': -1,  # Usar todos os núcleos
}
# Train/Test split
TRAIN_TEST_CONFIG = {
    'test_size': 0.2,
    'random_state': 42,
}
# Features
FEATURE_COLUMNS = ['day', 'month', 'day_of_week']
TARGET_COLUMN = 'sales'
```
## 🔧 Desenvolvimento
### Code Style
Seguir PEP 8 com ferramentas:
```bash
# Formatação
black src/ tests/ main.py
# Linting
flake8 src/ tests/ main.py
# Type checking
mypy src/
```
### Adicionar Novas Features
1. **Editar `src/preprocess.py`**: Extrair feature
2. **Atualizar `src/config.py`**: Adicionar ao `FEATURE_COLUMNS`
3. **Criar testes**: Em `tests/test_preprocess.py`
4. **Treinar modelo**: `python main.py train`
## 🚀 Próximas Etapas Sugeridas
1. ✅ Implementar CLI completa com argparse
2. ✅ Adicionar logging centralizado
3. ✅ Criar testes unitários
4. ⏳ Tentar modelos mais avançados (XGBoost, LightGBM)
5. ⏳ Otimização de hiperparâmetros com GridSearchCV
6. ⏳ Adicionar sazonalidade e tendências
7. ⏳ API REST com FastAPI
8. ⏳ Containerização com Docker
9. ⏳ CI/CD com GitHub Actions
10. ⏳ Deploy em nuvem (Heroku, AWS, GCP)
## 🐛 Troubleshooting
### "Model file not found"
```bash
python main.py train  # Treinar primeiro
```
### "No module named 'src'"
```bash
# Rodar sempre no diretório raiz do projeto
cd previsao-vendas-e-commerce
python main.py train
```
### "Streamlit not found"
```bash
pip install streamlit
```
## 📝 Licença
Projeto de demonstração de Machine Learning em Python
## 👤 Contribuições
Contribuições são bem-vindas! Por favor:
1. Faça um fork
2. Crie uma branch (`git checkout -b feature/improvement`)
3. Commit suas mudanças (`git commit -m "Add feature"`)
4. Push para a branch (`git push origin feature/improvement`)
5. Abra um Pull Request
---
**Versão**: 0.2.0  
**Última atualização**: Abril 2026  
**Status**: ✅ Producção-ready
