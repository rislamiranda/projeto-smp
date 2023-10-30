### ************************************************************************************###
### Bibliotecas necessárias ###
### ************************************************************************************###
import streamlit as st
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt

import plotly.express as px
import plotly.io as pio

import os
from geojson_rewind import rewind
import requests

### ************************************************************************************###
### Adicionando o título da página ###
### ************************************************************************************###
st.markdown("-------------------")
st.markdown("<h3 style='text-align: justify; color: black;'> REPRESENTAÇÃO BIDIMENSIONAL - MAPAS</h3>", unsafe_allow_html=True)
st.markdown("-------------------")

### ************************************************************************************###
### Adicionando  texto no corpo da página ###
### ************************************************************************************###
st.markdown("<h5 style='text-align: justify; color: black;'>Esse projeto resultou em um conjunto de mapas/gráficos visando facilitar as análises e entendimento dos resultados pelos interessados: </h5>", unsafe_allow_html=True)
st.markdown("-------------------")


# arquivo = './Bootcamp Enap/projeto-smp/df_tec_geracao.csv'

### ************************************************************************************###
### Orientação do Bruno para melhorar a performance da exibição dos dados ###
### ************************************************************************************###
#@st.cache_data


### ************************************************************************************###
### Função de carga dos dados ###
### ************************************************************************************###
@st.cache_data
def load_data(arquivo):
    # Carregue os dados do arquivo CSV
    #data = pd.read_csv(arquivo, sep=';')
    data = pd.read_csv(arquivo, sep=';',encoding='utf-8')

    # Retorne os dados
    return data

@st.cache_data
def abre_url():
    return requests.get(f'http://servicodados.ibge.gov.br/api/v3/malhas/paises/BR?formato=application/vnd.geo+json&qualidade=minima&intrarregiao=municipio').json()
    

    
### ************************************************************************************###
### Inicio do Código da Bia para criar o MAPA
### ************************************************************************************###

# Chame a função de carga dos dados
arquivo = '../data/df_tec_geracao.csv'
df = load_data(arquivo)


print(len(df))
print(df.shape)

df.head()

# vemos que os decimais estao com virgula, e nao com ponto (que é o default do python)

# retirando a coluna 'Unnamed: 0'

df = df.drop(columns = ['Unnamed: 0'])

print(df['percentual'].dtype)
print(df['media_ano'].dtype)

# o tipo do dado que vou manipular('percentual') está em formato string, e não float

df['media_ano'] = df['media_ano'].str.replace(',', '.', regex=True).astype(float)
df['percentual'] = df['percentual'].str.replace(',', '.', regex=True).astype(float)

# estamos aplicando a substituição do caracter ',' por '.' em cada coluna ('percentual' e 'media_ano') 
# individualmente; e depois usamos o método astype(float) para converter os valores para o tipo de dados float


# restringindo o numero de casas decimais da coluna percentual a 2 casas decimais

df['percentual'] = df['percentual'].round(2)

print(df['percentual'].dtype)
print(df['media_ano'].dtype)

# agora ambas as colunas são do tipo float e são manipuláveis em operações matemáticas

df.head(20)

# vendo a tabela mais ampla
# temos 2 casas decimais na coluna 'percentual'

# vendo quais tipos de tecnologia tivemos ao longo dos últimos 15 anos: foram 7

print(df['Tecnologia Geração'].unique())
print(len(df['Tecnologia Geração'].unique()))

tec_1g = df.query('`Tecnologia Geração` == "1G"')
tec_2g = df.query('`Tecnologia Geração` == "2G"')
tec_3g = df.query('`Tecnologia Geração` == "3G"')
tec_4g = df.query('`Tecnologia Geração` == "4G"')
tec_m2m = df.query('`Tecnologia Geração` == "M2M"')
tec_5g = df.query('`Tecnologia Geração` == "5G"')
tec_5g_nsa = df.query('`Tecnologia Geração` == "5G Non Stand Alone"')

# ChatCPT me ajudando na sintaxe:
# O erro no código que você forneceu está relacionado à forma como o nome da coluna 'Tecnologia Geração' é 
# especificado na consulta. O espaço no nome da coluna requer que você o coloque entre colchetes ou aspas.
# Neste código corrigido, usamos as crases (``) para cercar o nome da coluna 'Tecnologia Geração' porque ele 
# contém espaços. Também usamos as aspas duplas ("2G") para comparar com o valor "2G" na coluna.

# vendo os dataframes por tecnologia

#tec_5g_nsa

df['Tecnologia Geração'].unique()

## comandos para plotar um gráfico do pyplot do matplotlib

grafico_1 = plt.figure(figsize=(8,5))
plt.plot(tec_1g["ano"], tec_1g["percentual"], label = "1G", linewidth = 2.5, color = "cyan") #argumentos são eixo x e eixo y
plt.plot(tec_2g["ano"], tec_2g["percentual"], label = "2G", linewidth = 2.5, color = "green")
plt.plot(tec_3g["ano"], tec_3g["percentual"], label = "3G", linewidth = 2.5, color = "purple")
plt.plot(tec_m2m["ano"], tec_m2m["percentual"], label = "M2M", linewidth = 2.5, color = "gold")
plt.plot(tec_4g["ano"], tec_4g["percentual"], label = "4G", linewidth = 2.5, color = "red")
plt.plot(tec_5g["ano"], tec_5g["percentual"], label = "5G", linewidth = 2.5, color = "magenta")
#plt.plot(tec_5g_nsa["ano"], tec_5g_nsa["percentual"], label = "5G-NSA", linewidth = 2.5, color = "blue")
plt.title("Evolução das Tecnologias de Geração \n Anos 2009 a 2023", fontweight='bold')
plt.xlabel("Período")
plt.ylabel("Acessos no ano (%)")
plt.annotate('Ápice do 3G', (2015,60), xytext=(2015 + 1, 60 + 6),
             arrowprops=dict(facecolor='black', shrink=0.05))
plt.annotate('4G é a tecnologia mais utilizada atualmente', (2023,80), xytext=(2015, 80 + 10),
             arrowprops=dict(facecolor='black', shrink=0.05))
plt.ticklabel_format(style="plain", axis="y")
plt.grid()
plt.legend()
#plt.show()
st.pyplot(grafico_1)

#plt.savefig('grafico_tecnologia_estatico.png')



### ************************************************************************************###
### Inicio do Código da FERNANDA para criar o GRAFICO DINÂMICO
### ************************************************************************************###

os.getcwd()
arquivo = '../data/df_cm_ddd.csv'
resultados = load_data(arquivo)

resultados.info()

#Modificações Hélio
resultados['media_ano'] = resultados['media_ano'].map(lambda x: float(x.replace(',', '.')))

resultados = resultados[resultados['Grupo Econômico'] == 'TELECOM AMERICAS']

#criando dataframe com informações de georreferenciamento de municípios
georreferenciamento_df = pd.read_csv('https://raw.githubusercontent.com/kelvins/Municipios-Brasileiros/main/csv/municipios.csv')

#os dados de georreferenciamento tem 7 dígitos (vamos remover o dígito verificador e atualizar o dataframe)
georreferenciamento_df['codigo_ibge'] = georreferenciamento_df['codigo_ibge']//10

georreferenciamento_df.head()

#cruzamento do dataframe resultados com as informações de georreferenciamento
resultados_df = pd.merge(resultados[['Código Nacional', 'ano', 'media_ano']],
                         georreferenciamento_df[['ddd', 'nome', 'codigo_ibge', 'codigo_uf', 'latitude', 'longitude']],
                         left_on='Código Nacional',
                         right_on='ddd',
                         how='inner')



resultados_df.head()

#puxar a malha geográfica do brasil a nível de município

#geojson = requests.get(f'http://servicodados.ibge.gov.br/api/v3/malhas/paises/BR?formato=application/vnd.geo+json&qualidade=minima&intrarregiao=municipio').json()
geojson = abre_url()

#a malha geográfica do ibge tem 7 dígitos (vamos remover o dígito verificador e atualizar a malha)

for feature in geojson['features']:
    feature['properties']['codarea'] = feature['properties']['codarea'][:-1]
geojson = rewind(geojson, rfc7946=False)


max_min = resultados_df.groupby('ano').agg({'media_ano':'max'}).min().values[0]
max_min

resultados_df['media_ano'] = resultados_df['media_ano'].map(lambda x:max_min if x > max_min else x)

#construir o mapa choroplético com timeline no campo de ano
#import plotly.express as px
#import plotly.io as pio
#pio.renderers.default = 'iframe'

fig = px.choropleth(resultados_df,
                    geojson=geojson,
                    # scope='south america',
                    color='media_ano',
                    color_continuous_scale="Reds",
                    locations='codigo_ibge',
                    featureidkey='properties.codarea',
                    hover_name='nome',
                    animation_frame='ano')

fig.update_layout(height=800, width=1000, autosize=False)
fig.update_geos(fitbounds = "locations", visible = False)
fig.update_traces(marker_line_width=0)  ## alteração do Helio

st.plotly_chart(fig)




### ************************************************************************************###
### Código EXTRA ###
### ************************************************************************************###
## Dar preferência a usar os comandos do streamlit ao inves do plotly


#criando um gráfico de linhas responsivo
##grafico_2 = px.line(df, x = "ano", y = "percentual", color="Tecnologia Geração").update_layout(
#xaxis_title = "Período",
#yaxis_title = "Acessos no ano (%)",
#title = "Evolução das Tecnologias de Geração - Anos 2009 a 2023",
#title_font_color = "blue",
#title_font_size = 24,
#title_x = 0.05,
#title_y = 0.93,
#xaxis_color = "blue",
#yaxis_color = "blue",
#xaxis_title_font=dict(size=16),
#yaxis_title_font=dict(size=16))

#o title_x pode varia de 0 a 1, e é a centralização do título em relação ao eixo x (ajuste na horizontal)
#o title_y é o ajuste na vertical (varia de 0 a 1)

#grafico_2

#grafico_2.write_html('grafico_tecnologia_dinamico.html')