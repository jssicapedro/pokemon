import pandas as pd
import streamlit as st
from PIL import Image

pokemons = pd.read_csv('Pokemon.csv')
pokemon = list(pokemons['Name'].unique())
tipo1 = list(pokemons['Type 1'].unique())
tipo2 = list(pokemons['Type 2'].unique())

st.title('Pokedex')
st.sidebar.title('Escolhe o teu pokemon')

nome_pokemon = st.sidebar.selectbox('Nome', ['Todos'] + pokemon)
tipo1_pokemon = st.sidebar.selectbox('Tipo 1', ['Todos'] + tipo1)
tipo2_pokemon = st.sidebar.selectbox('Tipo 2', ['Todos'] + tipo2)

pokemons = pokemons[pokemons['Name'] == nome_pokemon]

if tipo1_pokemon != 'Todos':
    tipo_1 = pokemons[pokemons['Type 1'] == tipo1_pokemon]

if nome_pokemon != 'Todos':
    st.title(f'_{nome_pokemon}_')
    id_pokemon = pokemons.iloc[0]['#']
    pasta = f'img/{id_pokemon}.png'
    imagem = Image.open(pasta)
    st.image(imagem)
    st.write(pokemons)
else:
    st.header('Escolhe um pokemon')

if tipo1_pokemon != 'Todos':
    st.write(f'Lista de Pokemons do tipo {tipo1_pokemon}:')
    st.write(pokemons)
else:
    st.write(f'Lista de todos os Pokemons:')
    st.write(pokemons)

