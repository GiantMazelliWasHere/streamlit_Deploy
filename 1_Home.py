import streamlit as st
import pandas as pd
import numpy as np
from streamlit_extras.app_logo import add_logo

st.set_page_config(page_title="Eduardo Mazelli", layout="wide")

st.logo("images/crowdstrike.png")

st.sidebar.markdown("Desenvolvido por Eduardo Mazelli ®️ 2025")

col1, col2 = st.sidebar.columns([0.5, 0.5])
col1.markdown("""<a href="https://github.com/GiantMazelliWasHere"><img src="https://cdn3.emoji.gg/emojis/6705-githubblack.png" width="64px" height="64px" alt="github"></a>""", unsafe_allow_html=True)
col2.markdown("""<a href="https://www.linkedin.com/in/eduardo-mazelli/"><img src="https://cdn3.emoji.gg/emojis/70322-linkedin.png" width="64px" height="64px" alt="LinkedIn"></a>""""", unsafe_allow_html=True)

col1, col2 = st.columns([0.25, 0.75])
col1.image("images/perfil.png", width=150)
col2.title("Eduardo Mazelli")
col2.write("+55 (11) 97649-4397")
col2.write("eduardo.mazelli@gmail.com")

st.title("Sobre Mim!")

st.write("Nasci e cresci na cidade, sempre estive cercado por inovação, mudanças rápidas e infinitas oportunidades. Esse ambiente dinâmico moldou minha curiosidade e determinação, levando-me a seguir um caminho na tecnologia.")
st.write("Desde de muito pequeno adoro mecher com computadores e video games. Em casa brinco que sou o TI da fámilia, sempre ajudando a resolver problemas com computadores e cel.")
st.write("Após focar muito na parte criativa do meu cérebro e me formar em Pulbicidade, decidi que não era minha paixão e que realmente não tinha como negar que tecnologia era o meu lugar. Então me inscrevi e vim cursar Engenharia de Software na Fiap.")
st.write("Desde a adolescencia em decorrer dos conteúdos que eu consumia em meu tempo livre (filmes, séries e jogos) fiquei apaixonado por hacking e por como podemos usar esse mal para o bem.")
st.write("Por isso meu objetivo profissional e me tornar um hacker ético em poder assim ajudar cadavez mais empresas e governos a se protegerem de ataques cibernéticos.")
