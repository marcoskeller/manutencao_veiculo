import streamlit as st
from streamlit_option_menu import option_menu
from src.controller.pagina_relatorio_controller import relatorio_basico_controller



def inicio():
   
    st.set_page_config(layout='wide',initial_sidebar_state='collapsed',)

    with st.sidebar:
        selected = option_menu("Menu", ["Veículos", 'Manutenção', 'Relatório'], 
            icons=['house', 'gear','cloud-upload'], menu_icon="cast", default_index=1)
        selected

        
    opcao = option_menu(None, ["Inicio", "Veiculo", "Manutenção", 'Relatório'],
                            icons=['house', 'cloud-upload', "list-task", 'gear'],
                            key='menu_5', orientation="horizontal")
    opcao

    if opcao == "Inicio":
        st.title("Página Inicial")
        st.write("Bem-vindo à página inicial!")
    if opcao == "Veiculo":
        st.title("Veículo")
        st.write("Aqui você pode gerenciar os veículos.")
    if opcao == "Manutenção":
        st.title("Manutenção")
        st.write("Aqui você pode gerenciar a manutenção dos veículos.")
    if opcao == "Relatório":
        relatorio_basico_controller()

  


