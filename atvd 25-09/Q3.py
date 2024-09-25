def converter_temperatura(celsius, escala):
    if escala == 'F':
        return (9/5) * celsius + 32
    elif escala == 'K':
        return celsius + 273.15
    else:
        return None  

while True:
    celsius = float(input("Informe a temperatura em graus Celsius (ou um valor negativo para encerrar): "))
    if celsius < 0:
        print("O programa foi encerrado.")
        break
    
    escala = input("Deseja converter para Fahrenheit (F) ou Kelvin (K)? ")
    resultado = converter_temperatura(celsius, escala)
    
    if resultado:  
        if escala == 'F':
            print(f"{celsius}°C é igual a {resultado}°F.")
        elif escala == 'K':
            print(f"{celsius}°C é igual a {resultado}K.")
    else:
        print("Escala inválida! Escolha 'F' ou 'K'.")
