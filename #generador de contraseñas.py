# generador de contraseñas
import random
conLong = 0
letras = ("abcdefghi")
numeros = ("123456789")
simbolos = "@#!%$/'"
respuesta= "y"
caracteres = letras + numeros + simbolos #se unen los 3 grupos para formar un banco de caracterres disponibles
contraseña = "" # la variable contraseña se inicializa como vacio

# El  while continuará mientras conLog sea positivo.
while respuesta=="y" :
   while conLong <=0  :
    try:
        print("Ingrese la longitud de su contraseña deseada:") # pide al usuario un numero entero para la longitud de la contraseña
        conLong = int(input()) #el sistema lee el valor ingresado
        if conLong <=0 : #validacion si el valor es positivo
          print("ingrese un numero entero positivo") # imprime un mensaje y se repite el bucle
    except ValueError:
     print("ingrese un valor valido")

   for pos in range(conLong):
     contraseña= contraseña + random.choice(caracteres) #se itera consetraseña con nuevos carateres con la libreria random
#en el for se ingresa un caracter hasta que alcance al numero ingresado en conLog
   print("su contraseña es: " + contraseña)
   conLong=0
   contraseña=""
   #se limpian las respuestas para el segundo while
   print("desea generar otra contraseña? (escriba y para si y n para no)")
   #pregunta si quiere reinicar el programa
   respuesta = input() #lee la respuesta
   if respuesta =="n":#valida la respuesta
    print("fin del programa")
   #fin del programa
   # video codigo
   # https://www.loom.com/share/84bee7ad93ea4099a12036ddca671c5a

