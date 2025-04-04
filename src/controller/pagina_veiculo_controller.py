import streamlit as st
from src.model.pagina_veiculo_model import exibicao_dataframe


def veiculo_basico_controller():
    exibicao_dataframe()