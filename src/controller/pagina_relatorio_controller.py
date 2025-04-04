import streamlit as st
from src.model.pagina_relatorio_model import exibicao_dataframe



def relatorio_basico_controller():
    exibicao_dataframe()