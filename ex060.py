x = int(input('Digite um numero que deseje saber seu fatorial: '))
fator = 1
print("{}! =".format(x), end=' ')
while x != 0:
    print("{} ".format(x), end='')
    print('x ' if x > 1 else '=', end='')
    fator = x*fator
    x = x-1
print(' {}'.format(fator))