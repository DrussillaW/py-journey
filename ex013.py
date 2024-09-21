print('{:=^50}'.format('QUAL SEU NOVO SALÁRIO?'))

salario = float(input('Qual seu salário atual? '))

novo_salario = salario + (salario * 0.15)

print('Seu novo salário com o aumento de 15% é de R$ {:.2f}'.format(novo_salario).replace('.', ','))