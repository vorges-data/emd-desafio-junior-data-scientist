import streamlit as st
from PIL import Image

st.set_page_config(page_title='Desafio Técnico DS', page_icon='📊')

image = Image.open('marca_pessoal.png')
st.sidebar.image(image, width = 120)

st.sidebar.markdown('# Escritório de Dados')
st.sidebar.markdown('## Prefeitura da Cidade do Rio de Janeiro')
st.sidebar.markdown("""---""")
st.sidebar.write('**Desafio Técnico** - Cientista de Dados Júnior')
st.sidebar.markdown("""---""")
st.sidebar.write('Vinicius Borges')

#=========================================================

st.title('Desafio Técnico - Cientista de Dados')

# Exemplo de uma seção expansível para mostrar código
with st.expander("Clique para ver o código SQL"):
    code = """
    SELECT *
    FROM tabela_exemplo
    WHERE coluna = 'valor';
    """
    st.code(code, language='sql')

# Exemplo de outra seção expansível para mostrar código Python
with st.expander("Clique para ver o código Python"):
    code = """
    def exemplo_funcao():
        return sum([1, 2, 3])
    """
    st.code(code, language='python')
