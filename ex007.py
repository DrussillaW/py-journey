print('** BEM VINDO **!')
a = input('Qual seu nome? ')
print('Olá {}! Vamos começar. '.format(a))

nota1 = float(input('Qual sua primeira nota? ').replace(',', '.'))
nota2 = float(input('Qual sua segunda nota? ').replace(',', '.'))

m = (nota1 + nota2) / 2
print('Sua média final será {:.2f} !'.format(m))