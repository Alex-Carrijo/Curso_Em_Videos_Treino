def ficha(jog, gol):
    print(f"O jogador {jog} fez {gol} gols no campeonato! ")
nome = str(input("Nome do Jogador: "))
gols = str(input("Número de Gols: "))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip()=="":
    ficha(gol=gols)
else:
    ficha(nome, gols)