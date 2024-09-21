from colorama import Fore
from utils.helper import pline

print(f'{"DESAFIO 95":=^40}')
print(f'{Fore.GREEN}{"JOGADOR DE FUTEBOL 2.0":^40}{Fore.RESET}')
print(f'{"="*40:^40}')

lista_jogadores = list()
jogador = dict()
tot_gols = 0


while True:
    jogador['Nome'] = str.title(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    jogador['Gols'] = []
    jogador['Total Gols'] = 0
    for jogo in range(0, partidas):
        gols = int(input(f'Quants gols na {jogo + 1}ª partida? '))
        jogador['Total Gols'] += gols
        jogador['Gols'].append(gols)
    lista_jogadores.append(jogador.copy())
    resp = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
    print('-' * 40)

print('=' * 40)
print(f'{Fore.GREEN}{"Cod":^3} | {"Nome":^10} | {"Gols":^13} | {"Total":^5}{Fore.RESET}')
print('-' * 40)
for item, jogador in enumerate(lista_jogadores):
    print(f'{item + 1:^4}| {jogador["Nome"]:^10} | {str(jogador["Gols"]):^13} | {jogador["Total Gols"]:^5}')

print('=' * 40)
while True:
    perg = int(input(f'Deseja ver os dados de qual jogador {Fore.BLUE}[999 interrompe]{Fore.RESET}:  '))
    if perg == 999:
        break
    elif 0 <= perg or perg > len(lista_jogadores):
        print(f'{Fore.RED}ERRO. Não existe jogador com o código {perg}. Tente novamente...{Fore.RESET}')
    else:
        jogador_escolhido = lista_jogadores[perg - 1]
        print(f'Levantamento de jogador {jogador_escolhido["Nome"]}')
        if jogador_escolhido in lista_jogadores:
            for indice, gol in enumerate(jogador_escolhido['Gols']):
                print(f'{" ":^4}Na {Fore.BLUE}{indice + 1}ª partida{Fore.RESET} fez {gol} gols.')

print(f'{Fore.CYAN}{"PROGRAMA ENCERRADO!":^40}{Fore.RESET}')
