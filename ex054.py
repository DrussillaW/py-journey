from datetime import date
from colorama import Fore, Style

print(f'{"DESAFIO 54":=^40}')
print(f'{"_MAIOR IDADE_":^40}\n')

idade = 0
maior_idade = 0
qtd_anos = int(input('Quantas pessoas participarão do teste: '))

for i in range(0, qtd_anos):
    ano_nascimento = int(input('Seu ano de nascimento: '))
    idade = date.today().year - ano_nascimento
    if idade > 21:
        maior_idade = maior_idade + 1

print('Existem {} maior(s) de idade.'.format(Fore.GREEN + str(maior_idade) + Style.RESET_ALL))
print('Existem {} menor(s) de idade.'.format(Fore.GREEN + str(qtd_anos - maior_idade) + Style.RESET_ALL))





