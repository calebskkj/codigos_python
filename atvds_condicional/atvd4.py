valor = int(input("Digite um valor: "))

if valor % 2 == 0:

    resultado = valor + 10
    print(f"O valor {valor} é par. O resultado da operação é: {resultado}")
else:

    resultado = valor * 2
    print(f"O valor {valor} é impar. O resultado da operação é: {resultado}")