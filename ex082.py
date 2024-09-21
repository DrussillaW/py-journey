from colorama import Fore

print(f'{"DESAFIO 82":=^40}')
print(f'{Fore.GREEN}{"DIVIDINDO EM PAR E IMPAR":^40}{Fore.RESET}')
print(f'{"="*40:^40}')

a = list()
pares = list()
impares = list()

while True:
    num = int(input('Digite um valor: '))
    a.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    resp = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
    while resp not in ['S', 'N']:
        resp = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break

print(f'{"="*40:^40}')
print(f'A lista completa é : {Fore.GREEN}{a}{Fore.RESET}')
print(f'Os números pares da lista são: {Fore.GREEN}{pares}{Fore.RESET}')
print(f'Os números ímpares da lista são: {Fore.GREEN}{impares}{Fore.RESET}')


