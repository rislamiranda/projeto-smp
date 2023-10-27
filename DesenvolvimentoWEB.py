### ************************************************************************************###
### Bibliotecas necessárias ###
### ************************************************************************************###

import streamlit as st
import pandas as pd
#import seaborn as sns
#import matplotlib.pyplot as plt
#import numpy as np
import os
import webbrowser
from PIL import Image
from streamlit_option_menu import option_menu



### ************************************************************************************###
### Adicionando MENUS na página ###
### ************************************************************************************###

# Criando o MENU
with st.sidebar:
    selected = option_menu(None, ["O Projeto", 'Sobre Nós'], icons=['house', 'people'], menu_icon="cast", default_index=1, styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "20px"}, 
        "nav-link": {"font-size": "15px", "text-align": "left", "margin":"auto", "--hover-color": "#eee"},
         "nav-link-selected": {"background-color": "green"},
    }
)
    
if selected == "O Projeto":
       st.write(' ')
elif selected == "Sobre Nós":
        st.write(' ')


selected3 = option_menu(None, ["Acesso a Informação",  "Mapa", "Legislação", 'Sobre'], 
        icons=['house', "map", "list-task", 'book'], 
        menu_icon="cast", default_index=0, orientation="horizontal",
        styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "20px"}, 
        "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "green"},
        }
)


### ************************************************************************************###
### Adicionando o texto no corpo da página ###
### ************************************************************************************###

# escrevendo um título na página formato h1
st.markdown("<h1 style='text-align: center; color: grey;'>PROJETO BOOTCAMP</h1>", unsafe_allow_html=True)
#st.title("PROJETO BOOTCAMP", justify="center")

# escrevendo um subtítulo na página formato h2
st.markdown("<h2 style='text-align: center; color: blue;'>MERCADO REGULADO TELEFONIA MÓVEL</h2>", unsafe_allow_html=True)



### ************************************************************************************###
### Adicionando IMAGEM página ###
### ************************************************************************************###

# Importar a imagem
image = Image.open("image.png")
left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image(image, width=400)



### ************************************************************************************###
### Adicionando mais texto no corpo da página ###
### ************************************************************************************###

# escrevendo um subtítulo na página formato h3
st.markdown("<h3 style='text-align: center; color: black;'>Análise de Política Pública de Concorrência </h3>", unsafe_allow_html=True)
#st.header('Análise de política pública de concorrência\n')
st.write('Nesse projeto apresentamos uma série temporal de acessos no mercado de telefonia móvel, identificando  padrões e tendências nesse mercado e analisando a qualidade do serviço a partir do uso de tecnologias (4G, 3G e 2G)')

# escrevendo os textos com markdown

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




### ************************************************************************************###
### Adicionando os links na página ###
### ************************************************************************************###
st.header("LINKS")



### ************************************************************************************###
### Adicionando botões ao final da página e colocando link ###
### ************************************************************************************###
# Coloca os botões lado a lado
col1, col2 = st.columns(2)

# Criando os botões
btn_documentacao = st.button("Documentação")
btn_painel = st.button("Painel")

# Adiciona os botões às colunas e dá nome aos botões
#col1.write(btn_documentacao)
#col2.write(btn_painel)

# Clique no botão
if btn_documentacao:
    webbrowser.open("https://www.gov.br/mec/pt-br/assuntos/paineis-de-monitoramento-e-indicadores")
elif btn_painel:
    webbrowser.open("https://www.gov.br/mec/pt-br/assuntos/paineis-de-monitoramento-e-indicadores")

    
### ************************************************************************************###
### Código EXTRA ###
### ************************************************************************************###

## Incorporando e centralizando  a figura


# Carrega a imagem
#st.image('image.png')

# Importar a imagem
#image = Image.open("fig/image.png")

#left_co, cent_co,last_co = st.columns(3)
#with cent_co:
 #   st.image(image, width=500)


#st.markdown("<h1 style='text-align: center; color: blue;'>TELEFONIA MÓVEL</h1>", unsafe_allow_html=True)
#st.title('** MERCADO REGULADO DE TELEFONIA MÓVEL **')


# Clique no botão
#if btn_painel:
 #   webbrowser.open("https://www.gov.br/mec/pt-br/assuntos/paineis-de-monitoramento-e-indicadores")