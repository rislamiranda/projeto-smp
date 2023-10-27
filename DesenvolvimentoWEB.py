import streamlit as st
import pandas as pd
#import seaborn as sns
#import matplotlib.pyplot as plt
#import numpy as np
import os
import webbrowser
from PIL import Image


# escrevendo um título na página
st.markdown("<h1 style='text-align: center; color: grey;'>PROJETO BOOTCAMP</h1>", unsafe_allow_html=True)
#st.title("PROJETO BOOTCAMP", justify="center")


st.markdown("<h2 style='text-align: center; color: blue;'>MERCADO REGULADO TELEFONIA MÓVEL</h2>", unsafe_allow_html=True)
#st.markdown("<h1 style='text-align: center; color: blue;'>TELEFONIA MÓVEL</h1>", unsafe_allow_html=True)
#st.title('** MERCADO REGULADO DE TELEFONIA MÓVEL **')

# Importar a imagem
image = Image.open("image.png")
left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image(image, width=400)

st.markdown("<h3 style='text-align: center; color: black;'>Análise de Política Pública de Concorrência </h3>", unsafe_allow_html=True)
#st.header('Análise de política pública de concorrência\n')
st.write('Nesse projeto apresentamos uma série temporal de acessos no mercado de telefonia móvel, identificando  padrões e tendências nesse mercado e analisando a qualidade do serviço a partir do uso de tecnologias (4G, 3G e 2G)')

## Incorporando e centralizando  a figura


# Carrega a imagem
#st.image('image.png')

# Importar a imagem
#image = Image.open("fig/image.png")

#left_co, cent_co,last_co = st.columns(3)
#with cent_co:
 #   st.image(image, width=500)


st.header("CONTEXTUALIZANDO")
# Exibe um texto com uma tabela
st.markdown("Política de concorrência em mercado regulado")
st.markdown("Mercado de telefonia móvel")
st.markdown("Papel do CADE na defesa da concorrência")
st.markdown("Política que impacta diretamente nossa rotina como consumidores")

st.header("OBJETIVOS")
st.markdown("Construir uma série temporal de acessos no mercado de telefonia móvel")
st.markdown("Identificar padrões e tendências nesse mercado")
st.markdown("Analisar a qualidade do serviço a partir da tecnologia (4G, 3G e 2G))")
st.markdown("Criar um relatório final com as análises realizadas e publicação dos scripts de análise")

st.header("LINKS")
# Criando os botões
btn_documentacao = st.button("Documentação")
btn_painel = st.button("Painel")

# Coloca os botões lado a lado
col1, col2 = st.columns(2)

# Adiciona os botões às colunas
col1.write(btn_documentacao)
col2.write(btn_painel)


# Abre a documentação do painel quando o botão "Documentação" é clicado
if btn_documentacao:
    webbrowser.open("https://www.gov.br/mec/pt-br/assuntos/paineis-de-monitoramento-e-indicadores")

# Abre o painel em si quando o botão "Painel" é clicado
if btn_painel:
    webbrowser.open("https://www.gov.br/mec/pt-br/assuntos/paineis-de-monitoramento-e-indicadores")



