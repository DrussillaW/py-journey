from colorama import Fore
from datetime import datetime

print(f'{"DESAFIO 92":=^40}')
print(f'{Fore.GREEN}{"CADASTRO DE TRABALHADOR":^40}{Fore.RESET}')
print(f'{"="*40:^40}')

trabalhador = dict()

trabalhador['Nome'] = str.title(input('Nome: '))
ano = int(input('Ano de nascimento: '))
idade = datetime.now().year - ano
trabalhador['Idade'] = idade
sexo = str(input('Sexo [F/M]: ')).strip().upper()[0]
trabalhador['CTPS'] = int(input('Carteira de Trabalho [0 → não tem]: '))
if trabalhador['CTPS'] != 0:
    trabalhador['Ano Contratação'] = int(input('Ano de contratação: '))
    trabalhador['Salário'] = float(input('Salário: R$'))
    if sexo == 'M':
        trabalhador['Aposentadoria'] = trabalhador['Ano Contratação'] + 35
    if sexo == 'F':
        trabalhador['Aposentadoria'] = trabalhador['Ano Contratação'] + 30

for chave, valor in trabalhador.items():
    print(f'A chave {Fore.GREEN}{chave}{Fore.RESET} é {Fore.BLUE}{valor}{Fore.RESET}.')



