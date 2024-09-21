from utils.helper import titulo, pline

titulo('FICHA DO JOGADOR', 103)


def ficha(nome=None, gols=None):
    from colorama import Fore
    if nome is None:
        nome = '<desconhecido>'
    if gols is None:
        gols = 0
    print(f'O nome do jogador é {Fore.GREEN}{nome}{Fore.RESET} e ele fez {Fore.GREEN}{gols}{Fore.RESET} gols.')


# Programa Principal
name = str(input('Nome do jogador: ')).title()
num_gols = str(input('Número de gols: '))
pline()
if num_gols.isnumeric():
    num_gols = int(num_gols)
else:
    num_gols = 0
if name.strip() == '':
    ficha(gols=num_gols)
else:
    ficha(name, num_gols)
pline()
