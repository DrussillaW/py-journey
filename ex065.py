from colorama import Fore, Style

print(f'{"DESAFIO 65":=^40}')
print(f'{Fore.GREEN + "MÉDIA, MAIOR E MENOR" + Style.RESET_ALL:^50}\n')

num = int(input('Digite um valor: '))
contador = 1
soma = maior = menor = num
media = soma / contador
continuar = str(input('Deseja digitar outro valor: [S/N]  ')).upper().strip()[0]

while continuar == 'S':
    num = int(input('Digite outro valor: '))
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    soma += num
    contador += 1
    media = soma / contador
    continuar = str(input('Deseja digitar outro valor: [S/N]  ')).upper().strip()[0]

print('-='*20)
print('A média dos números digitados é {}'.format(Fore.GREEN + "{:.2f}".format(media) + Style.RESET_ALL))
print('O maior número é {} e o menor é {}'.format(Fore.GREEN + str(maior) + Style.RESET_ALL, Fore.GREEN + str(menor) + Style.RESET_ALL))






