import streamlit as st
import pandas as pd
import logging



#Leitura do arquivo Excel
def leitura_arquivo_excel():
    try:
        # Configuração do logger
        logging.basicConfig(level=logging.INFO, filename="./logs/veiculo.log", format="%(asctime)s - %(levelname)s - %(message)s")
        
        df = pd.read_excel('./dados/Controle_Manutencao_Honda_City.xlsm', sheet_name = '2. CADASTRO DE VEÍCULOS', skiprows = 7, usecols = range(1,6))
      
        logging.info("Arquivo lido com sucesso.")
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
def veiculo_model():
    # Lê o arquivo Excel e armazena em um DataFrame
    df = leitura_arquivo_excel()
    # Exibe o DataFrame no Streamlit
    st.dataframe(df)