import moeda
valor = int(input("Qual é o valor que deseja calcular: "))
au = int(input("Qual é a porcentagem que deseja aumentar: "))
di = int(input("Qual é a porcentagem que deseja diminuir: "))
moeda.aumentar(valor, au)
moeda.diminuir(valor, di)
moeda.dobrar(valor)
moeda.metade(valor)