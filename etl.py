import pandas as pd
import os
import glob


def extrair_dados_e_consolidar(path: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(path, '*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index=True)
    return df_total

def calcular_kpi_de_total_de_vendas(df: pd.DataFrame) -> pd.DataFrame:
    df["Total"] = df["Quantidade"] * df["Venda"]
    return df

def carregar_dados(df: pd.DataFrame, format_saida: list):
    for formato in format_saida:
        if formato == 'csv':
            df.to_csv('dados.csv',index=False)
        if formato == 'parquet':
            df.to_parquet('dados.parquet',index=False)

def pipeline_calcular_kpi_de_vendas_consolidado(pasta: str, formato_de_saida: list):
    df = extrair_dados_e_consolidar(pasta)
    df_novo = calcular_kpi_de_total_de_vendas(df)
    carregar_dados(df_novo, formato_de_saida)