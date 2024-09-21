from colorama import Fore

print(f'{"DESAFIO 85":=^40}')
print(f'{Fore.GREEN}{"LISTA COM PARES E IMPARES":^40}{Fore.RESET}')
print(f'{"="*40:^40}')

par_impar = [[], []]
for c in range(0, 7):
    num = int(input(f'Qual o {c + 1}º valor: '))
    if num % 2 == 0:
        par_impar[0].append(num)
    else:
        par_impar[1].append(num)

print(f'Os valores digitadados são: {par_impar}')
par_impar[0].sort()
print(f'Os valores pares digitados foram: {Fore.GREEN}{par_impar[0]}{Fore.RESET}')
par_impar[1].sort()
print(f'Os valores ímpares digitados  foram: {Fore.GREEN}{par_impar[1]}{Fore.RESET}')