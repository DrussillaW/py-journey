def aumentar(valor, taxa, form=False):
    vf_au = valor + (valor * (taxa / 100))
    return vf_au if not form else moeda(vf_au)


def diminuir(valor, taxa, form=False):
    vf_di = valor - (valor * (taxa / 100))
    return vf_di if not form else moeda(vf_di)


def dobrar(valor, form=False):
    vd = valor * 2
    return vd if not form else moeda(vd)


def metade(valor, form=False):
    vm = valor / 2
    return vm if not form else moeda(vm)


def moeda(valor):
    return f'R${valor:.2f}'.replace('.', ',')


def resumo(valor, tax_aum, tax_dim):
    from utils.helper import pline, cabecalho

    preco = moeda(valor)
    dob = dobrar(valor, True)
    met = metade(valor, True)
    t_up = aumentar(valor, tax_aum, True)
    t_dw = diminuir(valor, tax_dim, True)

    pline()
    cabecalho('RESUMO DO VALOR')
    pline()

    print(f'{"Preço Analisado":<20}{preco:>20}')
    print(f'{"Dobro do Preço:":<20}{dob:>20}')
    print(f'{"Metade do Preço:":<20}{met:>20}')
    print(f'{str(tax_aum) + "% de aumento:":<20}{t_up:>20}')
    print(f'{str(tax_dim) + "% de redução:":<20}{t_dw:>20}')

    pline()
