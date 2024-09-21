from colorama import Fore

print(f'{"DESAFIO 76":=^40}')
print(f'{Fore.GREEN}{"LISTA DE PREÇOS EM TUPLAS":^40}{Fore.RESET}')
print(f'{"="*40:^40}')

lista = ('Base', 69.9, 'Blush', 49.9, 'Corretivo', 47.8, 'Contorno em creme', 32.9, 'Batom', 27.9, 'Rímel', 59.9,
         'Paleta de sombra', 89.9, 'Pincéis', 139.9, 'Esponja', 23.8)

print(f'{Fore.CYAN}{"ITENS DE MAQUIAGEM":^40}{Fore.RESET}')
print(f'{"="*40:^40}')

# for list in range(0, len(lista)):
#     if list % 2 == 0:
#         print(f'{lista[list]:.<30}R$ ', end='')
#     else:
#         print(f'{lista[list]:>7.2f}')
# print(f'{"="*40:^40}')

for i in range(0, len(lista), 2):
    print(f'{lista[i]:.<30}R$ {lista[i+1]:>7.2f}')
