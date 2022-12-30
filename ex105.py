def notas(*n, sit=False):
    """
    -> Função para avaliar notas e situações dos alunos.
    :param n: Notas cadastradas.
    :param sit: Exibir a situaçao da turma.
    :return: Dicionario com as situações da turma.
    """
    r = dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Media'] = sum(n)/len(n)
    if sit:
        if r['Media'] >= 7:
            r['Situação'] = "Boa"
        elif r['Media'] >= 5:
            r['Situação'] = "Razoavel"
        else:
            r['Situação'] = "Ruim"
    return r


resposta = notas(5.5, 2.5, 9, 8.5, 10, sit=True)
print(resposta)