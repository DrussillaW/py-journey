from colorama import Fore
import time
from random import randint

print(f'{"DESAFIO 88":=^40}')
print(f'{Fore.GREEN}{"MEGA-SENA":^40}{Fore.RESET}')
print(f'{"="*40:^40}')

jogos = []
n = int(input('Quantos jogos deseja que eu sorteie? '))
print(f'{"="*40:^40}')

for l in range(0, n):
    jogos.append([])
    for c in range(0, 6):
        jogos[l].append(randint(1, 60))
    time.sleep(2)
    jogos[l].sort()
    print(f"Jogo {l + 1}: {Fore.GREEN}{jogos[l]}{Fore.RESET}")

print(f'{"="*40:^40}')
print(f'{Fore.CYAN}{"BOA SORTE!":^40}{Fore.RESET}')
