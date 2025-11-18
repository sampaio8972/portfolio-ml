import streamlit as st
import pickle
import os

# Estilo moderno e minimalista via CSS customizado
st.markdown("""
<style>
    .main {background-color:#f7f7f7;}
    .reportview-container .markdown-text-container {
        font-family: 'Montserrat', sans-serif;
        color:#222;
    }
    .sidebar .sidebar-content { background-color:#232946; color:white;}
    .element-container {margin-bottom:15px;}
    h2 {color:#232946; font-weight:700;}
    .css-1v0mbdj {box-shadow: 0 2px 8px #e2e2e2;}
</style>
""", unsafe_allow_html=True)

# SIDEBAR
st.sidebar.image('assets/logo.png', width=100)
st.sidebar.title('Portfólio Cientista de Dados')
st.sidebar.markdown('---')
categoria = st.sidebar.selectbox('Selecione a categoria:', ['Classificação', 'Regressão', 'Séries Temporais'])

if categoria == 'Classificação':
    projeto = st.sidebar.radio('Projetos:', [
        'Análise de Vinhos',
        'Avaliação de Veículos',
        'Risco de Crédito'
    ])
elif categoria == 'Regressão':
    projeto = st.sidebar.radio('Projetos:', [
        'Avaliação de Residências',
        'Avaliação de Parkinson',
        'Eficiência Energética'
    ])
else:
    projeto = st.sidebar.radio('Projetos:', [
        'Análise Passagens Aéreas',
        'Ativos Financeiros',
        'Consumo Elétrico',
        'Vendas Lojas Rossmann'
    ])

# HEADER
st.title('Portfólio Machine Learning | Seu Nome')
st.markdown('Explore meus principais projetos de Data Science para Classificação, Regressão e Séries Temporais. Teste os modelos e confira as etapas de desenvolvimento.')

st.markdown("---")

def mostrar_projeto(nome, arquivo_modelo, explicacao, input_fields):
    st.header(nome)
    st.markdown(explicacao, unsafe_allow_html=True)
    st.image(f"projetos/{nome.lower().replace(' ', '_')}.png", caption=f"Fluxograma de {nome}", use_column_width=True)
    with st.expander("Etapas do Projeto"):
        st.markdown(f"- Preparação dos dados<br>- Engenharia de atributos<br>- Treinamento e Ajuste do Modelo<br>- Testes e Métricas<br>- Exportação do modelo", unsafe_allow_html=True)
    st.subheader('Teste aqui!')
    entrada = []
    for campo, detalhes in input_fields.items():
        if detalhes['tipo'] == 'number':
            valor = st.number_input(campo, detalhes['min'], detalhes['max'], detalhes.get('padrao', detalhes['min']))
        elif detalhes['tipo'] == 'slider':
            valor = st.slider(campo, detalhes['min'], detalhes['max'], detalhes.get('padrao', detalhes['min']))
        entrada.append(valor)
    if st.button('Executar Teste do Modelo'):
        path_modelo = os.path.join('modelos', arquivo_modelo)
        with open(path_modelo, 'rb') as file:
            modelo = pickle.load(file)
        resultado = modelo.predict([entrada])
        st.success(f'Resultado: {resultado}')

# Exemplos de input para cada projeto (personalize conforme variáveis reais dos seus modelos)
explicacoes = {
    'Análise de Vinhos': 'Classificação da qualidade de vinhos portugueses usando atributos físico-químicos.',
    'Avaliação de Veículos': 'Classificação de avaliação de veículos para venda, considerando preço, ano e condição.',
    'Risco de Crédito': 'Modelo preditivo de concessão de crédito a partir de informações financeiras do cliente.',
    'Avaliação de Residências': 'Regressão para estimar o valor de casas usando variáveis como metragem, quartos e localização.',
    'Avaliação de Parkinson': 'Regressão para identificar padrões no progresso da doença.',
    'Eficiência Energética': 'Prevendo consumo energético com base em características construtivas.',
    'Análise Passagens Aéreas': 'Previsão de demanda de passagens por série temporal.',
    'Ativos Financeiros': 'Modelagem para previsão de preços de ativos usando series históricas.',
    'Consumo Elétrico': 'Predição do consumo elétrico residencial ao longo do tempo.',
    'Vendas Lojas Rossmann': 'Previsão de vendas em lojas usando dados temporais e externos.'
}

inputs_projetos = {
    'Análise de Vinhos': {'Álcool': {'tipo':'number','min':8,'max':15}, 'Acidez': {'tipo':'number','min':2.5,'max':5.5}},
    'Avaliação de Veículos': {'Ano': {'tipo':'number','min':1990,'max':2025}, 'Km rodados': {'tipo':'number','min':0,'max':400000}},
    'Risco de Crédito': {'Renda Mensal': {'tipo':'number','min':1000,'max':20000}, 'Idade': {'tipo':'slider','min':18,'max':80}},
    'Avaliação de Residências': {'Área (m²)': {'tipo':'number','min':30,'max':900}, 'Dormitórios': {'tipo':'slider','min':1,'max':10}},
    'Avaliação de Parkinson': {'UPDRS': {'tipo':'number','min':0,'max':100}, 'Idade': {'tipo':'slider','min':20,'max':80}},
    'Eficiência Energética': {'Área': {'tipo':'number','min':20,'max':400}, 'Isolamento': {'tipo':'slider','min':0,'max':5}},
    'Análise Passagens Aéreas': {'Ano': {'tipo':'number','min':2000,'max':2025}, 'Período': {'tipo':'slider','min':1,'max':12}},
    'Ativos Financeiros': {'Preço Atual': {'tipo':'number','min':1,'max':500}, 'Dias': {'tipo':'slider','min':1,'max':365}},
    'Consumo Elétrico': {'Mês': {'tipo':'slider','min':1,'max':12}, 'Dias': {'tipo':'slider','min':1,'max':31}},
    'Vendas Lojas Rossmann': {'Loja': {'tipo':'number','min':1,'max':2000}, 'Dia': {'tipo':'slider','min':1,'max':31}}
}

mostrar_projeto(projeto, projeto.lower().replace(' ', '_')+'.pkl', explicacoes[projeto], inputs_projetos[projeto])

st.markdown('---')
st.markdown('<span style="color:#232946;font-size:16px;">Desenvolvido por Seu Nome | [LinkedIn](https://linkedin.com/in/seuusuario)</span>', unsafe_allow_html=True)
