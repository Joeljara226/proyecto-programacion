# ========================================================
# PROYECTO: GENERADOR DE CREDENCIALES SEGURAS (CIBERSEGURIDAD)
# ASIGNATURA: INTRODUCCIÓN A LA PROGRAMACIÓN
# ========================================================

import random

# BANCOS DE CARACTERES GLOBALES
LETRAS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMEROS = "1234567890"
SIMBOLOS = "@#!%$/'()*+,-."

# --------------------------------------------------------
# F_1: FUNCIÓN PARA GENERAR LA CONTRASEÑA (Programación Funcional)
# --------------------------------------------------------
def construir_contraseña(longitud, usar_numeros, usar_simbolos):
    """
    Función pura que recibe parámetros y retorna una contraseña armada.
    Cumple con los requerimientos de la Unidad 4.
    """
    # Banco base solo con letras
    banco_caracteres = LETRAS
    
    if usar_numeros == "s":
        banco_caracteres += NUMEROS
    if usar_simbolos == "s":
        banco_caracteres += SIMBOLOS
        
    nueva_contraseña = ""
    # Tu bucle for original para armar la cadena
    for pos in range(longitud):
        if pos > 0 and pos % 4 == 0:
            nueva_contraseña += "-"
        nueva_contraseña += random.choice(banco_caracteres)
        
    return nueva_contraseña

# --------------------------------------------------------
# F_2: FUNCIÓN PARA VALIDAR ENTRADAS NUMÉRICAS (Control de Errores)
# --------------------------------------------------------
def pedir_longitud():
    """
    Gestiona el bucle de validación y captura de errores (Try-Except).
    """
    while True:
        try:
            print("\nIngrese la longitud de su contraseña deseada (mínimo 6 caracteres para seguridad):")
            longitud = int(input("-> "))
            if longitud <= 0:
                print("❌ Error: Ingrese un número entero positivo.")
            elif longitud < 6:
                print("⚠️ Advertencia: Las contraseñas de menos de 6 caracteres son inseguras.")
                return longitud
            else:
                return longitud
        except ValueError:
            print("❌ Error: Ingrese un valor numérico válido.")

# --------------------------------------------------------
# MENÚ PRINCIPAL INTERACTIVO (Estructura de Control Principal)
# --------------------------------------------------------
def programa_principal():
    respuesta = "y"
    
    print("==================================================")
    print("  SISTEMA DE GENERACIÓN DE CREDENCIALES SEGURAS   ")
    print("  Impacto: Prevención de Fraudes y Ciberataques   ")
    print("==================================================")
    
    while respuesta == "y":
        # 1. Obtener longitud validada
        conLong = pedir_longitud()
        
        # 2. Personalizar la robustez de la contraseña
        print("\n--- CONFIGURACIÓN DE SEGURIDAD ---")
        incluir_num = input("¿Desea incluir números? (s/n): ").lower()
        incluir_sim = input("¿Desea incluir símbolos/especiales? (s/n): ").lower()
        
        # 3. Llamar a la función generadora
        contraseña_final = construir_contraseña(conLong, incluir_num, incluir_sim)
        
        # 4. Mostrar resultados
        print("\n==============================================")
        print("🔑 Su contraseña generada es: " + contraseña_final)
        print("==============================================")
        
        # Pregunta de reinicio (tu lógica original)
        print("\n¿Desea generar otra contraseña? (escriba 'y' para SÍ o 'n' para NO)")
        respuesta = input("-> ").lower()
        
        if respuesta == "n":
            print("\nFin del programa. ¡Mantenga sus credenciales seguras!")

# EJECUCIÓN DEL PROYECTO
programa_principal()