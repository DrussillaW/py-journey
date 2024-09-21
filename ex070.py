from colorama import Fore, Style
import sys

print(f'{"DESAFIO 69":=^40}')
print(f'{Fore.GREEN + "ESTATÍSTICA DE PRODUTOS" + Style.RESET_ALL:^50}')
print(f'{"="*40:^40}\n')

total_gasto = produto_caro = 0
produto_barato = ''
menor = sys.maxsize

while True:
    continuar = ''
    nome = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço do produto R$ '))
    print('='*40)
    if preco > 1000:
        produto_caro += 1
    total_gasto += preco
    if preco < 1000:
        produto_barato = nome
    while continuar not in ['S', 'N']:
        continuar = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
        print('='*40)
    if continuar == 'N':
        break

print(f'\nO total da sua compra foi R$ {Fore.GREEN}{total_gasto}{Fore.RESET}')
print(f'Existem {Fore.GREEN}{produto_caro}{Fore.RESET} produtos com preço maior que {Fore.RED}R$ 1000{Fore.RESET}.')
print(f'O produto mais barato na sua compra foi o(a) {Fore.GREEN}{produto_barato.title()}{Fore.RESET}.')
