import random
from colorama import Fore, Style

print(f'{"DESAFIO 58":=^40}')
print(f'{Fore.GREEN + "JOGO DA ADIVINHAÇÃO" + Style.RESET_ALL:^50}\n')

print('Pensarei em um número entre 0 e 10...')

num_aleatorio = random.randint(0, 10)
num_usuario = int(input('Em qual número pensei? '))
qtd_de_rodada = 0

while num_usuario != num_aleatorio:
    if num_usuario > num_aleatorio:
        print (Fore.GREEN + '\nMenor...' + Style.RESET_ALL +' Tente de novo!')
    if num_usuario < num_aleatorio:
        print(Fore.GREEN + '\nMaior...' + Style.RESET_ALL +' Tente de novo!')
    num_usuario = int(input('Qual seu palpite: '))
    qtd_de_rodada += 1

print('\nVocê acertou!' + Fore.GREEN + 'PARABÉNS.' + Style.RESET_ALL)
print('Sua quantidade de tentativas foi de {} vezes.'.format(Fore.GREEN + str(qtd_de_rodada) + Style.RESET_ALL))


