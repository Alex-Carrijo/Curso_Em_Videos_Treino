from time import sleep
from datetime import date
for c in range(10,-1,-1):
    print(c)
    sleep(1)
print('Feliz ANO NOVO!, Feliz {}'.format(date.today().year+1))