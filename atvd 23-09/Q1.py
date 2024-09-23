print("Escolha uma atividade:")
print("1ª - Caminhada")
print("2ª - Corrida")
print("3ª - Ciclismo")

opcao = int(input("Digite o número correspondente à atividade: "))

tempo = int(input("Informe o tempo da atividade em minutos: "))

if opcao == 1:
    calorias_por_minuto = 5  
    atividade = "Caminhada"
elif opcao == 2:
    calorias_por_minuto = 10  
    atividade = "Corrida"
elif opcao == 3:
    calorias_por_minuto = 8  
    atividade = "Ciclismo"
else:
    print("Opção inválida. Tente novamente.")
    calorias_por_minuto = 0
    atividade = "Desconhecida"


calorias_queimadas = calorias_por_minuto * tempo


if calorias_por_minuto > 0:
    print(f"Você queimou {calorias_queimadas} calorias em {tempo} minutos de {atividade}.")