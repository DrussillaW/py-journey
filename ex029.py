print(f'{"DESAFIO 29":=^40}')

velocidade = int(input('Qual a velocidade do seu carro? '))

if velocidade > 80:
    vel_ultrapassada = (velocidade - 80)*7
    print('Você foi MULTADO. Sua velocidade ultrapassou 80km/h.'
          '\nO valor da sua multa ficará em R${}.'.format(vel_ultrapassada))
