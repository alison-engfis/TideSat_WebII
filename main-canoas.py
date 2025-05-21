'''
Arquivo que dá início a execução do domínio tidesat-canoas.streamlit.app
e a todo o fluxo de importações dos outros arquivos em main_canoas_config.py,
levando as informações constantes pertinentes a esse script.

'''

# SITE DE CANOAS
from main_canoas_config import ESTACOES_CANOAS, ESTACAO_PADRAO_CANOAS, TIMEZONE_PADRAO
from tools import main
from language import LANG

# Define o idioma para essa instância
idioma = "pt"
lang = LANG[idioma]

estacoes_info = ESTACOES_CANOAS
estacao_padrao = ESTACAO_PADRAO_CANOAS
tz_padrao = TIMEZONE_PADRAO
logotipo = "metsul_logo.png"
html_logo = "https://metsul.com/"

main(estacoes_info, estacao_padrao, logotipo, html_logo, lang, tz_padrao)