dia = int(input("quantos dia o carro foi alugado:"))
km = float(input("quantos km foi percorrido:"))
vd = dia * 60
vk = km * 0.15
vt = vd + vk
print("o valor total a ser pago é:R${:.2f}".format(vt))