from colorama import Fore

print(f'{"DESAFIO 90":=^40}')
print(f'{Fore.GREEN}{"APROVADO OU REPROVADO":^40}{Fore.RESET}')
print(f'{"="*40:^40}')

dados = {}
dados['nome'] = str(input('Qual seu nome: ')).title()
dados['media'] = float(input('Qual sua média: '))

# print(f'Nome é igual a {Fore.GREEN}[{dados["nome"]}]{Fore.RESET}.')
# print(f'Média é igual a {Fore.GREEN}[{dados["media"]}]{Fore.RESET}')
for chave, valor in dados.items():
    print(f'  - {chave.title()} é igual {valor}.')

if dados['media'] >= 7:
    print(f'  - Você está {Fore.GREEN}APROVADO{Fore.RESET}.')
else:
    print(f'  - Você está {Fore.RED}REPROVADO{Fore.RESET}.')
