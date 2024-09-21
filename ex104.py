from utils.helper import titulo, pline

titulo('VALIDANDO ENTRADA DE DADOS', 104)


def leiaint(msg):
    from colorama import Fore
    ok = False
    num = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            num = int(n)
            ok = True
        else:
            print(f'{Fore.RED}ERRO. Digite um número inteiro válido.{Fore.RESET}')
        if ok:
            break
    return num


# Programa Principal
numero = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {numero}.')