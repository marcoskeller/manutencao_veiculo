import streamlit as st
import pandas as pd 
import logging

 
#Leitura do arquivo Excel
def leitura_arquivo_excel():
    try:
        # Configuração do logger
        logging.basicConfig(level=logging.INFO, filename="./logs/oleo.log", format="%(asctime)s - %(levelname)s - %(message)s")
        df = pd.read_excel('./dados/Controle_Manutencao_Honda_City.xlsm', sheet_name = '6. TROCAS DE ÓLEO', skiprows = 6, usecols = range(0,13))
        logging.info("Arquivo da Pagina Oleo lido com sucesso.")
        return df  

    except FileNotFoundError as error:
        logging.error(f"Nao foi possivel encontrar o arquivo especificado.: {error}")
        print("Erro: Nao foi possivel encontrar o arquivo especificado.")
    except FileExistsError as error:
        logging.error(f"Nao foi possivel ler o arquivo, pois o mesmo contem erro: {error}")
        print("Erro: Nao foi possível ler o arquivo, pois o mesmo contem erro.")
    except Exception as error:
        logging.error(f"Erro inesperado: {error}")
        print("Erro: Erro inesperado ao ler o arquivo.")




# Função para exibir a página de manutenção
def oleo_model():
    # Lê o arquivo Excel e armazena em um DataFrame
    df = leitura_arquivo_excel()
    # Exibe o DataFrame no Streamlit
    st.dataframe(df)