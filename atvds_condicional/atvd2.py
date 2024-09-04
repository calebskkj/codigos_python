
nome = input("Digite o seu nome: ")
sexo = input("Digite o seu sexo (M/F): ")
estado_civil = input("Digite o seu estado civil (SOLTEIRO/A, CASADO/A, VIÚVO/A, DIVORCIADO/A): ")


if sexo == "F" and estado_civil == "CASADA":
    tempo_casada = int(input("Digite o tempo de casada (anos): "))
    print(f"{nome}, você está casada há {tempo_casada} anos.")
else:
    print(f"{nome}, obrigado e até a próxima.")