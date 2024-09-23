objetos = ('lápis', 'borracha', 'caderno')
print(objetos[1]) #Irá exibir o item na posição 1, ou seja segunda posição, pois a contagem começa do zero

print(type(objetos)) #irá mostrar o tipo da variável

print(objetos) #exibindo todos os itens de uma só vez

print("-"*50)
for item in range(0,3):
    print(objetos[item]) #exibindo todos os intens da tupla

#Exibindo todos os itens da tupla sem a função range
print("-"*50)
for elementos in objetos:
    print(elementos)

#Iremos tentar alterar o conteúdo da tupla
objetos[0] = "caneta"