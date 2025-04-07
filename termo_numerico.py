import random 
import os 



for r in range(10): 
    num_main = random.randrange(1000, 9999)
    
    resto = 0
    x = 0
    y = 0
    z = 0
    w = 0
        
    x = num_main // 1000 
    resto = num_main%1000
    y = resto // 100
    resto = resto%100
    z = resto // 10
    resto = resto%10
    w = resto // 1
            
    xd = ""   
    yd = ""
    zd = ""
    wd = ""
    
    xe = "_"
    ye = "_"
    ze = "_"
    we = "_"
    
    
    if (x == 5) or (x == 4) or (x == 3) or (x == 2) or (x == 1):
        xd = "\033[4m<=5\033[0m"
    else:
        xd = "\033[4m>5\033[0m"
    
    if (y == 1) or (y == 3) or (y == 5) or (y == 7) or (y == 9):
        yd = "\033[4mÍMPAR\033[0m"
    else:
        yd = "\033[4mPAR\033[0m"
    
    if (z == 5) or (z == 6) or (z == 7) or (z == 8) or (z == 9):
        zd = "\033[4m>=5\033[0m"
    else:
        zd = "\033[4m<5\033[0m"
    
    if (w == 1) or (w == 3) or (w == 5) or (w == 7) or (w == 9):
        wd = "\033[4mÍMPAR\033[0m"
    else:
        wd = "\033[4mPAR\033[0m"
    
    
    i = 0 
    chances = 10
    
    print ("="*50)
    print(f"  Bem-vindo ao termo numérico!\n{'='*50}")
    
   
    while i < 10: 
       print (f"\nVocê tem {chances} tentativas para adivinhar a sequência numérica de 4 dígitos:\n")
       print(f" ", x, y, z, w)
       print(f"Progresso: {xe} {ye} {ze} {we}")
       if i >= 1: 
           print(f"Ultimo chute: {chute}")
       chute = int(input("Insira uma sequência de 4 dígitos: "))
       
       resto2 = 0 
       
       chutex = 0
       chutey = 0
       chutez = 0
       chutew = 0
       
       chutex = chute // 1000 
       resto2 = chute%1000
       chutey = resto2 // 100
       resto2 = resto2%100
       chutez = resto2 // 10
       resto2 = resto2%10
       chutew = resto2 // 1
       
       
       
       
       
       if (chutex == x): 
           xe = x
       if (chutey == y): 
           ye = y
       if (chutez == z): 
           ze = z
       if (chutew == w): 
           we = w
       
       
       
       if i >= 5: 
           if xe == "_":  
               xe = xd
           elif ye == "_":
               ye = yd
           elif ze == "_":
               ze = zd
           elif we == "_": 
               we = wd
         
               
   
       if (xe == x) and (ye == y) and (ze == z) and (we == w):
           print(f"\n{'='*50}")
           print(f"Parabéns, você zerou o game!\nA sequência era: {xe}{ye}{ze}{we}")
           print(f"{'='*50}")
           dnv = input("Deseja jogar novamente? (SIM(s) | NÃO(n))").lower()
           if dnv == "s":
               break     
       else: 
           i += 1
           chances -= 1
   
       
       if i == 10: 
           print(f"\nVocê não conseguiu acertar a sequência. A sequência era: {x}{y}{z}{w}")
           print(f"{'='*50}")
           dnv = input("Deseja jogar novamente? (SIM(s) | NÃO(n))")
           if dnv == "s":
               break
     
                   
           
       os.system('cls')
    
    
    