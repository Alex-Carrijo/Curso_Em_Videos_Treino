def area(largura, comprimento):
    a = largura*comprimento
    print(f"A area do terreno {largura}x{comprimento} = {a}m²")

l = float(input("Largura (m): "))
c = float(input("Comprimento (m): "))
area(l, c)