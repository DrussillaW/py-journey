from utils.helper import titulo
from colorama import Fore

titulo('SISTEMA INTERATIVO', 106)


def ajuda(msg):
    while True:
        aj = str(input(f'{Fore.YELLOW}{msg}{Fore.RESET}'))
        if aj.upper() == 'FIM':
            print(f'{Fore.RED}Encerrando o programa!{Fore.RESET}')
            break
        print(f'{Fore.BLUE}Acessando o manual de {aj}...{Fore.RESET}')
        help(aj)


# Programa Principal
ajuda(f'Função ou Biblioteca ➡ ')


