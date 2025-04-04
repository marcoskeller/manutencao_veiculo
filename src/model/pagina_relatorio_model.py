import streamlit as st
import pandas as pd 
import logging
from datetime import datetime



#Leitura do arquivo CSV
def leitura_arquivo_excel():
    # Lê o arquivo CSV e armazena em um DataFrame
    #df = pd.read_csv('./src/dados/Controle Manutencao Honda City.xlsm', sep=';', encoding='latin1')
    df = pd.read_excel('./dados/Controle_Manutencao_Honda_City.xlsm',header = 7, sheet_name = 1)
    return df


# def exibicao_dataframe():
#     # Lê o arquivo CSV e armazena em um DataFrame
#     df = leitura_arquivo_excel()
#     # Exibe o DataFrame no Streamlit
#     st.dataframe(df)

def exibicao_dataframe():
    st.title("Relatórios")
    st.write("Aqui você pode gerenciar o veiculos através de diversos relatórios.")
    # Aqui você pode adicionar o código para gerenciar a manutenção dos veículos, como adicionar, editar ou excluir registros de manutenção.