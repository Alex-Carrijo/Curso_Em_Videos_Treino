def formatacao(texto):
    comprimento = len(texto)
    print("~"*(comprimento+2))
    print(f" {texto}")
    print("~"*(comprimento+2))


t = str(input("Digite um texto que deseja ser formatado: "))
formatacao(t)
