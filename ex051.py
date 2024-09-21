print(f'{"DESAFIO 51":=^40}')
print(f'{"_Progressão Aritmética_":^40}\n')

r = int(input('Digite a razão da P.A.: '))
i = int(input('Digite o início da P.A.: '))
f = (r * 10) + i

for c in range(i, f, r):
    print(c)

# for c in range(0, 10):
#     print(i+r*c)
