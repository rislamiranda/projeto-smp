import streamlit as st
import pandas as pd
#import seaborn as sns
#import matplotlib.pyplot as plt
#import numpy as np
import os
import webbrowser

# escrevendo um título na página
st.title('PROJETO BOOTCAMP MERCADO REGULADO DE TELEFONIA MÓVEL')

st.header('Análise de política pública de concorrência\n')
st.write('Nesse projeto vamos aprensentar uma série temporal de acessos no mercado de telefonia móvel, identificar  padrões e tendências nesse mercado e analisar a qualidade do serviço a partir da tecnologia (4G, 3G e 2G)')

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



