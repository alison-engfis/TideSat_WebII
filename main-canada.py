'''
Arquivo que dá início a execução do domínio tidesat-fundy.app
e a todo o fluxo de importações dos outros arquivos em main_canada_config.py,
levando as informações constantes pertinentes a esse script.

'''


from main_canada_config import ESTACOES_CANADA, ESTACAO_PADRAO_CANADA, TIMEZONE_PADRAO_CANADA
from tools import main
from language import LANG

# Define o idioma para essa instância
idioma = "en"
lang = LANG[idioma]

estacoes_info = ESTACOES_CANADA
estacao_padrao = ESTACAO_PADRAO_CANADA
tz_padrao = TIMEZONE_PADRAO_CANADA
logotipo = "TideSat_logo.webp"
html_logo = "https://www.tidesatglobal.com/"

main(estacoes_info, estacao_padrao, logotipo, html_logo, lang, tz_padrao)