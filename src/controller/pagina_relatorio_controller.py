import streamlit as st
import logging
from src.model.pagina_relatorio_model import exibicao_dataframe



def relatorio_basico_controller():
    exibicao_dataframe()