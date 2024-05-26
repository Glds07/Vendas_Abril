import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Movientação mensal GL")

with st.container():
    st.subheader("Vendas de relógios e bijuterias do mês de Abril")
    st.title("Movimentação mensal")
    st.write("Informações sobre as vendas do mês de Abril")

@st.cache_data
def carregar_dados_rel():
    tabela_rel = pd.read_csv("atividade_rel.csv")
    return tabela_rel

with st.container():
    st.write("---")
    st.subheader("Relógios vendidos no mês de Abril")
    qtde_dias = st.selectbox("Selecione o período", ["7D", "14D", "21D", "30D"])
    num_dias = int(qtde_dias.replace("D", " "))
    dados = carregar_dados_rel()
    dados = dados[:num_dias]
    st.area_chart(dados, x="Data", y="Itens vendidos")

@st.cache_data
def carregar_dados_biju():
    tabela_biju = pd.read_csv("atividade_biju.csv")
    return tabela_biju

with st.container():
    st.write("---")
    st.subheader("Bijuterias vendidas no mês de Abril")
    qtde_dias = st.selectbox("Selecione o período ", ["7D", "14D", "21D", "30D"])
    num_dias = int(qtde_dias.replace("D", " "))
    dados = carregar_dados_biju()
    dados = dados[:num_dias]
    st.area_chart(dados, x="Data", y="Itens vendidos")