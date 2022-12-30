n = int(input('Digite quantos elemento de fibonacci voce que ver? '))
print('~~'*28)
orden = 0
t1 = 0
t2 = 1
print('{} -> {}'.format(t1,t2), end="")
while orden != n:
    fibonacci = t1 + t2
    t1 = t2
    t2 = fibonacci
    print(' -> {}'.format(fibonacci), end='')
    orden +=1
print(' -> FIM')