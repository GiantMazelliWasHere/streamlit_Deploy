import streamlit as st
import pandas as pd
import numpy as np
from streamlit_extras.app_logo import add_logo

st.set_page_config(page_title="Skills", layout="wide")

st.logo("images/crowdstrike.png", size="large")

st.sidebar.markdown("Desenvolvido por Eduardo Mazelli ®️ 2025")
col1, col2 = st.sidebar.columns([0.5, 0.5])
col1.markdown("""<a href="https://github.com/GiantMazelliWasHere"><img src="https://cdn3.emoji.gg/emojis/6705-githubblack.png" width="64px" height="64px" alt="github"></a>""", unsafe_allow_html=True)
col2.markdown("""<a href="https://www.linkedin.com/in/eduardo-mazelli/"><img src="https://cdn3.emoji.gg/emojis/70322-linkedin.png" width="64px" height="64px" alt="LinkedIn"></a>""""", unsafe_allow_html=True)

st.image("images/skill.png", width=150)
st.title("Skills")

col1, col2 = st.columns([0.5, 0.5])

col1.header("Soft Skills:")
col1.write("- Trabalho em Grupo;")
col1.write("- Gerenciamento do Tempo;")
col1.write("- Trabalho Sobre Pressão.")

col2.header("Hard Skills:")
col2.write("- Python;")
col2.write("- Java;")
col2.write("- Pacote Office;")
col2.write("- Pacote Google Docs.")

st.title("Línguas")
st.write("- Português, Língua Mãe;")
st.write("- Inglês, Fluente;")
st.write("- Alemão, Básico;")
st.write("- Japônes, Básico.")