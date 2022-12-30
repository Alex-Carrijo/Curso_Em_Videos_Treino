from time import sleep

def contagem(inicio, fim, passo):

    if passo < 0:
        passo = passo*-1
    if passo == 0:
        passo = 1

    print("~~" * 10)
    print(f"Iniciando contagem de {inicio} até {fim} pulando de {passo} !!!")
    if inicio<fim:
        c = inicio
        while c <= fim:
            print(f"{c} ", end="", flush=True)
            c += passo
            sleep(0.5)
        print("Fim!!!")

    else:
        c = inicio
        while c >= fim:
            print(f"{c} ", end="", flush=True)
            c -= passo
            sleep(0.5)
        print("Fim!!!")

contagem(1, 10, 1)
contagem(10, 0, 2)
print("~~" * 10)
print("Agora personalize a sua propria contagem")
inicio = int(input("Por onde quer começar: "))
fim = int(input("E a onde quer terminar: "))
passo = int(input("Qual será o intervalo: "))
print("~~" * 10)

contagem(inicio, fim, passo)