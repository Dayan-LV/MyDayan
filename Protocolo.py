#López Valderrabano Josahani Dayan 4IM10

def menu():

    print("""
                        MENÚ
        1.- Ordenar
        2.- Longitud
        3.- Añadir elemento
        4.- Borrar un elemento
        5.- Salir
        """)
cantidad = int(input("Escribir con números la cantidad de elementos que desea ingresar: "))
inci = []
cont = []
x = 0
lis=[1]
while x <= cantidad:
    inc=int(input("Ingrese el inciso: "))
    inci.append(inc)
    con=str(input("Ingrese el contenido : "))
    cont.append(con)
    x = x+1
while True:
    menu()
    opcion = int(input("Introduce la opcion deseada a realizar del Menú : "))
    rang1=len(inci)
    rang2=len(cont)
    if opcion == 1:
        juntas = list(zip(inci,cont))
        print("El orden del protocolo es es : ")
        print("")
        print(juntas)
    elif opcion == 2:
        print("La lognitud del protocolo es : ",str(len(inci)))  
    elif opcion==3:
        print("Elemento a añadir")
        loca=int(input("Inciso: "))
        con2=input("Contenido: ")
        cont.insert(loca,str(con2))
        print(cont)
    elif opcion==4:
        delete=int(input("Inciso a eliminar: "))
        inci.pop(delete)
        print(inci)
        delete2=int(input("Inciso a eliminar de contenido: "))
        cont.pop(delete2)
        print(cont)
    elif opcion==5:
        print("Muchas gracias, hasta luego")
        break
    else:
        print("Opción incorrecta")
        break
