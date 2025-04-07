import streamlit as st
import pandas as pd 
import logging

 
#Leitura do arquivo Excel
def leitura_arquivo_excel():
    try:
        # Configuração do logger
        logging.basicConfig(level=logging.INFO, filename="./logs/manutencao.log", format="%(asctime)s - %(levelname)s - %(message)s")
        df = pd.read_excel('./dados/Controle_Manutencao_Honda_City.xlsm', sheet_name = '5. MANUTENÇÕES', skiprows = 6, usecols = range(0,9))
        #df = pd.read_excel('./dados/src/Controle_Manutencao_Honda_City.xlsm', sheet_name = '5. MANUTENÇÕES', skiprows = 6, usecols = range(0,9))
        logging.info("Arquivo da Pagina Manutencao lido com sucesso.")
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


def filtro_exibicao_dataframe_model():
    # Lê o arquivo Excel e armazena em um DataFrame
    df = leitura_arquivo_excel()
    # Cria um filtro para o exibicao dos dados
    opcaoes_tabela = ['Exibir apenas as primeiras linhas', 'Exibir apenas as últimas linhas', 'Exibir amostra aleatória','Exibir todos os dados']
    #exibir_tabela = st.checkbox('Exibir Todos os dados')
    exibir_tabela = st.segmented_control(st.write("Exibir Dados"), opcaoes_tabela, selection_mode="multi")

    if 'Exibir todos os dados' in exibir_tabela:
        # Exibe apenas as primeiras linhas do DataFrame
        st.dataframe(df)
    if 'Exibir apenas as primeiras linhas' in exibir_tabela:
        # Exibe apenas as primeiras linhas do DataFrame
        st.dataframe(df.head())
    if 'Exibir apenas as últimas linhas' in exibir_tabela:
        # Exibe apenas as últimas linhas do DataFrame
        st.dataframe(df.tail())
    if 'Exibir amostra aleatória' in exibir_tabela:
        # Exibe uma amostra aleatória de 10 linhas do DataFrame
        st.dataframe(df.sample(5))
        #d = df.sample(10)
        #st.dataframe(d)


def filtro_exibicao_por_data_model():
    # Lê o arquivo Excel e armazena em um DataFrame
    df = leitura_arquivo_excel()

    #Filtro Data
    # Cria um filtro para a coluna 'Data'
    data_selecionada = st.selectbox('Selecione uma Data', df['Data'].unique())


def filtro_exibicao_por_placa_model():
    # Lê o arquivo Excel e armazena em um DataFrame
    df = leitura_arquivo_excel()

    # Cria um filtro para a coluna 'Placa'
    placa = st.selectbox('Selecione uma Placa', df['Placa'].unique())
    placa_selecionada = df[df['Placa'] == placa]


def filtro_exibicao_por_modelo_fabricante_model():
    # Lê o arquivo Excel e armazena em um DataFrame
    df = leitura_arquivo_excel()

    # Cria um filtro para a coluna 'Modelo	Fabricante'
    modelo = st.selectbox('Selecione um Modelo', df['Fabricante'].unique())
    modelo_fabricante_selecionado = df[df['Fabricante'] == modelo]


def filtro_exibicao_por_estabelecimento_model():
    # Lê o arquivo Excel e armazena em um DataFrame
    df = leitura_arquivo_excel()

    estabelecimento = st.selectbox('Selecione um Estabelecimento', df['Estabelecimento'].unique())
    estabelecimento_selecionado = df[df['Estabelecimento'] == estabelecimento]


def filtro_exibicao_por_tipo_de_servico_model():
    # Lê o arquivo Excel e armazena em um DataFrame
    df = leitura_arquivo_excel()

    # Cria um filtro para a coluna 'Tipo de serviço'
    tipo_servico = st.selectbox('Selecione um Tipo de Serviço', df['Tipo de serviço'].unique())
    df_filtrado = df[df['Tipo de serviço'] == tipo_servico]


def filtro_exibicao_por_descricao_do_servico_model():
    # Lê o arquivo Excel e armazena em um DataFrame
    df = leitura_arquivo_excel()

    # Cria um filtro para a coluna 'Descrição do serviço'
    descricao_servico = st.selectbox('Selecione uma Descrição do Serviço', df['Descrição do serviço'].unique())
    df_filtrado = df[df['Descrição do serviço'] == descricao_servico]


def filtro_exibicao_por_qualificao_do_servico_model():   
    # Lê o arquivo Excel e armazena em um DataFrame
    df = leitura_arquivo_excel()

     # Cria um filtro para a coluna 'Qualificacao do Serviço'
    qualificacao_servico = st.selectbox('Selecione uma Qualificação do Serviço', df['Qualificacao do Serviço'].unique())
    df_filtrado = df[df['Qualificacao do Serviço'] == qualificacao_servico]


def filtro_exibicao_por_custo_total_model():  
    # Lê o arquivo Excel e armazena em um DataFrame
    df = leitura_arquivo_excel()

    # Cria um filtro para a coluna 'Custo total R$'
    custo_total = st.number_input('Selecione um Custo Total', min_value=0, max_value=int(df['Custo total R$'].max()), value=0)
    df_filtrado = df[df['Custo total R$'] == custo_total]


def filtros_model():
    # Mostra as Colunas disponíveis para filtro
    colunas_interesse = ['Data', 'Placa', 'Modelo	Fabricante', 'Estabelecimento',	'Tipo de serviço',	'Descrição do serviço',	'Qualificacao do Serviço',	 'Custo total R$']
    coluna_desejada = st.selectbox('Selecione Abaixo a Categoria Desejada', colunas_interesse, None)

    if coluna_desejada == 'Data':
        #Chama a função de filtro por Data
        filtro_exibicao_por_data_model()
    elif coluna_desejada == 'Placa': 
        #Chama a função de filtro por Placa
        filtro_exibicao_por_placa_model()
    elif coluna_desejada == 'Modelo	Fabricante':
        #Chama a função de filtro por Modelo do Fabricante
        filtro_exibicao_por_modelo_fabricante_model()
    elif coluna_desejada == 'Estabelecimento':
        #Chama a função de filtro por Estabelecimento
        filtro_exibicao_por_estabelecimento_model()
    elif coluna_desejada == 'Tipo de serviço':
        #Chama a função de filtro por Tipo de Serviço
        filtro_exibicao_por_tipo_de_servico_model()
    elif coluna_desejada == 'Descrição do serviço':
        #Chama a função de filtro por Descrição do Serviço
        filtro_exibicao_por_descricao_do_servico_model()
    elif coluna_desejada == 'Qualificacao do Serviço':
        #Chama a função de filtro por Qualificação do Serviço
        filtro_exibicao_por_qualificao_do_servico_model()
    elif coluna_desejada == 'Custo total R$':
        #Chama a função de filtro por Custo Total
        filtro_exibicao_por_custo_total_model()
    else:
        st.write("Nenhum filtro selecionado.")

    

   

# Função para exibir a página de manutenção
def manutencao_model():
    filtro_exibicao_dataframe_model()
    filtros_model()
    #filtro_exibicao_por_data_model()






