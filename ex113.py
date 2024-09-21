from utils.helper import titulo, pline
from utilidadescev.dado import leiaint, leiafloat

titulo('TRATANDO ERROS', 113)


# Programa Principal
inteiro = leiaint('Digite um Inteiro: ')
real = leiafloat('Digite um Real: ')
pline()
print(f'O número inteiro digitado foi [{inteiro}] e o real foi [{real}].')
