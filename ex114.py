from utils.helper import pline, titulo
import requests

titulo('REQUISIÇÃO', 114)

try:
    site = requests.get('http://www.pudim.com')
    # Para verificar se o acesso está disponível testa o '.status_code' se a resposta é '200'
    if site.status_code == 200:
        print('Consegui acessar o site PUDIM com sucesso!')
        # Se quiser retornar o acesso em HTML(normalmente) usa-se o '.text'
        # print(site.text)

# Se quiser testar o motivo pelo qual o site não conseguiu ser acessado, usa-se o 'requests.exceptions.RequestException'
# Nessa caso retorna a inacessibilidade do porque não acessou
except requests.exceptions.ConnectionError:
    print(f'O site PUDIM não está disponível no momento.')
