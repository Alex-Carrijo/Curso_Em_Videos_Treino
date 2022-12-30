x = int(input('Digite um numero: '))
total = 0
for c in range(1, x+1):
    if x % c == 0:
        print('\033[34m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print('{}' .format(c), end=' ')
print('\n\033[mO numero {} foi dividido {} vezes'.format(x, total))
if total == 2:
    print('por isso ele é IMPAR')
else:
    print('por isso ele é PAR')