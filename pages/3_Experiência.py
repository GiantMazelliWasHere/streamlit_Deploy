import streamlit as st
import pandas as pd
import numpy as np
from streamlit_extras.app_logo import add_logo

st.set_page_config(page_title="Formação e Experiências", layout="wide")

st.logo("images/crowdstrike.png")

st.sidebar.markdown("Desenvolvido por Eduardo Mazelli ®️ 2025")
col1, col2 = st.sidebar.columns([0.5, 0.5])
col1.markdown("""<a href="https://github.com/GiantMazelliWasHere"><img src="https://cdn3.emoji.gg/emojis/6705-githubblack.png" width="64px" height="64px" alt="github"></a>""", unsafe_allow_html=True)
col2.markdown("""<a href="https://www.linkedin.com/in/eduardo-mazelli/"><img src="https://cdn3.emoji.gg/emojis/70322-linkedin.png" width="64px" height="64px" alt="LinkedIn"></a>""""", unsafe_allow_html=True)

st.image("images/experiencia.png", width=150)
st.title("Experiência")

st.header("Trainee de Analista de Mídia")
st.subheader("Agência Traktor")
st.markdown("Abril de 2022 - Julho de 2022, Remoto")
st.write("Programar a postagem de stories e posts de clientes. Participação de reuniões com clientes para a apresentação de resultados e alinhamento de metas. Participar de reuniões com o time interno da agência para alinharmos o trabalho em equipe e para que pudéssemos avaliar se as metas estão sendo atingidas ou se precisamos focar nelas.")

st.header("Analista de Mídia")
st.subheader("Agência Traktor")
st.markdown("Julho de 2022 - Fevereiro de 2023, Remoto")
st.write("Analisar as mídias digitais dos clientes e realizar ajustes necessários. Criar campanhas estratégias para o atingimento das metas dos clientes, sendo um foco central para ajudar o cliente na montagem de peças e na programação de postagens para melhorar o tráfego das mídias digitais do cliente. Montar documentos expondo os resultados das metas atingidas nos períodos de tempo, apresentar esse resultado para o cliente em reuniões e realizar a ata da reunião enviando todos os documentos as partes importantes.")