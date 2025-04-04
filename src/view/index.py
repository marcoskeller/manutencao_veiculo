import streamlit as st
from streamlit_option_menu import option_menu
from src.view.pagina_relatorio_view import relatorio_basico_view
from src.view.pagina_veiculo_view import veiculo_basico_view
from src.view.pagina_manutencao_view import manutencao_view
from src.view.pagina_oleo_view import oleo_view
from src.view.pagina_pneu_view import pneu_view



def inicio():
   
    st.set_page_config(layout='wide',initial_sidebar_state='collapsed',)

    with st.sidebar:
        selected = option_menu("Menu", ["Veículos", 'Manutenção', 'Relatório'], 
            icons=['house', 'gear','cloud-upload'], menu_icon="cast", default_index=1)
        selected

        
    opcao = option_menu(None, ["Veiculo", "Manutenção","Óleo", "Pneu",'Relatório'],
                            icons=['house', 'cloud-upload', "list-task", 'gear'],
                            key='menu_5', orientation="horizontal")
    opcao

    if opcao == "Veiculo":
        veiculo_basico_view()    
    if opcao == "Manutenção":
        manutencao_view()
    if opcao == "Óleo":
        oleo_view()
    if opcao == "Pneu":
        pneu_view()
    if opcao == "Relatório":
        relatorio_basico_view()

  


