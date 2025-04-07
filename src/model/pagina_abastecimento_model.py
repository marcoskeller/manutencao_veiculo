import streamlit as st
import pandas as pd
import numpy as np
import logging

#Funcao para Formatar Valores Monetarios
def formatar_moeda_pais(valor):
    valor_formatado = "R${:,.2f}".format(valor)
    valor_formatado = valor_formatado.replace(',', 'temp').replace('.', ',').replace('temp', '.')
    return valor_formatado

#Funcao para Formatar Valores Numericos
def formatar_valores_numericos(valor):
    valor_formatado = "{:,.2f}".format(valor)
    valor_formatado = valor_formatado.replace(',', 'temp').replace('.', ',').replace('temp', '.')
    return valor_formatado

 

#Leitura do arquivo Excel
def leitura_arquivo_excel():
    try:
        # Configuração do logger
        logging.basicConfig(level=logging.INFO, filename="./logs/abastecimento.log", format="%(asctime)s - %(levelname)s - %(message)s")
        df = pd.read_excel('./dados/Controle_Manutencao_Honda_City.xlsm', sheet_name = '4. ABASTECIMENTOS', skiprows = 6, usecols = range(0,10))
        df["Custo total R$"] = df["Custo total R$"].apply(formatar_moeda_pais)
        df["Preço por litro"] = df["Preço por litro"].apply(formatar_moeda_pais)
        df["Litros abastecidos"] = df["Litros abastecidos"].apply(formatar_valores_numericos)
        logging.info("Arquivo da Pagina Abastecimento lido com sucesso.")
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
def abastecimento_model():
    # Lê o arquivo Excel e armazena em um DataFrame
    df = leitura_arquivo_excel()

    #Formatação da coluna 'Data' para o formato datetime
    df['Data'] = pd.to_datetime(df['Data'])
    df['Data'] = df['Data'].dt.strftime('%d/%m/%Y')
    
    # Exibe o DataFrame no Streamlit
    st.dataframe(df)