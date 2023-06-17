Comidas= ["Combo Hamburguesa","Sandwich","Pizza"]
Comidas.append("Gaseosa")
#Append 1
print(Comidas)
#extend varios
Comidas.extend(["Malteada","Perro Caliente"])
print(Comidas)
print("En este momento la lista es de ",len(Comidas),"Comidas")
for i,e in enumerate(Comidas):
    print(i,e)
#Agregar un elemento en la list
Comidas.insert(2,"Empanadas")
for i,e in enumerate(Comidas):
    print(i,e)
#Borrar un elemento de  la lista 
Comidas.remove("Gaseosa")
#Borrar un elemento  de una posicion especifica de la lista 
del Comidas [4]
#Borrar el ultimo elemento de la lista 
Comidas.pop()
#limpiar la lista
#Comidas.clear()
print(Comidas)
#ordenar ascendentemente una lista
Comidas.sort()
#ordenar descendentemente una lista
Comidas.reverse()
Comidas.sort(reverse=True)
#Devolver en que posicion esta un elemento de una lista 
print(Comidas.index(4))
