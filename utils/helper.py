from colorama import Fore


def titulo(texto, exercicio):
    print(f'{"DESAFIO " + str(exercicio):=^40}')
    print(f'{Fore.GREEN}{texto:^40}{Fore.RESET}')
    print(f'{"=" * 40:^40}')


def pline():
    print(f'{"-" * 40:^40}')


def cabecalho(texto):
    print(f'{Fore.BLUE}{texto:^40}{Fore.RESET}')
