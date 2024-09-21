import time
from colorama import Fore
from utils.helper import titulo, pline


titulo('QUEM É O MAIOR?', 99)


def maior(* numero):
    print(f'{Fore.GREEN}Analisando os valores passados...{Fore.RESET}')
    big = 0
    for num in numero:
        time.sleep(0.4)
        print(f'{Fore.BLUE}{num}{Fore.RESET} ', end='')
        if num > big:
            big = num
    tam = len(numero)
    print(f'\nForam informados ao todo {Fore.BLUE}{tam} números{Fore.RESET}. ')
    print(f'O maior valor informado foi {Fore.BLUE}{big}{Fore.RESET}. ')
    pline()


# Programa principal
maior(2, 5, 8, 9)
maior(5, 20)
maior(8)
maior()


