num = int(input("digite um numero: "))
u = num // 1 % 10 # u = num % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10 # m = num // 1000
print("analisando o numero: {}".format(num))
print("Unidade: {}".format(u))
print("Dezena: {}".format(d))
print("Centena: {}".format(c))
print("Milhar: {}".format(m))
