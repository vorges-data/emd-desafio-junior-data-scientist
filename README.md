# Desafio Técnico - Cientista de Dados Júnior

## Descrição do Projeto

Este projeto é um dashboard interativo desenvolvido como parte de um desafio técnico para a posição de Cientista de Dados Júnior na Prefeitura da Cidade do Rio de Janeiro. O dashboard permite a visualização de dados relacionados a chamados abertos na cidade e a análise climática utilizando dados de uma API meteorológica.

## Funcionalidades

- **Análise de Chamados:** Visualizações baseadas em dados extraídos do BigQuery usando a biblioteca `basedosdados`.
- **Análise Climática:** Visualizações baseadas em dados meteorológicos obtidos via API.
- **Dashboard Interativo:** Implementado utilizando Streamlit, permitindo uma navegação fácil entre as diferentes análises.

## Requisitos

- **Python 3.8 ou superior**
- **Poetry** para gerenciamento de dependências

## Como Rodar o Projeto Localmente

### 1. Clone este Repositório

Primeiro, você precisa clonar o repositório para sua máquina local. Abra o terminal e execute o seguinte comando:

```bash
git clone https://github.com/vorges-data/emd-desafio-junior-data-scientist.git
```

### 2. Navegue para o Diretório do Projeto
Entre no diretório do projeto clonado:
```bash
cd emd-desafio-junior-data-scientist
```

### 3. Configure os Ambientes Virtuais com Poetry
#### Ambiente 1: Para basedosdados
Este ambiente é dedicado ao uso da biblioteca basedosdados para extrair dados do BigQuery. Devido à incompatibilidade de versões entre basedosdados e streamlit.

1. Instale as dependências do Poetry para basedosdados:
```bash
poetry install
```

2. Ative o ambiente virtual criado pelo Poetry:
```bash
poetry shell
```

3. Execute os scripts necessários para extrair os dados do BigQuery.

#### Ambiente 2: Para streamlit
Este ambiente é dedicado ao Streamlit e outras bibliotecas necessárias para o dashboard.

1. Volte ao diretório raiz do projeto:
```bash
cd ../../
```

2. Navegue para o diretório do Streamlit:
```bash
cd streamlit-env
```

3. Instale as dependências do Poetry para Streamlit:
```bash
poetry install
```

4. Ative o ambiente virtual criado pelo Poetry:
```bash
poetry shell
```

### 4. Rode o Dashboard
Com o ambiente virtual para Streamlit ativado, você pode rodar o dashboard usando o comando:
```bash
streamlit run Home.py
```

### Estrutura do Projeto
```bash

├── dados/                      # Diretório para arquivos CSV
├── extraction/                 # Diretório para scripts de extração de dados
│   ├── api-data/               # Scripts relacionados à API
│   └── bigquery/               # Scripts relacionados ao BigQuery
├── pages/                      # Diretório para diferentes páginas do Streamlit
├── streamlit-env/              # Arquivos relacionados ao ambiente Streamlit
├── Home.py                     # Página principal do Streamlit
├── README.md                   # Este arquivo README
└── pyproject.toml              # Arquivo de configuração das dependências
```

### Autor
Este projeto foi desenvolvido por Vinicius Borges como parte de um desafio técnico para a posição de Cientista de Dados Júnior.

