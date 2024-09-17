final=1
arroz=2.50
feijao=3.50
total =0


while final !=0:
    compra= int(input("informe o produto: \n arroz:1 \n feijão:2 \n"))
    final = int(input("quer finalizar?\n sim:0 \n não:1 "))
    if compra ==1:
        total= total +arroz
    elif compra ==2:
        total= total+feijao
    else:
        print("ok")


print(f"Lojão do Mohamed\n arroz: 2,50\n feijão: 3,50\n O total da compra foi: {total}")
vpg = float(input("Informe o valor pago: "))

troco = vpg - total
print(f"O valor do seu troco foi {troco}")