from colorama import Fore
from utils.helper import titulo, pline
from random import randint
from time import sleep


titulo('SORTEANDO E SOMANDO', 100)


def sortear(lista, n):
    print(f'Sorteando {n} valores da lista: [', end='')
    for c in range(n):
        rn = randint(1, 10)
        sleep(1)
        print(f'{rn} ', end='')
        lista.append(rn)
    print('\b]. FIM')


def soma_par(numeros):
    print(f'A soma dos valores pares de {numeros} é igual a ', end='')
    sp = 0
    for n in numeros:
        if n % 2 == 0:
            sp += n
    print(f'{sp}.')


# Programa principal
numeros = []
sortear(numeros, 5)
soma_par(numeros)
