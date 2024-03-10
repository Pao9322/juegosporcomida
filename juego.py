# Importa la clase Personaje del módulo personaje

from personaje import Personaje
import random

# Muestra un mensaje de bienvenida y solicita el nombre del jugador
print("¡Bienvenido a Gran Fantasía!")
nombre = input("Por favor indique nombre de su personaje: \n")

# Crea una instancia de la clase Personaje con el nombre proporcionado
p = Personaje(nombre)

# Muestra el estado inicial del personaje
print(p.estado)

# Crea un personaje Orco y calcula la probabilidad de ganar contra él
print("\n¡Oh no!, ¡Ha aparecido un Orco!")
o = Personaje("Orco")
probabilidad_ganar = p.get_probabilidad_ganar(o)

# Muestra un diálogo con opciones y entra en un bucle mientras la opción seleccionada sea 1
opcion_orco = Personaje.mostrar_dialogo_opcion(probabilidad_ganar)
while opcion_orco == 1:

# Genera un resultado aleatorio (G: ganar, p: perder) basado en la probabilidad de ganar
    resultado = "G" if random.uniform < probabilidad_ganar else "p"

# Realiza acciones basadas en el resultado
    if resultado == "G":
        print(
            "\n ¡Le has ganado al Orco, felicidades!\n"
            "Recibirás 50 pntos de experiencia! \n"
         )
        p.estado = 50
        o.estado = -30

    else:
        print(
            "\n ¡Oh no!¡El Orco te ha ganado! \n"
            "Has perdido 30 puntos de experiencia! \n"
        )
        p.estado = -30
        o.estado = 50

 # Muestra el estado actualizado de ambos personajes
    print(p.estado)
    print(o.estado)

# Calcula la nueva probabilidad de ganar contra el Orco
    probabilidad_ganar = p.get_probabilidad_ganar(o)

# Muestra un diálogo con opciones y actualiza la opción seleccionada
    opcion_orco = Personaje.mostrar_dialogo_opcion(probabilidad_ganar)