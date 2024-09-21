import random

print('{:=^50}'.format('QUEM SERÁ O ESCOLHIDO?'))

aluno1 = input("Digite o nome do primeiro aluno: ")
aluno2 = input("Digite o nome do segundo aluno: ")
aluno3 = input("Digite o nome do terceiro aluno: ")
aluno4 = input("Digite o nome do quarto aluno: ")

alunos_escolhidos = random.sample((aluno1, aluno2, aluno3, aluno4), 4)

print(f'A ordem escolhida foi {alunos_escolhidos}')