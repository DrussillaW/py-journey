from colorama import Fore, Style

print(f'{"DESAFIO 56":=^40}')
print(Fore.GREEN + f'{"_ANÁLISE COMPLETA_":^40}\n' + Style.RESET_ALL)

qts_pessoas = int(input('Quantas pessoas participarão: '))
soma_idade = 0
maior_idade = 0
sexo_feminino = 'F'
sexo_masculino = 'M'
nome_homem_velho = ''
qtd_mulheres = 0

for i in range(0, qts_pessoas):
    nome = str(input('Qual seu nome: '))
    idade = int(input('Qual sua idade: '))
    sexo = str(input('Qual seu sexo? (F) Feminino ou (M) Masculino: ')).upper()
    soma_idade += idade
    if sexo == sexo_masculino and maior_idade < idade:
        maior_idade = idade
        nome_homem_velho = nome
    if idade < 20 and sexo == sexo_feminino:
        qtd_mulheres += 1

print('\nA média das idades é {}'.format(Fore.GREEN + str(soma_idade / qts_pessoas) + Style.RESET_ALL))
print('\nO nome do Homem mais velho é {}.'.format(Fore.GREEN + nome_homem_velho + Style.RESET_ALL))
print('\nHá {} mulher(s) menores que 20 anos.'.format(Fore.GREEN + str(qtd_mulheres) + Style.RESET_ALL))

