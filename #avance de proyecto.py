 #avance de proyecto
conLong = 0 # se inicia un valor entero que representa la longitud de la contraseña
letras = ("abcdefghi")
numeros = ("123456789")
simbolos = "@#!%$/'"
caracteres = letras + numeros + simbolos #se unen los 3 grupos para formar un banco de caracterres disponibles
contraseña = "" # la variable contraseña se inicializa como vacio
while conLong <=0  :
    try:
        print("Ingrese la longitud de su contraseña deseada:") # pide al usuario un numero entero para la longitud de la contraseña
        conLong = int(input()) #el sistema lee el valor ingresado
        if conLong <=0 : #validacion si el valor es positivo
          print("ingrese un numero entero positivo") # imprime un mensaje y se repite el bucle
    except ValueError:
     print("ingrese un valor valido")
     # enlace video
     #https://www.loom.com/share/b3d760e5fd374bd2b5504a38ffde1474