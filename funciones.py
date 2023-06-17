#Declaracion de un metodo sin parametros 
def sumar(n1,n2):
    #Cuerpo metodo
    sumar=n1+n2
    return sumar
    print("Este es el metodo sumar")


#Declaracion metodo con paramentros

def restar(n1,n2):
    #Cuerpo de el metodo
    restar=n1-n2
    print(f"La resta entre {n1} y {n2} es {restar}")

#Declaracion metodo con valor de retorno

def multiplicar(n1,n2):
#cuerpo de el metodo
    multiplicar=num1*num2
    return multiplicar

def sumarp():
    seguir="si"
    suma=0
    contador=0
    while seguir=="si":
        numeros=int(input("Dijite un numero entero "))
        suma=suma+numeros
        seguir=input("Para seguir dijite si de lo contrario no ")
        contador=contador+1 
        promedio=suma/contador
    return promedio


print("Menu Opciones")
num1=int(input("Ingrese el numero 1 "))
num2=int(input("Ingrese el numero 2 "))

op=int(input("Ingrese la opcion segun la operacion a relizar\n1.Suma\n2.Resta\n3.Multiplicar\n4.Dividir\n5.Promedio\n6. Pro de muchos numeros\n"))
if(op==1):
    #Invocar metodo sumar
    sumar()
elif(op==2):
    #invocar metodo con parametros
    restar(num1,num2)
elif(op==3):
    #invocar un valor de retorno
    #muntiplicar(num1,num2)
    #directamente una impresion
    print(f"La multiplicacion entre {num1} y {num2} es {multiplicar(num1,num2)}")
    #guardar una variable para operarlo en otro momento
    producto=multiplicar(num1,num2)
    if(producto<50):
        print("El p es menor que 50")
    else:
        print("es mayor que 50")
elif(op==5):
    #Se debe utilizar el metodo suma
    sumar(num1,num2)#suma de los 2 numeros
    promedio=sumar(num1,num2)/2
elif(op==6):
    
    print(f"Su promedio es de {sumarp()}")
      

