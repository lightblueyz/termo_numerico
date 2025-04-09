import random 
import os 

j = 0  

while j < 1:
    os.system('cls')  
    
    num_main = random.randrange(1000, 9999)
    
    x = num_main // 1000 
    resto = num_main % 1000
    y = resto // 100
    resto = resto % 100
    z = resto // 10
    w = resto % 10

    if x <= 5:
        xd = "\033[4m<=5\033[0m"
    else:
        xd = "\033[4m>5\033[0m"

    if y % 2 == 1:
        yd = "\033[4mÍMPAR\033[0m"
    else:
        yd = "\033[4mPAR\033[0m"

    if z >= 5:
        zd = "\033[4m>=5\033[0m"
    else:
        zd = "\033[4m<5\033[0m"

    if w % 2 == 1:
        wd = "\033[4mÍMPAR\033[0m"
    else:
        wd = "\033[4mPAR\033[0m"

    xe = "_"
    ye = "_"
    ze = "_"
    we = "_"

    i = 0
    chances = 10
    chute = 0

    print("=" * 50)
    print(f"  Bem-vindo ao termo numérico!\n{'='*50}")

    while i < 10:
        print(f"\nVocê tem {chances} tentativas para adivinhar a sequência numérica de 4 dígitos:\n")
        print(f" ", x, y, z, w)  
        print(f"Progresso: {xe} {ye} {ze} {we}")
        if i >= 1:
            print(f"Último chute: {chute}")
        chute = int(input("Insira uma sequência de 4 dígitos entre 1000 e 9999: "))
        
        if chute < 1000 or chute > 9999:
            print("O número inserido não é válido.")
            continue  

        chutex = chute // 1000 
        resto2 = chute % 1000
        chutey = resto2 // 100
        resto2 = resto2 % 100
        chutez = resto2 // 10
        chutew = resto2 % 10

        if chutex == x:
            xe = x
        if chutey == y:
            ye = y
        if chutez == z:
            ze = z
        if chutew == w:
            we = w

        if i >= 5:
            if xe == "_":
                xe = xd
            if ye == "_":
                ye = yd
            if ze == "_":
                ze = zd
            if we == "_":
                we = wd

        if xe == x and ye == y and ze == z and we == w:
            print(f"\n{'='*50}")
            print(f"Parabéns, você zerou o game!\nA sequência era: {x}{y}{z}{w}")
            print(f"{'='*50}")
            dnv = input("Deseja jogar novamente? (SIM(s) | NÃO(n))")
            if dnv == "s" or dnv == "S":
                j = 0
            elif dnv == "n" or dnv == "N":
                j = 1  
            else:
               print("Entrada inválida. Apenas s ou n.")
               dnv = input("Deseja jogar novamente? (SIM(s) | NÃO(n))")
            break

        i += 1
        chances -= 1

        if i == 10:
            print(f"\nVocê não conseguiu acertar a sequência. A sequência era: {x}{y}{z}{w}")
            print("=" * 50)
            dnv = input("Deseja jogar novamente? (SIM(s) | NÃO(n))")
            if dnv == "s" or dnv == "S":
                j = 0
            elif dnv == "n" or dnv == "N":
                j = 1
            else:
                print("Entrada inválida. Apenas s ou n.")
                dnv = input("Deseja jogar novamente? (SIM(s) | NÃO(n))")
