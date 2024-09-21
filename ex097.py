from utils.helper import titulo, pline

titulo('PRINT ESPECIAL', 97)


def escreva(msg):
    t = len(msg) + 2
    print(f'{"-" * t:^40}')
    print(f'{msg:^40}')
    print(f'{"-" * t:^40}')


# Programa principal
escreva('Drussilla Carvalho')
escreva('Curso Python')
escreva('Mundo3')


