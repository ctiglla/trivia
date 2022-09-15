import random  # Importamos la librería random
import time

# Para implementar puntajes, crearemos una nueva variable llamada "puntaje", la que inicializamos en 0.
puntaje = random.randint(1, 10)
iniciar_trivia = True
intentos = 0
puntajes = []

#Constantes de Colores
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

# Lo primero es mostrar en pantalla el texto de bienvenida para quien juegue tu trivia
print(GREEN)
print(("BIENVENIDO A TRIVIANIME").center(50, "="))
print("Pondremos a prueba tus conocimientos")
print("Te regalo", puntaje, "puntos")

# Agregaremos personalización para nuestros jugadores, preguntando y almacenando sus nombres en una variable
time.sleep(0.5)
nombre = (input(YELLOW + "Ingresa tu nombre: ")).upper()

if nombre == "":
    nombre = "Sin nombre"
print("こんにちは", nombre)
while True:
    edad = (input("Escribe tu edad: "))
    try:
        edad = int(edad)
        break
    except ValueError:
        print("La edad es un numero entero")

# Es importante dar instrucciones sobre cómo jugar:
# Ahora, lo personalizaremos con el nombre del jugador, diciéndole a print() que muestre el contenido de la variable "nombre". Cada cosa distinta que queremos que muestre en la pantalla, la separamos con comas
while iniciar_trivia == True:
    print(
        BLUE + "\nHola", nombre,
        "responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n",
        "Empezamos...")

    #Cuenta regresiva
    for i in range(5, 0, -1):
        print(i)
        time.sleep(1)

    print("")
    # Pregunta 1
    print("1) ¿Dónde nació Naruto Uzumaki?")
    print("a) Namekusei")
    print("b) Konoha")
    print("c) País del Fuego")
    print("d) Japón")

    # Almacenamos la respuesta del usuario en la variable "respuesta_1"
    respuesta_1 = input(YELLOW + "\nTu respuesta: ")

    while respuesta_1 not in ("a", "b", "c", "d", "x"):
        respuesta_1 = input(
            "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

    # Ahora, verificamos su respuesta para mandar un mensaje de acierto o de error
    if respuesta_1 == "a":
        print(
            RED + "Incorrecto!", nombre,
            "Namekusei es un planeta de la serie de manga y anime de Dragon Ball "
        )
        puntaje -= random.randint(10, 20)
    elif respuesta_1 == "c":
        print(RED + "Bien!", nombre, " pero pudiste ser más específico")
        puntaje += random.randint(5, 15)
    elif respuesta_1 == "d":
        print(RED + "Incorrecto!", nombre,
              "Japón es es un país insular de Asia Oriental")
        puntaje /= random.randint(2, 10)
    elif respuesta_1 == "x":
        print(CYAN + "Soy el más perron aquí!")
        puntaje += 1000
    else:
        puntaje += random.randint(100, 200)
        print(CYAN + "Muy bien", nombre,
              ", Naruto nació en la Aldea Oculta Entre las Hojas! ")

    print(MAGENTA + nombre, "llevas", int(puntaje), "puntos")

    time.sleep(1)
    # Pregunta 2
    print(BLUE + "\n1) ¿Cual es la técnica representativa de Goku?")
    print("a) Dodonpa")
    print("b) Genkidama")
    print("c) Kaiō Ken")
    print("d) Kame Hame Ha")

    # Almacenamos la respuesta del usuario en la variable "respuesta_2"
    respuesta_2 = input(YELLOW + "\nTu respuesta: ")

    while respuesta_2 not in ("a", "b", "c", "d", "2"):
        respuesta_2 = input(
            "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

    # Ahora, verificamos su respuesta para mandar un mensaje de acierto o de error
    if respuesta_2 == "a":
        print(
            RED + "Incorrecto!", nombre,
            "Esta es la utilizada por Tao Pai Pai para matar a Goku que se salva gracias a una esferadel Dragon"
        )
        puntaje -= random.randint(1, 20)
    elif respuesta_2 == "b":
        print(
            RED + "Muy poderosa,",
            "esta técnica es aprendida de Kaio del Norte, Al menos es de Goku")
        puntaje += random.randint(3, 10)
    elif respuesta_2 == "c":
        print(
            RED + "Utilizada, pero no es la mas representativa", nombre,
            "esta es la técnica que aprende Son Goku en el planeta de Kaiosama"
            + CYAN)
        puntaje *= random.randint(10, 12)
    elif respuesta_2 == "2":
        wow = int(respuesta_2)
        print(
            wow,
            "y",
            wow,
            "son",
            wow + wow,
            wow + wow,
            "y",
            wow,
            "son",
            wow + wow + wow,
            wow + wow + wow,
            "y",
            wow,
            "son",
            wow + wow + wow + wow,
            "y",
            wow + wow + wow + wow,
            wow + wow + wow + wow + wow + wow + wow + wow,
        )
        puntaje += 1000
    else:
        puntaje += random.randint(100, 200)
        print(
            CYAN + "Muy bien", nombre,
            "Es la técnica que aprende Goku del Maestro Roshi al apagar el incendio en el palacio de Ox-Satán"
        )

    print(MAGENTA + nombre, "llevas", int(puntaje), "puntos")

    time.sleep(1)
    # Pregunta 3
    print(BLUE + "\n1) ¿En que año se emitio el primer episodio de one piece?")
    print("a) 1999")
    print("b) 1821")
    print("c) 2022")
    print("d) 2000")

    # Almacenamos la respuesta del usuario en la variable "respuesta_3"
    respuesta_3 = input(YELLOW + "\nTu respuesta: ")

    while respuesta_3 not in ("a", "b", "c", "d", "y"):
        respuesta_3 = input(
            "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

    if respuesta_3 == "b":
        print(
            RED +
            "Totalmente incorrecto!. No se publicaba ni siquiera el manga de One Piece, como dato este es el año de independencia del Perú"
        )
        puntaje /= random.randint(1, 100)
    elif respuesta_3 == "c":
        print(
            RED +
            "Incorrecto!. Es el año actual y ya lleva emitiendose más de 2 décadas"
        )
        puntaje -= random.randint(1, 10)
    elif respuesta_3 == "d":
        print(RED +
              "Por poco, vamos a darte algo por ser un hombre de Cultura")
        puntaje += random.randint(30, 50)
    elif respuesta_3 == "y":
        print(CYAN + "Gomu gomu no...")
        puntaje += 1000
    else:
        print(
            CYAN +
            "Correcto! El anime es producido por Toei Animation, y emitido en Japón en Fuji TV desde el 20 de octubre de 1999 hasta la actualidad"
        )
        puntaje += random.randint(100, 150)
    print(MAGENTA + nombre, "llevas", int(puntaje), "puntos")
    time.sleep(1)

    print("BONUS")
    extra = 0
    for i in range(1, 6):
        a = random.randint(0, 100)
        print("+", a)
        time.sleep(0.5)
        extra += a
    print("Total BONUS +", extra)
    puntaje += extra

    print("\nLLevas", intentos, "intentos")

    print("\n¿Deseas intentar la trivia nuevamente?")
    repetir_trivia = input(
        "Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower(
        )
    intentos += 1

    if repetir_trivia != "si":
        iniciar_trivia = False
    else:

        puntajes.append(puntaje)
        puntaje = 0

if len(puntajes) > 0:
    for i in range(0, len(puntajes)):
        print(MAGENTA + "Gracias", nombre,
              "por jugar mi trivia, Tu puntaje en la ronda", i + 1, "fue",
              int(puntajes[i]))
else:
    print(MAGENTA + "Gracias", nombre, "por jugar mi trivia, alcanzaste",
          int(puntaje), "puntos")

print("\nEspero", nombre, "que lo hayas pasado bien, hasta pronto!")
