import sys
from colorama import Fore

print(f'{"DESAFIO 87":=^40}')
print(f'{Fore.GREEN}{"MATRIZ 2.0":^40}{Fore.RESET}')
print(f'{"="*40:^40}')

matriz = []
soma_par = soma_coluna3 = 0
big = -sys.maxsize

for l in range(0, 3):
    matriz.append([])
    for c in range(0, 3):
        num = int(input(f'Digite um valor para [{l}, {c}]: '))
        matriz[l].append(num)
        if num % 2 == 0:
            soma_par += num
        if c == 2:
            soma_coluna3 += num
        if l == 1:
            if num > big:
                big = num
print(f'{"~"*40:^40}')
for l in matriz:
    for c in l:
        print(f'[{Fore.GREEN}{c:^7}{Fore.RESET}]', end='')
    print()
print(f'{"~"*40:^40}')
print(f'{Fore.GREEN}A soma dos valores pares é:{Fore.RESET} {soma_par}.')
print(f'{Fore.GREEN}A soma dos valores da 3ª coluna é:{Fore.RESET} {soma_coluna3}')
print(f'{Fore.GREEN}O maior valor na 2ª coluna é:{Fore.RESET} {big}')


