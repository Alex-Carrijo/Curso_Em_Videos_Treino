from time import sleep
from random import randint

def sorteio(lista):
    for cont in range(0,5):
        n = randint(1, 10)
        lista.append(n)
        print(f"{n} ", end="", flush=True)
        sleep(0.3)
    print("Pronto!")


def somarpar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f"Somando os valores pares da lista {lista}, temos {soma}")

numeros = list()
sorteio(numeros)
somarpar(numeros)