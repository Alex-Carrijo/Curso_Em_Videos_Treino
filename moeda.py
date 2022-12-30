def aumentar(valor, x):
    aume = valor*(1 + x/100)
    print(f" Aumentando o R${valor} em {x}% temos R${aume}")

def diminuir(valor, x):
    dimi = valor*(1 - x/100)
    print(f" Diminuindo o R${valor} em {x}% temos R${dimi}")

def dobrar(valor):
    dobr = valor*2
    print(f" Dobrando o R${valor} temos R${dobr}")

def metade(valor):
    meta = valor/2
    print(f" Fazendo a metade do R${valor} temos R${meta}")