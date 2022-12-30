classificacao = ('Atletico-MG','Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians',
                 'Bragantino', 'Fluminense', 'América-MG', 'Atlético-GO','Santos','Ceará-SC',
                 'Internacional', 'São Paulo', 'Athletico-PR','Cuiabá','Juventude','Grêmio',
                 'Bahia','Sport Recife','Chapecoense')
len(classificacao)
print(f'Lista de Times: {classificacao}')
print('-='*20)
print(classificacao[0:6])
print('-='*20)
print(classificacao[-4:])
print('-='*20)
print(f'Lista em ordem alfabetica: {sorted(classificacao)}')
print('-='*20)
print(f'O Chapecoense esta no {classificacao.index("Chapecoense") + 1}° lugar')