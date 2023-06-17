fruver={}
while True:
    Opcion=(int(input("Bienvenido A Fruver Supermercado Noe\n \n1. Añadir/Midificar \n2. Buscar\n3.Borrar\n4.Listar\n5.Salir\n")))
    if(Opcion==1):
        articulo=input("Ingrese el nombre de el articulo\n ")
        if(articulo in fruver):
            print("El articula a se encuentra registrado")
            opcion=int(input("1 Modificar el precio de un articulo \n2.Modificar el tipo de articulo \n3.Termino\n"))
            if(opcion==1):
                precio=int(input("Dame el nuevo precio de el articulo\n"))
                fruver[articulo]['precio']=precio
            if(opcion==2):
                tipo=int(input("Seleccione el nuevo tipo de el articulo \n1.Vegetal \n2.Fruta\n"))
                if(tipo==1):
                    variedad="Vegetal"
                elif(tipo==2):
                    variedad="Fruta"
                fruver[articulo]['Tipo']=variedad
        else:
            fruver [articulo]={}
            precio=int(input("Dame el precio de el articulo"))
            fruver [articulo]['precio']= precio
            tipo=int(input("Seleccione el tipo de articulo \n1. Vegetar\n2. Fruta"))
            if(tipo==1):
                variedad="Vegetal"
            else:
                variedad="Fruta"
            fruver[articulo]["tipo"]=variedad
    elif(Opcion==2):
        texto=input("Ingrese el articulo a Buscar")
        print("Se encontraron los siguientes resultados")

        for fruta,datos in fruver.items():
            if fruta.startswith(texto):
                print(f"El precio  de  el articulo ingresado es  {fruver[articulo] ['precio']}")
                print(articulo)
            else:
                print("Articulo no encontrado")
    elif(Opcion==3):
        if len(fruver)==0:
            print("pos si no hay nada q va borarr lokota")
        else:
            for k,v in fruver.items():
                print(k," = ",v)
            borrar=input("Dijite el articulo a Borrar")
            fruver.pop(borrar)
            print("Se borro exitosamente el articulo,",borrar,"y la tabla quedo asi")
            for k,v in fruver.items():
                print("",k," = ",v)
    elif(Opcion==4):
        if len(fruver)==0:
            print("No hay nada aun")
        else:
            for k in fruver:
                print("El listado es \n",k)
    elif(Opcion==5):
        print("Chao Pelea")
        break
    

