#proyecto generador de contraseñas segura
#Logica de programacion
import random
#lote de caracteres dividido por numeros letas y simbolos
LETRAS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMEROS = "1234567890"
SIMBOLOS = "@#!%$/'()*+,-."

#funcion para generar la contraseña

def construir_contraseña(longitud, usar_numeros, usar_simbolos):
    """ Función pura que recibe parámetros y retorna una contraseña armada """
    #lote de caracteres
    banco_caracteres = LETRAS
    if usar_numeros == "s":
        banco_caracteres += NUMEROS
    if usar_simbolos == "s":
        banco_caracteres += SIMBOLOS    
    nueva_contraseña = ""
    for pos in range(longitud):
        if pos > 0 and pos % 4 == 0:
            nueva_contraseña += "-"
        nueva_contraseña += random.choice(banco_caracteres)   
    return nueva_contraseña

#funcion para validar la longitud

def pedir_longitud():
    """Gestiona el bucle de validación y captura de errores"""
    while True:
        try:
            print("Ingrese la longitud de su contraseña deseada mínimo 6 caracteres para seguridad")
            longitud = int(input())
            if longitud <= 0:
                print(" Ingrese un número entero positivo")
            elif longitud < 6:
                print("por seguridad las contraseñas deben ser mayores a 6 caracteres")
                continue  
            else:
                return longitud
        except ValueError:
            print("Ingrese un numero entero positivo")
            
#menu

def programa_principal():
    respuesta = "y"
    print("  sistema de generacion de credenciales seguras  ")
    while respuesta == "y":
        #se obtiene una longitud validada
        conLong = pedir_longitud()
        #se personalisa la solidez de la contraseña
        print("CONFIGURACIÓN DE SEGURIDAD")
        incluir_num = input("¿Desea incluir números? (s para si n para no) ").lower() 
        #.lower convierte un caracter en mayuscula a minuscula para poder continuar con el programa
        #sin importar si el usuario imgresa una letra mayuscula
        incluir_sim = input("¿Desea incluir caracteres especiales? (s para si n para no) ").lower()
        #Llamar a la función que genera la contraseña
        contraseña_final = construir_contraseña(conLong, incluir_num, incluir_sim)
        #se llama a contruir contraseña con los parametros de longitud de la contraseña
        #asi como si desea incluir numero y caracteres especiales
        #imprimir resultados
        print("Su contraseña es" + contraseña_final)
        #el while externo pregunta si quier geberar una nueva contraseña 
        print("¿Desea generar otra contraseña? (escriba 'y' para SÍ o 'n' para NO)")
        respuesta = input().lower()
        if respuesta == "n":
            print("Fin del programa")

#ejecucion del programa
programa_principal()