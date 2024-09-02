import streamlit as st
from PIL import Image

# Configuração da página
st.set_page_config(page_title='Desafio Técnico DS', page_icon='📊')

# Exibir imagem no sidebar
image = Image.open('marca_pessoal.png')
st.sidebar.image(image, width=120)

# Informações no sidebar
st.sidebar.markdown('# Escritório de Dados')
st.sidebar.markdown('## Prefeitura da Cidade do Rio de Janeiro')
st.sidebar.markdown("""---""")
st.sidebar.write('**Desafio Técnico** - Cientista de Dados Júnior')
st.sidebar.markdown("""---""")
st.sidebar.write('Vinicius Borges')

# Título da página principal
st.title('Desafio Técnico - Cientista de Dados')

# Seções de explicação
st.markdown("""
### Bem-vindo ao Desafio Técnico!

Este desafio foi desenvolvido para avaliar as habilidades de um Cientista de Dados Júnior, focando em análise de dados, visualização e manipulação de dados usando APIs e bancos de dados. O desafio está dividido em duas partes principais:

1. **Análise de Dados do BigQuery**: Explorando e visualizando dados relacionados aos chamados abertos na cidade do Rio de Janeiro.
2. **Análise Climática com Dados de API**: Investigando condições climáticas e tendências através de uma API de dados meteorológicos.

Use a barra lateral para navegar entre as diferentes análises e visualizações.

### Objetivos do Desafio:
- Demonstrar habilidades de manipulação de dados usando Python.
- Criar visualizações interativas e informativas para ajudar na tomada de decisões.
- Integrar dados de diferentes fontes (BigQuery e API) em um dashboard coeso.

### Estrutura do Dashboard:
- **Análise de Chamados**: Visualizações baseadas em dados do BigQuery.
- **Análise Climática**: Visualizações baseadas em dados obtidos via API.

Explore as seções e veja como diferentes técnicas de análise e visualização foram aplicadas para resolver problemas reais.
""")

# Botão de navegação para as seções do dashboard
st.markdown("## Navegação")
st.markdown("Use os botões abaixo para acessar diretamente as seções do dashboard:")

# Botões para navegação
col1, col2 = st.columns(2)
with col1:
    if st.button('Ir para Análise de Chamados'):
        st.write("Navegue para a seção de análise de chamados usando a barra lateral.")
with col2:
    if st.button('Ir para Análise Climática'):
        st.write("Navegue para a seção de análise climática usando a barra lateral.")

# Footer
st.markdown("""---""")
st.write("Desenvolvido por Vinicius Borges como parte do Desafio Técnico para Cientista de Dados Júnior.")
st.write("Escritório de Dados, Prefeitura da Cidade do Rio de Janeiro.")
