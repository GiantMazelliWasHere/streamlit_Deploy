import streamlit as st
import pandas as pd
import numpy as np
from streamlit_extras.app_logo import add_logo

st.set_page_config(page_title="Formação", layout="wide")

st.logo("images/crowdstrike.png", size="large")

st.sidebar.markdown("Desenvolvido por Eduardo Mazelli ®️ 2025")
col1, col2 = st.sidebar.columns([0.5, 0.5])
col1.markdown("""<a href="https://github.com/GiantMazelliWasHere"><img src="https://cdn3.emoji.gg/emojis/6705-githubblack.png" width="64px" height="64px" alt="github"></a>""", unsafe_allow_html=True)
col2.markdown("""<a href="https://www.linkedin.com/in/eduardo-mazelli/"><img src="https://cdn3.emoji.gg/emojis/70322-linkedin.png" width="64px" height="64px" alt="LinkedIn"></a>""""", unsafe_allow_html=True)

st.image("images/formacao.png", width=150)
st.title("Formação")

st.header("Publicidade e Propaganda")
st.subheader("Universidade Prebiteriana Mackenzie")
st.markdown("Janeiro de 2017 - Dezembro de 2021, SP")
st.write("Sou formado no curso de Publicidade e Propaganda pela Universidade Presbiteriana Mackenzie, onde aprendi tanto as competências para ser um profissional da área de marketing como também para a área de criação e design.")

st.header("Engenharia de Software")
st.subheader("FIAP")
st.markdown("Agosto de 2023 - Julho de 2027, SP")
st.write("Estou realizando a segunda faculdade, agora cursando engenharia de software para me capacitar como desenvolvedor full-stack e Devops. Curso na faculdade FIAP, no período matutino, onde participo de vários trabalhos curriculares e extracurriculares que me desafiam a botar tudo que aprendo em aula na prática. Curso no período matutino.")