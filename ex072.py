from colorama import Fore

print(f'{"DESAFIO 72":=^40}')
print(f'{Fore.GREEN}{"LEITURA POR EXTENSO":^40}{Fore.RESET}')
print(f'{"="*40:^40}')

num_extenso = ('zero', 'um', 'dois', 'três', 'quatro',
               'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
               'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis',
               'dezessete', 'dezoito', 'dezenove', 'vinte')

num = int(input(f'Digite um valor de {Fore.RED}{"0 a 20"}{Fore.RESET}: '))
while num < 0 or num > 20:
    print('Opção inválida. ', end='')
    num = int(input(f'Digite um valor de {Fore.RED}{"0 a 20"}{Fore.RESET}: '))

# num = int(input(f'Digite um valor de {Fore.RED}{"0 a 20"}{Fore.RESET}: '))
# while True:
#     if num < 0 or num > 20:
#         print('Opção inválida. ', end='')
#         num = int(input(f'Digite um valor de {Fore.RED}{"0 a 20"}{Fore.RESET}: '))
#     else:
#         break

print(f'Você digitou o número {Fore.GREEN}{num_extenso[num].upper()}{Fore.RESET}.')

