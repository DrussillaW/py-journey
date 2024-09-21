from operator import itemgetter
from colorama import Fore

print(f'{"DESAFIO 93":=^40}')
print(f'{Fore.GREEN}{"JOGADOR DE FUTEBOL":^40}{Fore.RESET}')
print(f'{"="*40:^40}')

jogador = dict()
tot_gols = 0
jogador['Nome'] = str.title(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
jogador['Gols'] = []
jogador['Total Gols'] = 0
for jogo in range(0, partidas):
    gols = int(input(f' - Quants gols na {jogo + 1}ª partida? '))
    jogador['Total Gols'] += gols
    jogador['Gols'].append(gols)

print(f'{"="*40:^40}')
print(jogador)
print(f'{"="*40:^40}')

for chave, valor in jogador.items():
    print(f'O campo {Fore.BLUE}{chave}{Fore.RESET} tem valor {Fore.BLUE}{valor}{Fore.RESET}.')
print(f'{"="*40:^40}')

print(f'{Fore.BLUE}O jogador {jogador["Nome"]} jogou {partidas} partidas.{Fore.RESET}')
for indice, gol in enumerate(jogador['Gols']):
    print(f'{" ":^4}Na {Fore.BLUE}{indice + 1}ª partida{Fore.RESET} fez {gol} gols.')
print(f'Fez um total de {Fore.BLUE}[{jogador["Total Gols"]}]{Fore.RESET} gols.')


