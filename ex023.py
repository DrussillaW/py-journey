print(f'{"DESAFIO 23":=^40}')

num = input('Digite um número entre 0 e 9999: ')

t_num = len(num)
qtd_zero = 0

if t_num < 4:
    qtd_zero = 4 - t_num

num_comp = '0' * qtd_zero + num

print(f'Unidade: {num_comp[-1]}')
print(f'Dezena: {num_comp[-2]}')
print(f'Centena: {num_comp[-3]}')
print(f'Milhar: {num_comp[-4]}')
