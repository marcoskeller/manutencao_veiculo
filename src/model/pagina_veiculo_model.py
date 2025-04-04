import streamlit as st
import pandas as pd 
from datetime import datetime

#Leitura do arquivo CSV
def leitura_arquivo_excel():
    # Lê o arquivo CSV e armazena em um DataFrame
    df = pd.read_excel('./dados/Controle_Manutencao_Honda_City.xlsm', sheet_name = '2. CADASTRO DE VEÍCULOS', skiprows = 7, usecols = range(1,6))
    
    return df


def exibicao_dataframe():
    # Lê o arquivo Excel e armazena em um DataFrame
    df = leitura_arquivo_excel()
    # Exibe o DataFrame no Streamlit
    st.dataframe(df)