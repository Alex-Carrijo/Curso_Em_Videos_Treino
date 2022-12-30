from random import choice
n1 = str(input("digite o nome do primeiro aluno:"))
n2 = str(input("digite o nome do segundo aluno:"))
n3 = str(input("digite o nome do terceiro aluno:"))
n4 = str(input('digite o nome do quarto aluno:'))
al = [n1,n2,n3,n4]
esc = choice(al)
print('o aluno escolhido foi: {}'.format(esc))