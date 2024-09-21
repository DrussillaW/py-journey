import time

from utils.helper import titulo, pline
from time import sleep

titulo('CONTADOR', 98)


def contador(inicio, fim, passo):
    if passo == 0:
        if inicio < fim:
            passo = 1
        else:
            passo = -1
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}...')
    if inicio > fim and passo > 0:
        passo = -passo
    if inicio < fim:
        fim += 1
    else:
        fim -= 1
    for c in range(inicio, fim, passo):
            time.sleep(1)
            print(f'[{c}] ', end='')
    print('FIM')
    pline()


# Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é a sua vez de definir a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)

