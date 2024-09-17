import random
tentativa = 1
alt = random.randint(1, 10)


while tentativa <=5 or alt!=valor:
    valor = int(input("Informe um número: "))
    if alt > valor:
        print("Informe um valor maior: ")
        
    elif alt< valor:
        print("Informe um valor menor: ")
       
    elif alt==valor:
        print("Parabéns você acertou")
    else:
        print(alt)
    tentativa= tentativa+1
