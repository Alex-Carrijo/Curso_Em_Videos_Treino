from math import sqrt, hypot
ca = float(input("digite o tamanho do cateto adjacente:"))
co = float(input("digite o tamanho do cateto oposto:"))
hi = sqrt((ca**2) +(co**2))
# hi = hypot(ca, co)
print("a hipotenusa é: {:.2f}".format(hi))