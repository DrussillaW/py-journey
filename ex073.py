from colorama import Fore

print(f'{"DESAFIO 73":=^40}')
print(f'{Fore.GREEN}{"TABELA DO BRASILEIRÃO 2024":^40}{Fore.RESET}')
print(f'{"="*40:^40}')

times = ('Botafogo', 'Fortaleza', 'Palmeiras', 'Flamengo', 'Cruzeiro', 'São Paulo', 'Bahia', 'Vasco', 'Atlético-MG',
         'Internacional', 'Bragantino', 'Atlético-PR', 'Juventude', 'Criciúma', 'Grêmio', 'Fluminense', 'Corinthians',
         'EC Vitória', 'Cuiabá', 'Atlético-GO')

print(f'Os {Fore.GREEN}cinco primeiros{Fore.RESET} colocados são:')
print(f'{Fore.GREEN}{(", ".join(times[:5]))}{Fore.RESET}')
print('~'*40)

print(f'Os {Fore.RED}quatro últimos{Fore.RESET} colocados são:')
print(f'{Fore.RED}{(", ".join(times[-4:]))}{Fore.RESET}')
print('~'*40)

print(f'A {Fore.CYAN}ordem alfabética{Fore.RESET} dos times é:')
times_string = "\n".join(sorted(times))
print(f'{Fore.CYAN}{times_string}{Fore.RESET}')
print('~'*40)

chapeco = 'Chapecoense'

# try:
#     rank = times.index(chapeco)
#     print(f'O Chapecoense está na {rank}ª posição.')
# except:
#     print('O Chapecoense não esta na Série A do Brasileirão!')

if chapeco in times:
    rank = times.index(chapeco) + 1
    print(f'O Chapecoense está na {rank}ª posição.')
else:
    print(f'{Fore.GREEN}O Chapecoense não está na Série A do Brasileirão!{Fore.RESET}')