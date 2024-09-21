from colorama import Fore, Style

print(f'{"DESAFIO 64":=^40}')
print(f'{Fore.GREEN + "TRATANDO VALORES" + Style.RESET_ALL:^50}\n')

num = int(input('Digite um número [999 para PARAR]: '))
contador = 0
soma = 0

while num != 999:
    soma += num
    contador += 1
    num = int(input('Digite um número [999 para PARAR]: '))
print('=-'*20)
print('''Foram digitados {} números. 
A soma entre eles é {}.'''.format(Fore.GREEN + str(contador) + Style.RESET_ALL, Fore.GREEN + str(soma) + Style.RESET_ALL))
print('=-'*20)