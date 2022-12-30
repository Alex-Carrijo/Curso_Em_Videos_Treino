lanche = ('hambuguer', 'Batata', 'refri', 'pudim')

for c in lanche:
    print(c)

print(len(lanche))

for cont in range(0,len(lanche)):
    print(lanche[cont])

print(sorted(lanche))

a = (2,5,4)
b = (5, 8, 1, 2)
c = a + b
print(len(c))
print(c.count(5))#quantas vezes aparece o 5
print(c.index(5))#a onde o primeiro 5

pessoa = ('Alex', 21, 'M', 60)
print(pessoa)
del(pessoa)#deleta a tupla