persona = {
    "nombre":"Jennifer Andrea",
    "nombre2" : "fajardo bolivar ",
    "age":25,
    "id" : 125489,
    "state":True
}
#Muestra contenido integro
print(persona)
#Muestra el valor de un key en particular
print(persona["nombre"])
#Muestra el valor de una key en particular con el metodo get
print(persona.get("nombre2"))
#Acceder a un elemento para poder modificarlo atraves de la key 
persona["nombre"] = "Tatiana Lizeth"
print(persona["nombre"])
#Agregar una key con su valor 
persona["titulo"]="Ingenieria Electronica"
#Acceder a un elemento 
persona.update({"nombre":"Jennifer Andrea"})
print(persona)
#borrar por una key
persona.pop("titulo")
print(persona)
#Borrar ultimo elemento
persona.popitem()
print(persona)

del persona["nombre"]
print(persona)
#Muestra los keys de el diccionario
for k in persona:
    print(k)
#Muetra lo value de el diccionario 
for v in persona:
    print(persona[v])
#Muestra cada par key y value de el diccionario
for k,v in persona.items():
    print(k,":",v)
i1={
    "Nombre":"Neider",
    "Apellido":"Dulcey",
    "Titulo":"Ingieneria en sistemas"
}
i2={
    "Nombre":"Willson",
    "Apellido":"Cabrera",
    "Titulo":"Ingenieria Electronica"
}
#Diccionarios anidados
instructores={
    "instructor":i1,
    "instrctor":i2
}
print(instructores)