valor_conta = float(input("Informe o valor da conta (R$): "))

percentual_gorjeta = float(input("Informe o percentual de gorjeta (%): "))

valor_gorjeta = valor_conta * (percentual_gorjeta / 100)

total_conta = valor_conta + valor_gorjeta

print(f"Gorjeta: R$ {valor_gorjeta:.2f}")
print(f"Total: R$ {total_conta:.2f}")
