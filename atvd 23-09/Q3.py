import time
def contador(segundos): 
    
    for ctg in range (segundos,0,-1):
        print(ctg)
        time.sleep(1)


segundos = int(input("INFORME A QUANTIDADE DE SEGUNDOS: "))

print(contador(segundos))

