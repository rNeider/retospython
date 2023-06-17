repetir="s"
baul = []

while repetir=="S"or repetir=="s":
    opcion=int(input("Que quiere hacer,\n1.Agregar Articulo al Baul\n2.Listar los articulos acendentemente\n3.Borrar el ultimo elemento \n4.Borrar un articulo de el baul\n"))
    if(opcion==1):
        articulo=input("Ingresa el nombre del articulo que deseas agregar")
        baul.append(articulo)
        print("El articulo ",articulo, "ha sido agregado al baul")
    elif(opcion==2):
        if len(baul)==0:
            print("El baul está vacio")
        else:
            ordenbaul=sorted(baul)
            print("Los articulos del baul son los siguientes")
            for i, articulo in enumerate(ordenbaul):
                print(f"{i+1} {articulo}")
    elif(opcion==3):
        if len(baul)==0:
            print("El baul esta vacio")
        else:
            BorrarArticulo=baul.pop()
            print("El articulo ",BorrarArticulo," ha sido borrado del baul")
    elif(opcion==4):
        if len(baul)==0:
            print("El baul esta vacio")
        else:
            print("Los articulos del baul son los siguientes")
            for i, articulo in enumerate(baul):
                print(f"{i+1} {articulo}")
            lugarLista = int(input("Ingresa el número del articulo que deseas borrar: "))
            if lugarLista<1 or lugarLista>len(baul):
                print("El lugar ingresado no es valido")
            else:
                BorrarArticulo = baul.pop(lugarLista-1)
                print("El articulo" ,BorrarArticulo ,"ha sido borrado con exito del baul.")
    else:
        print("Opcion no valida ")
    repetir=input("Dijte S para segui o N para salir")