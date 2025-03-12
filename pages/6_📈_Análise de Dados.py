import streamlit as st
import pandas as pd
import numpy as np
import scipy.stats as stats
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
from plotnine import *
import statistics as sta

def variancia(media, dados):
    return sum((x - media) ** 2 for x in dados) / len(dados) 

def plot_distribution(x, y, title, xlabel, ylabel):
    fig = go.Figure(data=[go.Bar(x=x, y=y)])
    fig.update_layout(title=title, xaxis_title=xlabel, yaxis_title=ylabel)
    st.plotly_chart(fig)
    
with open("pdfs/relatorio_crowdstrike.pdf", "rb") as file:
    crowdstrike_pdf = file.read()
    
with open("pdfs/relatorio_itu.pdf", "rb") as file:
    itu_pdf = file.read()

ataques = pd.read_csv("databases/Ataques de Identidade e Explorações de Vulnerabilidades por Mês no Ano de 2024.csv")
vishing = pd.read_csv("databases/Campanhas de Vishing.csv")
ict = pd.read_csv("databases/ICT regulator have a cybersecurity mandate.csv")
leis = pd.read_csv("databases/Cybersecurity legislation_regulation exist.csv")

st.set_page_config(page_title="Análise de Dados", layout="wide")

st.logo("images/crowdstrike.png")

st.sidebar.markdown("Desenvolvido por Eduardo Mazelli ®️ 2025")
col1, col2 = st.sidebar.columns([0.5, 0.5])
col1.markdown("""<a href="https://github.com/GiantMazelliWasHere"><img src="https://cdn3.emoji.gg/emojis/6705-githubblack.png" width="64px" height="64px" alt="github"></a>""", unsafe_allow_html=True)
col2.markdown("""<a href="https://www.linkedin.com/in/eduardo-mazelli/"><img src="https://cdn3.emoji.gg/emojis/70322-linkedin.png" width="64px" height="64px" alt="LinkedIn"></a>""""", unsafe_allow_html=True)

st.image("images/estatistica.png", width=150)

st.title("Análise de Dados")

st.write("Nesta seção irei fazer uma breve análise de alguns dados relacionados a área de cybersecurity. Tirados de um relatório feito pela Crowdstrike, uma empresa de segurança cibernética e da ITU (International Telecommunication Union), uma agência especializada em tecnologia da informação e comunicação das Nações Unidas.")

pages = st.selectbox("Selecione a análise:", [
    "Ataques de Identidade e Explorações de Vulnerabilidades por Mês no Ano de 2024", 
    "Campanhas de Vishing", 
    "Relatório de Proteção do ITU", 
    "Relatório de Legislação do ITU"])

if pages == "Ataques de Identidade e Explorações de Vulnerabilidades por Mês no Ano de 2024":
    
    st.header("Ataques de Identidade e Explorações de Vulnerabilidades por Mês no Ano de 2024")
    
    st.write("Nesse primeiro conjunto de dados temos o levantamento de dados feito pela Crowdstrike que nos mostra quantos ataques e explorações houveram em 2024, isso separando elas por mês.")
    st.table(ataques)
    st.write("Nesse conjuto de dados temos váriaveis do tipo qualitativas nomiais: os meses do ano e quantitativas discretas: a quantidade de ataques e explorações.")
    
    st.subheader("Perguntas:")
    st.write("1. Qual é a tendência dos ataques?")
    st.write("2. Qual foi o mês com mais ataques e explorações em 2024?")
    st.write("3. Podemos usar essa média com uma dado que posso nos ajudar para futuras proteções?")
    
    st.header("Gráficos de Medidas de Tendência Central")
    
    media_ataques = round(ataques["Quantidade de Ataques"].mean())
    median_ataques = round(ataques["Quantidade de Ataques"].median())
    moda_ataques = round(sta.mode(ataques["Quantidade de Ataques"]))
    padrao_ataques = round(np.std(ataques["Quantidade de Ataques"]))
    variancia_ataques = variancia(media_ataques, ataques["Quantidade de Ataques"])

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=ataques["Mês"], y=ataques["Quantidade de Ataques"], mode='lines+markers', name='Quantidade de Ataques'))
    fig.add_trace(go.Scatter(x=ataques["Mês"], y=[media_ataques]*len(ataques), mode='lines', name='Média', line=dict(dash='dash')))
    fig.add_trace(go.Scatter(x=ataques["Mês"], y=[median_ataques]*len(ataques), mode='lines', name='Mediana', line=dict(dash='dot')))
    fig.add_trace(go.Scatter(x=ataques["Mês"], y=[moda_ataques]*len(ataques), mode='lines', name='Moda', line=dict(dash='dashdot')))
    fig.update_layout(title="Ataques de Identidade e Explorações de Vulnerabilidades - Média, Mediana e Moda", xaxis_title="Mês", yaxis_title="Quantidade de Ataques")
    st.plotly_chart(fig)
    
    st.write(f"Podemos ver que a media e a mediana se encontram muito perto, com uma diferença de {media_ataques - median_ataques}. Ou seja, temos um meio e uma medida média muito alinhadas. Porem nossa moda se encontra muito fora d padrão, o que nos mostra que em maioria nossa data base deve ser formada de dados altos que se encontram fora do padrão da mediana.")

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=ataques["Mês"], y=ataques["Quantidade de Ataques"], mode='lines+markers', name='Quantidade de Ataques'))
    fig.add_trace(go.Scatter(x=ataques["Mês"], y=[padrao_ataques]*len(ataques), mode='lines', name='Desvio Padrão', line=dict(dash='dash')))
    fig.add_trace(go.Scatter(x=ataques["Mês"], y=[variancia_ataques]*len(ataques), mode='lines', name='Variância', line=dict(dash='dot')))
    fig.update_layout(title="Ataques de Identidade e Explorações de Vulnerabilidades - Desvio Padrão e Variância", xaxis_title="Mês", yaxis_title="Quantidade de Ataques")
    st.plotly_chart(fig)
    
    st.write("Com esses dados adiquiridos podemos analisar que os dados do relátorio estão muito dispersos e espalhados em relação a média. O que nos mostra que a média não é um bom indicador para esses dados, pois ela não representa bem a tendência dos dados, já que eles alem de estarem dispersos do centro, estão també espalhados dele.")
    
    st.header("Gráficos de Distribuição")
    st.subheader("Distribuição Normal:")
    
    media = media_ataques
    std = padrao_ataques
    x = np.linspace(media - 4*std, media + 4*std, 100)
    y = stats.norm.pdf(x, media, std)
    y_cdf = stats.norm.cdf(x, media, std)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='PDF'))
    fig.update_layout(title="Distribuição Normal", xaxis_title="Valores", yaxis_title="Densidade de Probabilidade")
    st.plotly_chart(fig)
    
    st.write("Usamos uma distribuição normal pois queriamos ver como era a distribuição de dados em como os ataques se comportavam durante o ano de 2024.")
    st.write("Podemos ver que a distribuição é bem simétrica e que a maior parte dos dados se encontram perto da média, o que entra em cotradição com o que foi previamente descoberto pois nos mostra que a média é um bom indicador para esses dados.")
    
    st.markdown("### Referências:")
    st.download_button(label = "Global Threat Report 2025", data = crowdstrike_pdf, file_name= "Global Threat Report 2025.pdf", mime="application/pdf", icon=":material/download:",)
        
elif pages == "Campanhas de Vishing":
    
    st.header("Campanhas de Vishing")
    
    st.write("Neste segundo ainda temos dados do mesmo relatório da Crowdstrike. Porém aqui podemos ver a quantidade de campanhas de Vishing realizadas no ano de 2024.")
    st.table(vishing)
    st.write("Nesse conjuto de dados temos váriaveis do tipo qualitativas nomiais: os meses do ano e quantitativas discretas: a quantidade de campanhas de Vishing.")
    
    st.subheader("Perguntas:")
    st.write("1. Qual é a tendência das campanhas de Vishing?")
    st.write("2. Quais meses podemos prever um maior número de vishing para nos protegermos mais?")
    
    st.header("Gráficos de Medidas de Tendência Central")
    
    media_campanha = round(vishing["Quantidade de Campanhas"].mean())
    median_campanha = round(vishing["Quantidade de Campanhas"].median())
    moda_campanha = round(sta.mode(vishing["Quantidade de Campanhas"]))
    padrao_campanha = round(np.std(vishing["Quantidade de Campanhas"]))
    variancia_campanha = round(variancia(media_campanha, vishing["Quantidade de Campanhas"]),2)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=vishing["Mês"], y=vishing["Quantidade de Campanhas"], mode='lines+markers', name='Quantidade de Campanhas'))
    fig.add_trace(go.Scatter(x=vishing["Mês"], y=[media_campanha]*len(vishing), mode='lines', name='Média', line=dict(dash='dash')))
    fig.add_trace(go.Scatter(x=vishing["Mês"], y=[median_campanha]*len(vishing), mode='lines', name='Mediana', line=dict(dash='dot')))
    fig.add_trace(go.Scatter(x=vishing["Mês"], y=[moda_campanha]*len(vishing), mode='lines', name='Moda', line=dict(dash='dashdot')))
    fig.update_layout(title="Campanhas de Vishing - Média, Mediana e Moda", xaxis_title="Mês", yaxis_title="Quantidade de Campanhas")
    st.plotly_chart(fig)

    st.write(f"Neste caso vemos uma diferença interessante com os nossos dados. Podemos ver que a mediana e a moda são os mesmos, o que mostra que nossa mediana está dentro da tendencia dos números que mais aparecem, e assim não deve ser um numero fora do padrão, devemos ter uma lista de números mais focados nesse padrão. Já média escapa desse número tendo uma diferença de {media_campanha - moda_campanha} com a moda e {media_campanha - median_campanha} com a mediana e isso pode nos informar que nossos dados possuem uma grande variedade de dados.")

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=vishing["Mês"], y=vishing["Quantidade de Campanhas"], mode='lines+markers', name='Quantidade de Campanhas'))
    fig.add_trace(go.Scatter(x=vishing["Mês"], y=[padrao_campanha]*len(vishing), mode='lines', name='Desvio Padrão', line=dict(dash='dash')))
    fig.add_trace(go.Scatter(x=vishing["Mês"], y=[variancia_campanha]*len(vishing), mode='lines', name='Variância', line=dict(dash='dot')))
    fig.update_layout(title="Campanhas de Vishing - Desvio Padrão e Variância", xaxis_title="Mês", yaxis_title="Quantidade de Campanhas")
    st.plotly_chart(fig)
    
    st.write("Podemos analisar que os dados estão muito dispersos, porém pouco espalhados. Tronando a média um bom indicador para esses dados já que eles não dispersão do centro apenas se esplaham em volta dele.")
    
    st.header("Gráficos de Distribuição")
    st.subheader("Distribuição Poisson:")
    media_campanha = round(vishing["Quantidade de Campanhas"].mean())
    x_max = st.number_input("Número de eventos desejado", min_value=0, step=1, value=12)
    
    x = np.arange(0, x_max + 1)
    y = stats.poisson.pmf(x, media_campanha)
    
    fig = go.Figure(data=[go.Bar(x=x, y=y)])
    fig.update_layout(title="Distribuição de Poisson", xaxis_title="Número de eventos", yaxis_title="Probabilidade")
    st.plotly_chart(fig)
    
    st.write("Usamos uma distribuição de Poisson pois se tratar de um evento mais fechado, se tratando de um tipo específico de ataque.")
    st.write("Podemos ver que a probabilidade de termos 0 campanhas de Vishing é de 0.0001, o que nos mostra que é muito improvável que não tenhamos nenhuma campanha de Vishing em um mês. Porém ela se regulariza em torno de 24, 25 ou seja é provavel que tenhamos em torno de 25 campanhas de Vishing em um mês.")
    
    st.markdown("### Referências:")
    st.download_button(label = "Global Threat Report 2025", data = crowdstrike_pdf, file_name= "Global Threat Report 2025.pdf", mime="application/pdf", icon=":material/download:",)
    
elif pages == "Relatório de Proteção do ITU":

    st.subheader("Relatório de Proteção do ITU:")
    st.write("Nesta tabela podemos analisar quais países da américa do sul possuem algum tipo de proteção sobre as informações e comunicação no âmbito tecnológico.")
    st.table(ict)
    st.write("Neste conjunto de dados temos váriaveis apenas do tipo qualitativas nominais: os países da américa do sul e se eles possuem ou não alguma proteção.")

    st.subheader("Perguntas:")
    st.write("1. Quais países da américa do sul possuem proteção sobre as informações e comunicação no âmbito tecnológico?")
    st.write("2. Qual é a porcentagem de países que possuem proteção?")
    st.write("3. Qual é a porcentagem de países que não possuem proteção?")
    st.write("4. Na questão turística, quais países devemos tomar cuidado ao usar a tecnologia por não possuir nenhuma proteção?")
    
    st.header("Gráficos de Distribuição")
    st.subheader("Distribuição Binomial:")
    
    n = len(ict)
    k = ict["Status"].apply(lambda x: 1 if x == "Yes" else 0).sum()
    p = k / n
    
    st.write("Número de ensaios (n):", n)
    st.write("Número de sucessos (k):", k)
    st.write("Probabilidade de sucesso (p):", round(p, 2))
    
    x = np.arange(0, n + 1)
    y = stats.binom.pmf(x, n, p)
    df_binomial = pd.DataFrame({"X": x, "P(X)": y, "P(X ≤ k) (Acumulado)": np.cumsum(y)}).set_index("X")
    
    tabela = st.checkbox("Tabela de probabilidades")
    if tabela:
        st.write("Tabela de probabilidades:")
        st.write(df_binomial)
    plot_distribution(x, y, "Distribuição Binomial", "Número de sucessos", "Probabilidade")
    
    st.write("Usamos uma distribuição binomial pois queriamos ver como era a distribuição de dados em como os países se comportavam em relação a proteção de informações e comunicação no âmbito tecnológico.")
    st.write("Podemos ver que a probabilidade de termos 0 países com proteção é de 0.0001, o que nos mostra que é muito improvável que não tenhamos nenhum país com proteção. Porém ela se regulariza em torno de 5, 6 ou seja é provavel que tenhamos em torno de 6 países com proteção. E isso nos mostra que num continente com 12 países, a metade dele ainda pode estar desprotegido.")
    
    st.markdown("### Referências:")
    st.download_button(label = "Global Cybersecurity Index 2024", data = itu_pdf, file_name= "Global Cybersecurity Index 2024.pdf", mime="application/pdf", icon=":material/download:",)

elif pages == "Relatório de Legislação do ITU":
    
    st.subheader("Relatório de Legislação do ITU:")

    st.write("Nesta segunda tabela analisamos quais países da américa do sul possuem algum tipo de legislação ou regulamentação sobre a segurança cibernética.")
    st.table(leis)
    st.write("Neste conjunto de dados temos váriaveis apenas do tipo qualitativas nominais: os países da américa do sul e se eles possuem ou não alguma legislação ou regulamentação.")

    st.subheader("Perguntas:")
    st.write("1. Quais países da américa do sul possuem legislação ou regulamentação sobre a segurança cibernética?")
    st.write("2. Qual é a porcentagem de países que possuem legislação ou regulamentação?")
    st.write("3. Qual é a porcentagem de países que não possuem legislação ou regulamentação?")
    
    st.header("Gráficos de Distribuição")
    st.subheader("Distribuição Binomial:")
    
    n = len(leis)
    k = ict["Status"].apply(lambda x: 1 if x == "Yes" else 0).sum()
    p = k / n
    
    st.write("Número de ensaios (n):", n)
    st.write("Número de sucessos (k):", k)
    st.write("Probabilidade de sucesso (p):", round(p, 2))
    
    x = np.arange(0, n + 1)
    y = stats.binom.pmf(x, n, p)
    df_binomial = pd.DataFrame({"X": x, "P(X)": y, "P(X ≤ k) (Acumulado)": np.cumsum(y)}).set_index("X")
    
    tabela = st.checkbox("Tabela de probabilidades")
    if tabela:
        st.write("Tabela de probabilidades:")
        st.write(df_binomial)
    plot_distribution(x, y, "Distribuição Binomial", "Número de sucessos", "Probabilidade")
    
    st.write("Usamos uma distribuição binomial pois queriamos ver como era a distribuição de dados em como os países se comportavam em relação a legislação ou regulamentação sobre a segurança cibernética.")
    st.write("Podemos ver que a probabilidade de termos 0 países com legislação ou regulamentação é de 0.0001, o que nos mostra que é muito improvável que não tenhamos nenhum país com legislação ou regulamentação. Porém ela se regulariza em torno de 5, 6 ou seja é provavel que tenhamos em torno de 6 países com legislação ou regulamentação. E isso nos mostra que metade dos países da américa do sul ainda não possuem legislação ou regulamentação sobre a segurança cibernética.")
    
    st.markdown("### Referências:")
    st.download_button(label = "Global Cybersecurity Index 2024", data = itu_pdf, file_name= "Global Cybersecurity Index 2024.pdf", mime="application/pdf", icon=":material/download:",)

