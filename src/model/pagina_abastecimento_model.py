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


# Função para exibir o DataFrame geral de abastecimento sem filtros
def exibi_dataframe_geral_abastecimento():
    # Lê o arquivo Excel e armazena em um DataFrame
    df = leitura_arquivo_excel()

    #Formatação da coluna 'Data' para o formato datetime
    df['Data'] = pd.to_datetime(df['Data'])
    
    #Ordena as Datas
    df = df.sort_values("Data")

    #Formata as Datas para o formato dd/mm/yyyy
    #df['Data'] = df['Data'].dt.strftime('%d/%m/%Y')

    #Trabalhando a Exibição dos dados
    df_colunas_especificas = df[['Data','Placa','Modelo','Tipo de Combustivel','Custo total R$' ,'Preço por litro','Litros abastecidos','Quilometragem do hodômetro (Km)','Km percorridos']]
    
    st.dataframe(df_colunas_especificas, use_container_width=True, hide_index=True)
    # Exibicao de Todos os dados filtrados
    # on = st.toggle("Exibir todos os dados sem filtro!", False, key="exibir_todos_dados_abastecimento")
    # if on:
    #     st.dataframe(df_colunas_especificas, use_container_width=True, hide_index=True)


# Função para exibir a página de manutenção
def abastecimento_model():
    # Lê o arquivo Excel e armazena em um DataFrame
    df = leitura_arquivo_excel()

    
    #Formatação da coluna 'Data' para o formato datetime
    #df['Data'] = pd.to_datetime(df['Data'], format = '%d/%m/%Y')
    df['Data'] = pd.to_datetime(df['Data'])

    #Formata as Datas para o formato dd/mm/yyyy
    #df['Data'] = df['Data'].dt.strftime('%d/%m/%Y')

    
    # Criar uma nova coluna "Mes" e "Ano" que contém o ano e o mês dos abastecimentos
    df["Ano"] = pd.to_datetime(df["Data"]).dt.year
    df["Mes"] = pd.to_datetime(df["Data"]).dt.month_name()

    
    # Criar uma seleção para a escolha do ano do abastecimento
    ano_abastecimento = df["Ano"].unique()
    st.selectbox("Selecione o Ano", ano_abastecimento)
    
    # Criar uma seleção de meses na barra lateral do dashboard
    mes_abastecimento = st.selectbox("Selecione o Mês do Abastecimento", df["Mes"].unique(),None, placeholder="Nenhum Mês Selecionado")

    # Filtrar os dados com base no mês selecionado
    df_filtrado = df[df["Mes"] == mes_abastecimento]

    
    #Trabalhando a Exibição dos dados
    df_colunas_especificas = df_filtrado[['Data','Placa','Modelo','Tipo de Combustivel','Custo total R$' ,'Preço por litro','Litros abastecidos','Quilometragem do hodômetro (Km)','Km percorridos']]
    
    
    # Exibe o DataFrame no Streamlit
    if mes_abastecimento is not None:
        #df_colunas_especificas['Data'].dt.strftime('%d/%m/%Y')
        st.dataframe(df_colunas_especificas, use_container_width=True, hide_index=True)

    
    exibi_dataframe_geral_abastecimento()
        

