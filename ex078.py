import sys
from colorama import Fore

print(f'{"DESAFIO 78":=^40}')
print(f'{Fore.GREEN}{"MAIOR E MENOR EM UMA LISTA":^40}{Fore.RESET}')
print(f'{"="*40:^40}')

maior = -sys.maxsize
menor = sys.maxsize
valores = list()
for v in range(0, 5):
    num = int(input('Digite um valor: '))
    valores.append(num)
    if num > maior:
        maior = num
    if num < menor:
        menor = num

print(f'{"="*40:^40}')
print(f'Os valores da lista são {Fore.GREEN}{valores}{Fore.RESET}')
print(f'{"="*40:^40}')
print(f'O maior valor da lista é {maior} e o menor é {menor}.')



