frases = ('Cansei', 'de', 'estudar', 'mas', 'if', 'i', 'dont', 'do', 'it', 'now', 'i', 'will', 'feel', 'bad', 'later')
for p in frases:
    print(f'\nNa palavra {p.upper()} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

