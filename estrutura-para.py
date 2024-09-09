'''
for(contador=1; contador<=5; contador++){
}
'''

#1ª forma d operação do for
for contador in range(1,6):
    print(contador)


#2ª forma de operação do for
for contador in range (1,11,2):#o 3º parametro indica como os valores serão incrementados(alteração do valor)
    print(contador)
print("-"*40)

#3ªforma de operação for
for contador in range(10,0,-1):
    print(contador, end= " ")