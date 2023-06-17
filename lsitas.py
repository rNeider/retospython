#Definicion o declaracion de lista 
numeros= [1,2,3,4]
#Mostrar contenido integro de la lista
print(numeros)
#Mostrar posicion particular 
print(numeros [2])
#Mostrar posicion particular
print(numeros [-1])
#Cmbiar numero de posicion
numeros [1]=9
print(numeros)
#recorrer una lista 
for i in numeros:
    print(i)
#recorrer posicion accediente tanto al index como al elemento 
for i,e in enumerate(numeros):
    print(i,e)
#Recorrer 2 listas al mismo tiempo 
generos= ["Jazz", "Salsa", "Rock"]
for ln,lg in zip(numeros,generos):
    print(ln,lg)
#Longitud de la lista 
print(len(generos))


