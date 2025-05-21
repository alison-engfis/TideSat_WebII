'''
Arquivo que dá início a execução do domínio tidesat-portosrs.streamlit.app
e a todo o fluxo de importações dos outros arquivos em main_gen.py,
levando as informações constantes pertinentes a esse script.

'''

# SITE PARA PORTOSRS
from main_portosrs_config import ESTACOES_PORTOS, ESTACAO_PADRAO_PORTOS, TIMEZONE_PADRAO
from tools import main
from language import LANG

# Define o idioma para essa instância
idioma = "pt"
lang = LANG[idioma]

estacoes_info = ESTACOES_PORTOS
estacao_padrao = ESTACAO_PADRAO_PORTOS
tz_padrao = TIMEZONE_PADRAO
logotipo = "portosrs_logo.png"
html_logo = "https://www.portosrs.com.br/site/"

main(estacoes_info, estacao_padrao, logotipo, html_logo, lang, tz_padrao)