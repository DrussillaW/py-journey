from unidecode import unidecode

print(f'{"DESAFIO 26":=^40}')

frase = input('Digite uma frase: ')

frase_normalizada = unidecode(frase)
b_frase = frase_normalizada.lower()
letra_proc = 'a'
a_frase = b_frase.count(letra_proc)
pa_frase = frase_normalizada.find(letra_proc) + 1
ua_frase = frase_normalizada.rfind(letra_proc) + 1

if letra_proc in frase_normalizada:
    print('Aparecem {} letras [A] na frase digitada.'.format(a_frase))
    print('A letra [A] aparece a primeira vez na posição {}.'.format(pa_frase))
    print('A letra [A] aparece a pela última vez na posição {}.'.format(ua_frase))
else:
    print('Não foi encontrada letra [A] na frase digitada.')