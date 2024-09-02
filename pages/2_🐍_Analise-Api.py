import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Função para carregar dados
def load_data(filename):
    return pd.read_csv(f'dados/{filename}')

# Título do aplicativo
st.title("Dashboard de Análise Climática")

# Sidebar para selecionar o dataset
dataset = st.sidebar.selectbox(
    "Selecione o conjunto de dados",
    ["Temperatura Média Mensal", "Tempo Predominante Mensal", 
     "Temperatura Média Diária", "Clima Favorável por Mês", 
     "Temperaturas Mínimas e Máximas"]
)

# Condicional para exibir o gráfico com base na seleção do usuário
if dataset == "Temperatura Média Mensal":
    df = load_data('temperatura_media_mensal.csv')
    st.subheader("Temperatura Média Mensal")
    st.line_chart(df.set_index('month')['avg_temp'])

elif dataset == "Tempo Predominante Mensal":
    df = load_data('tempo_predominante_mensal.csv')
    st.subheader("Tempo Predominante por Mês")
    st.bar_chart(df)

elif dataset == "Temperatura Média Diária":
    df_weather = load_data('weather_daily.csv')  # Suponha que você salvou os dados diários
    df_weather['date'] = pd.to_datetime(df_weather['date'])
    st.subheader("Temperatura Média Diária")
    fig, ax = plt.subplots()
    ax.plot(df_weather['date'], df_weather['avg_temp'], color='#1f77b4')
    ax.set_xlabel("Data")
    ax.set_ylabel("Temperatura Média (°C)")
    st.pyplot(fig)

elif dataset == "Clima Favorável por Mês":
    df_weather = load_data('weather_daily.csv')  # Suponha que você salvou os dados diários
    df_weather['date'] = pd.to_datetime(df_weather['date'])
    df_weather['month'] = df_weather['date'].dt.month

    # Considera clima favorável: sem chuva, claro ou parcialmente nublado (códigos 0, 1, 2)
    df_weather['clima_favoravel'] = df_weather['weathercode'].isin([0, 1, 2])
    favorable_days = df_weather.groupby('month')['clima_favoravel'].sum()

    st.subheader("Dias com Clima Favorável por Mês")
    st.bar_chart(favorable_days)

elif dataset == "Temperaturas Mínimas e Máximas":
    df_weather = load_data('weather_daily.csv')  # Suponha que você salvou os dados diários
    df_weather['date'] = pd.to_datetime(df_weather['date'])
    st.subheader("Temperaturas Mínimas e Máximas Diárias")
    fig, ax = plt.subplots()
    ax.plot(df_weather['date'], df_weather['temperature_2m_min'], label='Mínima', color='#1f77b4')
    ax.plot(df_weather['date'], df_weather['temperature_2m_max'], label='Máxima', color='#ff7f0e')
    ax.fill_between(df_weather['date'], df_weather['temperature_2m_min'], df_weather['temperature_2m_max'], color='#b0c4de', alpha=0.3)
    ax.set_xlabel("Data")
    ax.set_ylabel("Temperatura (°C)")
    ax.legend()
    st.pyplot(fig)
