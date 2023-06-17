import random

seguir="s"
Valor=500

def LanzarMoneda():
    nombreJugador=input("Digite su nombre\n")
    numero= random.randint(1, 2)
    return (numero,nombreJugador)

def jugar():
    numero,nombreJugador=LanzarMoneda()
    Seleccion=int(input("Digite \n1. Cara\n2. Cruz\n"))
    Apuesta=int(input(f"Digite cuanto dinero va a apostar {nombreJugador}, su dinero actual es de {Valor} \n"))
    if Seleccion==1:
        print("Usted Escogio Cara")
    elif Seleccion==2:
        print("Usted Escogio Cruz")
    else:
        print("Opcion no valida")

    if numero==1 and Seleccion==1 and Apuesta<=Valor:
        print("Salió Cara, usted escogió cara, Ganaste!...")
        ganar(Valor,Apuesta)
    elif numero==1 and Seleccion==2 and Apuesta<=Valor:
        print("Salió Cara, usted escogió Sello, Perdiste!...")
        perder(Valor,Apuesta)
    elif numero==2 and Seleccion==2 and Apuesta<=Valor:
        print("Salió Sello, usted escogió Sello, Ganaste!...")
        ganar(Valor,Apuesta)
    elif numero==2 and Seleccion==1 and Apuesta<=Valor:
        print("Salió Sello, usted escogió Cara, Perdiste!...")
        perder(Valor,Apuesta)
    elif numero!=1 or Seleccion!=2 and Apuesta<=Valor:
        print("Digitaste una opción incorrecta")
    else:
        print("Datos Incorrectos o dinero insuficiente")
    
    return (Seleccion, Apuesta)
    
def ganar(Valor,Apuesta):
    ValorGlobal=ValorGlobal+Apuesta
    print(f"El Valor Global Es {Valor} mil pesos")
        
def perder(Valor,Apuesta):
    ValorGlobal=ValorGlobal-Apuesta
    print(f"El Valor Global Es {Valor} mil pesos")
        
while seguir=="s":  
    print("Bienvenido al juego carisellazo") 
    jugar()
    seguir=input("Digite s para seguir o otra letra para salir\n")





      
   