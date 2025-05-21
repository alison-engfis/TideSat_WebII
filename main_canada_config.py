'''
Arquivo que contém todas as informações consideradas constantes
para o funcionamento do fluxo da lógica do script main-canada.py

'''

################# FUSO PADRÃO #################
TIMEZONE_PADRAO_CANADA = "Canada/Atlantic"

################# CONFIGURAÇÕES #################
ESTACOES_CANADA = {
    "EST1": {
        "descricao": "EST1 - Rio Taquari (Foz do Boa Vista)",
        "url": "https://app.tidesatglobal.com/est1/est1_out.csv",
        "coord": [-29.471768, -51.956703],
        "descricao_imagem": "Estação EST1 - Porto de Estrela",
        "caminho_imagem": "",
        "cota_alerta": 17.00,
        "cota_inundacao": 19.00
    }
        
}

ESTACAO_PADRAO_CANADA = "EST1"