print(f'{"DESAFIO 36":=^40}')

print(f'{"_TRANSFORMANDO BASES_":^40}')

n1 = int(input('\nDigite um número inteiro: '))

base = int(input('''Converter em qual base: 
[1] Binária 
[2] Octal 
[3] Hexadecimal
 => Escolha sua opção: '''))

base_bin = 1
base_octal = 2
base_hexa = 3

if base == base_bin:
    base = bin(n1)[2:]
    print('O número {} na Base Binária é {}'.format(n1, base))
elif base == base_octal:
    base = oct(n1)[2:]
    print('O número {} na Base Octal é {}'.format(n1, base))
elif base == base_hexa:
    base = hex(n1)[2:]
    print('O número {} na Base Hexadecimal é {}'.format(n1, base))
else:
    print('Você não escolheu nenhuma opção válida. O programa está encerrando!')