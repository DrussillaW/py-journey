from colorama import Fore
from random import randint

print(f'{"DESAFIO 74":=^40}')
print(f'{Fore.GREEN}{"MAIOR E MENOR EM TUPLAS":^40}{Fore.RESET}')
print(f'{"="*40:^40}')

num1 = randint(0, 10)
num2 = randint(0, 10)
num3 = randint(0, 10)
num4 = randint(0, 10)
num5 = randint(0, 10)

numeros = (num1, num2, num3, num4, num5)
print(f'A tupla de números gerada é {Fore.GREEN}{numeros}{Fore.RESET}')
print('')

min = 11
max = -1
for num in numeros:
    if num < min:
        min = num
    if num > max:
        max = num
print(f'O menor valor é {Fore.GREEN}{max}{Fore.RESET}.')
print(f'O menor valor é {Fore.GREEN}{min}{Fore.RESET}.')

# print(f'O maior valor é {Fore.GREEN}{max(numeros)}{Fore.RESET}.')
# print(f'O menor valor é {Fore.GREEN}{min(numeros)}{Fore.RESET}.')
print('='*40)



