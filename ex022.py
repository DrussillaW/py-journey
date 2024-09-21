print(f'{"DESAFIO 22":=^40}')

nome = input('Digite seu nome completo: ')
print('Seu nome em letras maiúsculas é {}'.format(nome.upper()))
print('Seu nome em letras minúsculas é {}'.format(nome.lower()))
print('Seu nome possui {} letras'.format(len(nome.replace(' ', ''))))

# qtd_espacos = nome.count(' ')
# tamanho_tot = len(nome)
# print('Seu nome possui {} letras'.format(tamanho_tot - qtd_espacos))

nome_div = nome.split()
primeiro_nome = nome_div[0]
tam_primeiro_nome = len(primeiro_nome)
print('Seu primeiro nome tem {} letras'.format(tam_primeiro_nome))

