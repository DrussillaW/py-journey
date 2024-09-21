import random
print('{:=^50}'.format('QUEM SERÁ O ESCOLHIDO?'))
aluno1 = input("Digite o nome do primeiro aluno: ")
aluno2 = input("Digite o nome do segundo aluno: ")
aluno3 = input("Digite o nome do terceiro aluno: ")
aluno4 = input("Digite o nome do quarto aluno: ")

# lista = [aluno1, aluno2, aluno3, aluno4]
# aluno_choice = random.choice(lista)
aluno_escolhido = random.choice((aluno1, aluno2, aluno3, aluno4))

print(f'O aluno escolhido foi: {aluno_escolhido}')
# print('O aluno escolhido foi: {}. '.format(aluno_choice))
