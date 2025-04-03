import streamlit as st
from streamlit_option_menu import option_menu

def pagina_inicial():
    #make it look nice from the start
    st.set_page_config(layout='wide',initial_sidebar_state='collapsed',)
    # 1. as sidebar menu
    with st.sidebar:
        selected = option_menu("Menu", ["Veículos", 'Manutenção', 'Dashboard'], 
            icons=['house', 'gear','cloud-upload'], menu_icon="cast", default_index=1)
        selected

        
    opcao = option_menu(None, ["Inicio", "Veiculo", "Manutenção", 'Dashboard'],
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
    if opcao == "Dashboard":
        st.title("Dashboard")
        st.write("Aqui você pode visualizar o dashboard.")
  


