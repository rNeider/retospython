instructor =[]
repetir = "s"

while repetir == "S" or repetir == "s":
    opcion = int(input("Que quiere hacer,\n1.Agregar Un instructor\n2.Listar los instructores\n3.modificar elemento de la lista \n4.Borrar un elemento de la lista \n5.Buscar un elemento en particular\n6.Ordenar la lista de intructores\n"))
    if(opcion==1):
        instructor.append(input("Dijite el nombre de el instructor a agregar\n"))
    elif(opcion==2):
        for i,e in enumerate(instructor):
            print(i,e)
    elif(opcion==3):
        for i,e in enumerate(instructor):
            print(i,e)
        modificar=int(input("Ingrese la posicion a modificar \n"))
        ValorN=input("Dijite el instructor a remlpazar ")
        instructor[modificar]=ValorN
        for i,e in enumerate(instructor):
            print(i,e)
    elif(opcion==4):
        for i,e in enumerate(instructor):
            print(i,e)
        BorrarElemento = (input("Ingresa el instructor que desea borrar:"))
        instructor.remove(BorrarElemento)
    elif(opcion==5):
        buscar=input("Dijite lo que quiere buscar\n")
        verificar=False
        for instructors in instructor:
            if instructors==buscar.lower():
                verificar=True
                print("El instructor se encuentra en el listado")
                for i,e in enumerate(instructor):
                    print(i,e)
        if not verificar:
            print("El instructor no esta en el listado")
    elif(opcion==6):
        instructor.sort()
        print(instructor)
    
    repetir=input("Dijte S para segui o N para salir\n")
        
