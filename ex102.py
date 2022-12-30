def fatorial(num, show=False):
    """
    -> Calcular o fatorial de um numero
    :param num: O numero o qual quer se obter o fatorial
    :param show: Mostrar a conta ou não do fatorial
    :return: O resultado do fatorial
    """

    cont = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end="")
            if c > 1:
                print(" x ", end="")
            else:
                print(" = ", end="")
        cont *= c
    return cont

print(fatorial(5, show = True))