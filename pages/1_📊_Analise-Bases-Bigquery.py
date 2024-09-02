import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Função para carregar dados
def load_data(filename):
    return pd.read_csv(f'dados/{filename}')

# Título do aplicativo
st.title("Dashboard de Análise de Chamados e Clima")

# Sidebar para selecionar o dataset
dataset = st.sidebar.selectbox(
    "Selecione o conjunto de dados",
    ["Total de Chamados", "Tipo de Chamados", "Bairros com Mais Chamados", 
     "Subprefeitura com Mais Chamados", "Chamados Sem Associação", 
     "Média Diária por Evento", "Distribuição de Tipos de Chamados", 
     "Comparação de Eventos"]
)

# Condicional para exibir o gráfico com base na seleção do usuário
if dataset == "Total de Chamados":
    df = load_data('total_chamados_01042023.csv')
    st.subheader("Total de Chamados no mês de Abril 2023")
    st.metric(label="Total de Chamados", value=int(df['total_chamados'].sum()))

elif dataset == "Tipo de Chamados":
    df = load_data('tipo_chamados_01042023.csv')
    st.subheader("Tipo de Chamados em 01/04/2023")
    fig, ax = plt.subplots()
    df.set_index('tipo_situacao').plot(kind='barh', stacked=True, ax=ax, color=['#1f77b4', '#ff7f0e', '#2ca02c'])
    ax.set_xlabel("Total de Chamados")
    ax.set_ylabel("Tipo de Situação")
    st.pyplot(fig)

elif dataset == "Bairros com Mais Chamados":
    df = load_data('bairros_mais_chamados_01042023.csv')
    st.subheader("Bairros com Mais Chamados em 01/04/2023")
    st.bar_chart(df.set_index('bairro'))

elif dataset == "Subprefeitura com Mais Chamados":
    df = load_data('subprefeitura_mais_chamados_01042023.csv')
    st.subheader("Subprefeitura com Mais Chamados em 01/04/2023")
    st.bar_chart(df.set_index('subprefeitura'))

elif dataset == "Chamados Sem Associação":
    df = load_data('chamados_sem_associacao_01042023.csv')
    st.subheader("Chamados Sem Associação em 01/04/2023")
    st.dataframe(df)

elif dataset == "Média Diária por Evento":
    df = load_data('media_diaria_eventos.csv')
    st.subheader("Média Diária de Chamados por Evento")
    fig, ax = plt.subplots()
    df.set_index('evento').plot(kind='line', ax=ax, color='#1f77b4', linewidth=2.5)
    ax.fill_between(df['evento'], df['media_diaria'], color='#1f77b4', alpha=0.3)
    ax.set_ylabel("Média Diária")
    ax.set_xlabel("Evento")
    st.pyplot(fig)

elif dataset == "Distribuição de Tipos de Chamados":
    df = load_data('tipo_chamados_01042023.csv')
    st.subheader("Distribuição de Tipos de Chamados em 01/04/2023")
    fig = px.pie(df, names='tipo_situacao', values='total_chamados', title="Distribuição de Tipos de Chamados")
    st.plotly_chart(fig)

elif dataset == "Comparação de Eventos":
    df = load_data('media_diaria_eventos.csv')
    st.subheader("Comparação da Média Diária de Chamados por Evento")
    fig = px.line_polar(df, r='media_diaria', theta='evento', line_close=True)
    st.plotly_chart(fig)
