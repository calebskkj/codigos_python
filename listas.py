animais = ["cobra", "galinha", "ornitorrinco"]
print(type(animais))#exibindo o tipo da variável

print(animais)

#exibindo todos os itens da lista
print("="*50)
for itens in animais:
    print(itens)

#1ª etapa atualizar dados
print("="*50)
animais[0] = "carcará"
print(animais)

#2ª etapa: Inserir dados
print("="*50)
#Forma 1 - Usando append
animais.append("Cacatua") #irá inserir um novo item no final da lista
print(animais)

#2ª forma - usando insert
animais.insert(1, "Ave") #insert precisa de dois valores, o primeiro será o índice que desejo inserir o valor, o segundo é o conteúdo
print(animais)

#3ª etapa - excluir dados
print("="*50)
#forma 1 - usando pop()
animais.pop()#remove o último item da lista
print(animais)

#forma 2 usando pop() com indice
animais.pop(0) #aqui iremos escolher qual índice da lista será excluido
print(animais)

#forma 3 - usando remove
animais.remove("galinha") #irá remover o item pelo conteúdo
print(animais)