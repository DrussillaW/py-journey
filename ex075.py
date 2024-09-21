from colorama import Fore

print(f'{"DESAFIO 75":=^40}')
print(f'{Fore.GREEN}{"ANALISANDO DADOS EM TUPLAS":^40}{Fore.RESET}')
print(f'{"="*40:^40}')

num1 = int(input('Digite o 1º valor: '))
num2 = int(input('Digite o 2º valor: '))
num3 = int(input('Digite o 3º valor: '))
num4 = int(input('Digite o 4º valor: '))
print('='*40)

numeros = (num1, num2, num3, num4)

print(f'Os valores digitados foram: {Fore.GREEN}{str(numeros)}{Fore.RESET}')
print(f'O número 9 apareceu {Fore.GREEN}{numeros.count(9)}{Fore.RESET} vez(s).')
tem3 = False
pares = ''
for num in numeros:
    if num % 2 == 0:
        pares += str(num) + ', '
    if num == 3:
        tem3 = True
if tem3:
    print(f'O número 3 aparece a primeira vez na {Fore.GREEN}{numeros.index(3) + 1}{Fore.RESET}ª posição.')
else:
    print(f'{Fore.RED}{"O número 3 não foi encontrado!"}{Fore.RESET}')

if pares:
    print(f'Os pares encontrados foram {Fore.GREEN}{pares[:-2]}{Fore.RESET}.')
else:
    print(f'{Fore.RED}{"Nenhum número par foi encontrado."}{Fore.RESET}')