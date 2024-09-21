import time
from time import sleep
from random import randint
from operator import itemgetter
from colorama import Fore

print(f'{"DESAFIO 91":=^40}')
print(f'{Fore.GREEN}{"JOGO DE DADOS":^40}{Fore.RESET}')
print(f'{"="*40:^40}')

def myfunc(jogador):
    if type(jogador) != int:
        return jogador['valor']
    else:
        return jogador

# jogadores = list()
# jogador_vez = dict()
#
# print(f'{Fore.CYAN}{"Valores sorteados...":^40}{Fore.RESET}')
# for j in range(0, 4):
#     jogador_vez['nome'] = 'Jogador' + str(j+1)
#     jogador_vez['valor'] = randint(1, 6)
#     jogadores.append(jogador_vez.copy())
#     # jogadores.append({'nome': 'Jogador' + str(j+1), 'valor': randint(1, 6)})
#
# for jogador in jogadores:
#     # Ex.: jogador -> {'nome': 'Jogador' + str(j+1), 'valor': randint(1, 6)}
#     time.sleep(1)
#     print(f'{" ":13}{jogador["nome"]} → {jogador["valor"]}')
#
# print('-' * 40)
# print(f'{Fore.CYAN}{"Ranking dos Jogadores":^40}{Fore.RESET}')
# jogadores.sort(key=myfunc, reverse=True)
# # jogadores.sort(key=lambda x: x['valor'], reverse=True)
# print(jogadores)

jogo = {'Jogador1': randint(1, 6), 'Jogador2': randint(1, 6),
        'Jogador3': randint(1, 6), 'Jogador4': randint(1, 6)}
ranking = list()

print(f'{Fore.CYAN}{"Valores sorteados...":^40}{Fore.RESET}')
for chave, valor in jogo.items():
    time.sleep(1)
    print(f'{chave} → {valor}')

# Nesse momento faz-se um sorted() (para ordenar o dicionário jogo) por ordem da key pegando o item na posição [1]
# que seria o valor randomico que foi feito. Se passasse a posição 0 seria a chave do dict().
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print(f'{Fore.CYAN}{"Ranking dos Jogadores":^40}{Fore.RESET}')
for item, valor in enumerate(ranking):
    time.sleep(1)
    print(f'{item + 1}º lugar: {valor[0]} → {valor[1]}')



