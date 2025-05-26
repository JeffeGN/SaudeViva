import pandas as pd
# Biblioteca para salvar/carregar modelos treinados em arquivo
import pickle

def carregar_dados(caminho):
    """Carrega um dataset CSV e retorna um DataFrame."""
    return pd.read_csv(caminho)

def salvar_modelo(modelo, caminho="modelos/Modelo_CustoAnual.pkl"):
    """Salva o modelo treinado em um arquivo pickle."""
    with open(caminho, "wb") as arquivo:
        pickle.dump(modelo, arquivo)

def carregar_modelo(caminho="modelos/Modelo_CustoAnual.pkl"):
    """Carrega um modelo pickle salvo anteriormente."""
    with open(caminho, "rb") as arquivo:
        return pickle.load(arquivo)

# dump: salvar arquivo como binário
# rb: read binary
# wb: write binary