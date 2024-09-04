A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))


if B != 0 and A % B == 0:
    print(f"O valor de A ({A}) é divisível por B ({B}).")
elif B != 0:
    print(f"O valor de A ({A}) não é divisível por B ({B}).")
else:
    print("Erro: não é possível dividir por zero.")