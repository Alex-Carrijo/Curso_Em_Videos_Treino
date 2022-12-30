lista = str(input('Digite uma expressão: '))
abri = fech = 0
for simb in lista:
    if simb == '(':
        abri += 1
    elif simb ==')':
        fech += 1
if abri == fech:
    print('Sua expressao está correta!!!')
else:
    total = abri-fech
    print(f'Sua expressao esta errada!\nEla tem {total} cochetes abertos a mais! ')

'''
expr =  str(input('Digite uma expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão esta certa!')
else:
    print('Sua expressão esta errada!')
'''