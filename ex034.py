print(f'{"DESAFIO 34":=^40}')
print(f'{"Qual o meu AUMENTO SALARIAL?":^40}')

salario = float(input('\nQual o seu salário atual: '))
aumento = 0
if salario > 1250:
    aumento = salario * 0.1

if salario <= 1250:
    aumento = salario * 0.15

print('Seu aumento foi de {:.2f}'.format(aumento))

