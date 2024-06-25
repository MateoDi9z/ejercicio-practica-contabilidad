from lib import *

# =======================================
# |      Creado por Mateo Diaz :)       #
# |  Contactame cualquier duda o idea.  #
# =======================================

# TODO: Pone aca tu nombre!
NOMBRE = "Mateo" # <-

def main():
    """ ### Sistema de contabilidad """

    print("\nBienvenido a el sistema de contabilidad!")
    print(f"de: {NOMBRE}")

    while True:
        print("\nMENU: Elija una opción! \n")
        print(" 1 - Crear entrada")
        print(" 2 - Crear salida")
        # Ejemplo: print(" 3 - Ver los ingresos")
        # TODO: Crea el resto de opciones aca :)

        print(" 3 - Salir")
        
        entrada = input("> ")
        print("")

        # TODO: Definí una función para resolver cada opción (Abajo de todos los ifs)

        # TODO: Crea todas las opciones necesarias aca!
        if entrada == "1":
            # TODO: Aca llama a la función para resolver el ejercicio!
            # (Y borra el print una vez hecho)
            print("Not implemented!")
            # Ejemplo: crear_entrada()
        elif entrada == "2":
            print("Not implemented!")
        else:
            break


#####################################
# * Implementa tus funciones aca! * #
#####################################

# Ejemplo: def crear_entrada():

main()  # <- Deja esto en la ultima linea del código!