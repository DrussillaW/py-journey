from utils.helper import titulo

titulo('ANALISANDO E GERANDO DISCIONÁRIOS', 105)


def notas(* nota, situacao=False):
    """
    -> Função para avaliar várias notas de um aluno e a sua situção.
    :param nota: recebe uma ou mais notas do aluno, podendo ser várias.
    :param situacao: (Opcional) Serve para mostrar a situação em relação à média.
    : return: retorna um discionário com total de notas, média, maior e menor nota.
    """
    notas = dict()
    notas['Total_Notas'] = len(nota)
    notas['Maior'] = max(nota)
    notas['Menor'] = min(nota)
    notas['Média'] = round(sum(nota) / notas['Total_Notas'], 2)
    if situacao:
        if notas['Média'] <= 5:
            notas['Situação'] = 'RUIM'
        if 6 < notas['Média'] < 7:
            notas['Situação'] = 'RAZOÁVEL'
        if notas['Média'] >= 7:
            notas['Situação'] = 'BOA'
    return notas


# Programa Principal
aluno = notas(5, 3.5, 4, 3, 2, situacao=True)
print(aluno)
