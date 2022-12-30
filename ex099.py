from time import sleep

def maior(* num):
    print("=-"*18)
    cont = maior = 0
    print("Analisando os valores informados")
    for valor in num:
        sleep(0.5)
        print(f'{valor} ',end="", flush=True)
        if cont == 0:
            maiornum = valor
        elif maiornum < valor:
            maiornum = valor
        cont += 1
    print("")
    print(f"Foram informados {cont} valores!")
    print(f"O maior valor informado foi: {maiornum}")
    print("=-" *18)

maior(1,2,3,4,5,6,7,6,5,4,3,2,1)
maior(8, 22, 0, 13, 24, 13, 10, 9)