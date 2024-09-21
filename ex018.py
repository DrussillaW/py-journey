from math import sin, cos, tan, radians

print('{:=^50}'.format('COSSENO, SENO E TANGENTE?'))
ang = float(input('Vamos calcular? Digite um valor de ângulo: '))

ang_rad = radians(ang)
c = cos(ang_rad)
s = sin(ang_rad)
t = tan(ang_rad)

print('Os valores são: \ncosseno é {:.2f} \nseno é {:.2f} \ntangente é {:.2f}'.format(c, s, t))


