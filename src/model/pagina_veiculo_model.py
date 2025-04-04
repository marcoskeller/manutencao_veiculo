import streamlit as st
import pandas as pd
import logging




#Leitura do arquivo Excel
def leitura_arquivo_excel():
    try:
        # Configuração do logger
        logging.basicConfig(level=logging.INFO, filename="./logs/veiculo.log", format="%(asctime)s - %(levelname)s - %(message)s")
        
        df = pd.read_excel('./dados/Controle_Manutencao_Honda_City.xlsm', sheet_name = '2. CADASTRO DE VEÍCULOS', skiprows = 7, usecols = range(1,6))
         
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

    # Informa se o arquivo foi lido
    logging.info("Arquivo da Pagina Veiculo lido com sucesso.")
    
    # Exibe o DataFrame no Streamlit
    st.dataframe(df)



def carregar_imagem():
    try:
        # Configuração do logger
        logging.basicConfig(level=logging.INFO, filename="./logs/veiculo.log", format="%(asctime)s - %(levelname)s - %(message)s")
        
        #Criacao da lista de imagens
        imgens = ["./img/1_Frente.jpg", "./img/2_Frente.jpg", "./img/3_Panoramica_lateral_direita.jpg", "./img/4_Panoramica_lateral_direita_superior.jpg", "./img/5_Panoramica_lateral_esquerda.jpg", "./img/6_Panoramica_paralama_direito.jpg"]
        
        # Carregar imagem
        st.image(imgens, use_container_width=False, width=455)
        st.image("./img/1_Frente.jpg", caption="Meu Honda City", use_container_width=True)
        st.image("./img/2_Frente.jpg", caption="Meu Honda City", use_container_width=True)
        st.image("./img/3_Panoramica_lateral_direita.jpg", caption="Meu Honda City", use_container_width=True)
        st.image("./img/4_Panoramica_lateral_direita_superior.jpg", caption="Meu Honda City", use_container_width=True)
        st.image("./img/5_Panoramica_lateral_esquerda.jpg", caption="Meu Honda City", use_container_width=True)
        st.image("./img/6_Panoramica_paralama_direito.jpg", caption="Meu Honda City", use_container_width=True)
    
    except FileNotFoundError as error:
        logging.error(f"Nao foi possivel encontrar a(s) imagem(s).: {error}")
        print("Erro: Nao foi possivel encontrar a(s) imagem(s).")
    except FileExistsError as error:
        logging.error(f"Nao foi possivel exibir a(s) imagem(s), pois a(s) mesma(s) contem erro(s): {error}")
        print("Nao foi possivel exibir a(s) imagem(s), pois a(s) mesma(s) contem erro(s).")
    except Exception as error:
        logging.error(f"Erro inesperado: {error}")
        print("Erro: Erro inesperado ao buscar imagem.")
        

  