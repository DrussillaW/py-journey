from colorama import Fore, Style

print(f'{"DESAFIO 67":=^40}')
print(f'{Fore.GREEN + "TABUADA 3.0" + Style.RESET_ALL:^50}\n')

cont = 1
num = int(input('Qual número deseja saber a tabuada? '))
print('='*40)

while True:
    if cont <= 10:
        n = num * cont
        print(f'{num} x {cont} = {Fore.GREEN + str(n) + Style.RESET_ALL}')
        cont += 1
    else:
        cont = 1
        print('='*40)
        num = int(input('Qual número deseja saber a tabuada? '))
        if num <= 0:
            break
        print('='*40)

print('\nO programa foi encerrado! Até mais...')
