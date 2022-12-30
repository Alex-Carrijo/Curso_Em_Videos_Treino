''' juros Composto e Juros Composto com acrescimos mensais '''

acrescimos = input("O juros será com acrescimos? S/N: ").upper().strip()[0]
valor = float(input("Qual é o valor que será investido? "))
juros = float(input("Qual é o valor do juros mensal? "))
meses = int(input("Quantos meses esse valor ficara rendendo? "))
total = valor

if acrescimos == "S":
    acrescimo = float(input("Qual é o valor do montante adicionado por mes? "))

    for c in range(1,meses+1):
        total += total*(juros/100) + acrescimo
    print(f"Valor total investido: {valor * meses} ")

else:

    for c in range(1,meses+1):
        total += total*(juros/100)
    print(f"Valor total investido: {valor} ")

print("O valor total em {} meses irá ser de R${:.2f}".format(meses,total) )