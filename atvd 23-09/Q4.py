import random
ale = random.randint(1,3)

escolha = int(input("Escolha: \n 1-Tesoura \n 2-Pedra \n 3-Papel\n"))

finaliz = 1
while finaliz!=0:
    if  ale == 1 and escolha ==3:
        print("robo ganhou")
        finaliz =int(input("voc quer continuar: sim: 1 não:0"))
    elif ale==1 and escolha==2:
        print("Você ganhou")
        finaliz =int(input("voc quer continuar: sim: 1 não:0"))
    elif ale==2 and escolha ==3:
        print("Você ganhou")
        finaliz =int(input("voc quer continuar: sim: 1 não:0"))
    elif ale == 3 and escolha ==1:
        print("você ganhou")
        finaliz =int(input("voc quer continuar: sim: 1 não:0"))
    elif ale==2 and escolha ==1:
        print("robo ganhou")
        finaliz =int(input("voc quer continuar: sim: 1 não:0"))
    elif ale ==3 and escolha ==2:
        print("robo ganhou")
        finaliz =int(input("voc quer continuar: sim: 1 não:0"))
    escolha = int(input("Escolha: \n 1-Tesoura \n 2-Pedra \n 3-Papel\n"))