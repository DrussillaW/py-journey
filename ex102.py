from utils.helper import titulo, pline

titulo('FATORIAL', 102)


def fatorial(num, show=False):
    """
    - Faz o fatorial de um número inteiro positivo.
    :param num: número que deseja fatorar.
    :param show: (Opcional) Mostra o cálculo do fatorial.
    :return: retorna o valor final do fatorial de 'num'.
    """
    f = 1
    fat = ''
    for c in range(num, 0, -1):
        f *= c
        if c == 1:
            fat += f'{c} '
        else:
            fat += f'{c} x '
    if show:
        print(f'{fat}', end='')
    return f'= {f}'


# Programa Principal
print(fatorial(8, True))
# help(fatorial)
