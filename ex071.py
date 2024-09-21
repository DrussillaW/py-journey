from colorama import Fore

print(f'{"DESAFIO 71":=^40}')
print(f'{Fore.GREEN}{"CAIXA ELETRÔNICO":^40}{Fore.RESET}')
print(f'{"="*40:^40}')

# valor = int(input('Qual valor deseja sacar R$ '))
#
# tot50 = valor // 50
# valor = valor - (tot50 * 50)
# if tot50 > 0:
#     print(f'O total de {Fore.GREEN}{tot50}{Fore.RESET} de cédulas de R$50.')
#
# tot20 = valor // 20
# valor = valor - (tot20 * 20)
# if tot20 > 0:
#     print(f'O total de {Fore.GREEN}{tot20}{Fore.RESET} de cédulas de R$20.')
#
# tot10 = valor // 10
# valor = valor - (tot10 * 10)
# if tot10 > 0:
#     print(f'O total de {Fore.GREEN}{tot10}{Fore.RESET} de cédulas de R$10.')
#
# tot1 = valor // 1
# valor = valor - (tot1 * 1)
# if tot1 > 0:
#     print(f'O total de {Fore.GREEN}{tot1}{Fore.RESET} de cédulas de R$1.')
#
# print(f'\n{Fore.CYAN}{"TENHA UM BOM DIA! Volte sempre..."}{Fore.RESET}')

valor = int(input('Quanto deseja sacar R$ '))
cont_cedulas = 0

while valor // 50 != 0:
    valor = valor - 50
    cont_cedulas += 1
if cont_cedulas > 0:
    print(f'O total de {Fore.GREEN}{cont_cedulas}{Fore.RESET} de cédulas de R$50.')
    cont_cedulas = 0
while valor // 20 != 0:
    valor = valor - 20
    cont_cedulas += 1
if cont_cedulas > 0:
    print(f'O total de {Fore.GREEN}{cont_cedulas}{Fore.RESET} de cédulas de R$20.')
    cont_cedulas = 0
while valor // 10 != 0:
    valor = valor - 10
    cont_cedulas += 1
if cont_cedulas > 0:
    print(f'O total de {Fore.GREEN}{cont_cedulas}{Fore.RESET} de cédulas de R$10.')
    cont_cedulas = 0
while valor // 1 != 0:
    valor = valor - 1
    cont_cedulas += 1
if cont_cedulas > 0:
    print(f'O total de {Fore.GREEN}{cont_cedulas}{Fore.RESET} de cédulas de R$1.')
    cont_cedulas = 0
print('='*40)
print(f'\n{Fore.CYAN}{"TENHA UM BOM DIA! Volte sempre..."}{Fore.RESET}')

