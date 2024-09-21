from unidecode import unidecode

print(f'{"DESAFIO 53":=^40}')
print(f'{"_POLÍNDROMO_":^40}\n')

frase_original = str(input('Digite sua frase: '))
frase_nova = unidecode(frase_original).upper().replace(' ', '').strip()
# frase_polin = "".join(reversed(frase_nova))
frase_polin = ''

for i in range(len(frase_nova) - 1, -1, -1):
    frase_polin = frase_polin + frase_nova[i]

if frase_nova == frase_polin:
    print('A frase é um POLÍNDROMO.')
else:
    print('A frase não é um POLÍNDROMO.')

print()
