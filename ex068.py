from colorama import Fore, Style
from random import randint

print(f'{"DESAFIO 68":=^40}')
print(f'{Fore.GREEN + "PAR OU ÍMPAR" + Style.RESET_ALL:^50}\n')

print('~'*50)
print(Fore.GREEN + f'{"QUE COMECEM OS JOGOS...":^50}' + Style.RESET_ALL)
print('~'*50)

soma = cont = 0
while True:
    num_jogador = int(input('Digite um número: '))
    num_pc = randint(0, 10)
    soma = num_pc + num_jogador
    opcao_jogador = ''
    while opcao_jogador not in ['P', 'I']:
        opcao_jogador = str(input('Par ou Ímpar [P/I]: ')).upper().strip()[0]
    print(f'Você jogou {num_jogador} e o pc {num_pc}!', end='')
    par_impar = 'PAR' if soma % 2 == 0 else 'IMPAR'
    print(f' O total de {soma} deu {Fore.GREEN + par_impar + Style.RESET_ALL}!')
    print('~'*50)
    if (soma % 2 == 0 and opcao_jogador == 'P') or (soma % 2 != 0 and opcao_jogador == 'I'):
        print(Fore.GREEN + 'Você GANHOU!' + Style.RESET_ALL + ' Vamos jogar de novo...')
        print('~'*50)
        cont += 1
    else:
        break

print(Fore.RED + 'GAME OVER! ' + Style.RESET_ALL + f'Você ganhou {cont} vezes.')


