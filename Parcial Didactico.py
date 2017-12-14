import time


if __name__ == "__main__":

    print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t PARCIAL #1 DE MECANICA ")
    nombre = input("Nombre: ")
    print("\n\n\t INSTRUCCIONES. Lea los siguientes axiomas y determine si son Cierto o Falsos (para Cierto ponga 'C' y para Falso 'F').")
    print("\t De igual forma cuando amerite, seleccione cual es la mejor respuesta a la pregunta (Solo ponga la letra).\n\n\n ")
    time.sleep(6)
    archivo = open("/Users/ryantygart/PycharmProjects/PROYECTO FINAL/Docs/Preguntass.txt", "r")



    acum = 0
    puntos = 0


#Imprime la pregunta #1
    while True:
        linea = archivo.readline()
        if acum == 0:
            print(linea)
            break

#Evalua si la respuesta ingresada por teclado es valida ('c' o 'f')
    while True:
        respuesta1 = input("\t\n RESPUESTA: ")
        if respuesta1.lower() == "f":
            print("\tRespuesta Correcta")
            break
        elif respuesta1.lower() == "c":
            print("\tRespuesta Incorrecta")
            break
        else:
            print("ERROR DE TECLA. Recuerde que usar 'c', para cierto y 'f', para falso")

#Acumulador de las respuestas correctas
    if respuesta1.lower() == "f":
        puntos = 20
    else:
        puntos =0


#-----------------------------------------------------------------------------------------------------------------------
# Imprime la pregunta #2
    print("\n\n")
    while True:
        linea = archivo.readline()
        if acum == 1:
            print(linea)
            break
        else:
            acum += 1

#Evalua si la respuesta ingresada por teclado es valida ('c' o 'f')
    while True:
        respuesta2 = input("\t\n RESPUESTA: ")
        if respuesta2.lower() == "f":
            print("\tRespuesta Incorrecta")
            break
        elif respuesta2.lower() == "c":
            print("\tRespuesta Correcta")
            break
        else:
            print("ERROR DE TECLA. Recuerde que usar 'c', para cierto y 'f', para falso")

#Acumulador de las respuestas correctas
    if respuesta2.lower() == "c":
        puntos = puntos + 20
    else:
        puntos = puntos + 0


#-----------------------------------------------------------------------------------------------------------------------
# Imprime la pregunta #3
    print("\n\n")
    while True:
        linea = archivo.readline()
        if acum == 2:
            print(linea)
            break
        else:
            acum += 1

# Evalua si la respuesta ingresada por teclado es valida ('c' o 'f')
    while True:
        respuesta3 = input("\t\n RESPUESTA: ")
        if respuesta3.lower() == "f":
            print("\tRespuesta Correcta")
            break
        elif respuesta3.lower() == "c":
            print("\tRespuesta Incorrecta")
            break
        else:
            print("ERROR DE TECLA. Recuerde que usar 'c', para cierto y 'f', para falso")


# Acumulador de las respuestas correctas
    if respuesta3.lower() == "f":
        puntos = puntos + 20
    else:
        puntos = puntos + 0


#-----------------------------------------------------------------------------------------------------------------------
#Imprime pregunta #4
    print("\n\n")
    while True:
        linea = archivo.readline()
        if acum == 3:
            print(linea)
        if acum == 4:
            print(linea)
        if acum == 5:
            print(linea)
        if acum == 6:
            print(linea)
        if acum == 7:
            print(linea)
            break
        else:
            acum += 1

# Evalua si la respuesta ingresada por teclado es valida ('a' o 'b' o 'c' o '' o'd')
    while True:
        respuesta4 = input("\t\n RESPUESTA: ")
        if respuesta4.lower() == "a":
            print("\tRespuesta Incorrecta")
            break
        elif respuesta4.lower() == "b":
            print("\tRespuesta Incorrecta")
            break
        elif respuesta4.lower() == "c":
            print("\tRespuesta Correcta")
            break
        elif respuesta4.lower() == "d":
            print("\tRespuesta Incorrecta")
            break
        else:
            print("ERROR DE TECLA. Recuerde que usar 'a', 'b', 'c', 'd'")

# Acumulador de las respuestas correctas
    if respuesta4.lower() == "c":
        puntos = puntos + 20
    else:
        puntos = puntos + 0


#-----------------------------------------------------------------------------------------------------------------------
# Imprime pregunta #5
    print("\n\n")
    while True:
        linea = archivo.readline()
        if acum == 8:
            print(linea)
        if acum == 9:
            print(linea)
        if acum == 10:
            print(linea)
        if acum == 11:
            print(linea)
        if acum == 12:
            print(linea)
            break
        else:
            acum += 1

# Evalua si la respuesta ingresada por teclado es valida ('a' o 'b' o 'c' o '' o'd')
    while True:
        respuesta5 = input("\t\n RESPUESTA: ")
        if respuesta5.lower() == "a":
            print("\tRespuesta Correcta")
            break
        elif respuesta5.lower() == "b":
            print("\tRespuesta Incorrecta")
            break
        elif respuesta5.lower() == "c":
            print("\tRespuesta Incorrecta")
            break
        elif respuesta5.lower() == "d":
            print("\tRespuesta Incorrecta")
            break
        else:
            print("ERROR DE TECLA. Recuerde que usar 'a', 'b', 'c', 'd'")

# Acumulador de las respuestas correctas
    if respuesta5.lower() == "a":
        puntos = puntos + 20
    else:
        puntos = puntos + 0



    print("\n\n\n\t\t",nombre,"su calificación es:", puntos,"/100")


    archivo.close()
