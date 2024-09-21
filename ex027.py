print(f'{"DESAFIO 27":=^40}')

nome = input('Digite seu nome completo: ')

div_nome = nome.split()
#ultimo_indice = len(div_nome) - 1

print('Seu primeiro nome é: {}'.format(div_nome[0].upper()))
print('Seu último nome é: {}'.format(div_nome[len(div_nome)-1]))

# print('Seu último nome é: {}'.format(div_nome[ultimo_indice].upper()))
# print('Seu último nome é: {}'.format(div_nome[-1].upper()))