def voto(ano):

    from datetime import date

    idade = date.today().year - ano

    if idade >= 18 and idade <65:
        print("O voto é OBRIGATORIO!!")
    elif idade >= 16 and idade <= 17 or idade > 65:
        print("O voto é OPCIONAL!!")
    else:
        print("Você ainda NÃO pode votar!!")


ano = int(input("Qual é o seu ano de nascimento: "))
voto(ano)