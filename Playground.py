from classes.builder.Director import Director
from classes.ente.Personaje import Personaje
from classes.juego.Juego import Juego
#from classes.laberintoFactory.LaberintoFactory import LaberintoFactory
#from classes.laberintoFactory.LaberintoBombasFactory import LaberintoBombasFactory


director = Director()
director.procesar('json/lab4hab4bichostunel.json')
juego = director.obtenerJuego()
nombre = input("Nick del personaje: ")
personaje = Personaje()
personaje.nick = nombre
juego.agregarPersonaje(personaje)
juego.personaje = personaje
while(True):
    print("¿Qué deseas hacer?\n    A. Atacar\n    1. Mover al norte\n    2. Mover al este\n    3. Mover al oeste\n    4. Mover al sur\n",
          "   5. Abrir Puertas\n    6. Lanzar bichos\n    H. Obtener hijos de la posición del personaje\n",
          "   C. Obtener Comandos")
    eleccion=input()
    if eleccion == "1":
        personaje.irAlNorte()
    if eleccion == "2":
        personaje.irAlEste()
    if eleccion == "3":
        personaje.irAlOeste()
    if eleccion == "4":
        personaje.irAlSur()
    if eleccion == "5":
        juego.abrirPuertas()
    if eleccion == "6":
        juego.lanzarBichos()
    if eleccion == "a" or eleccion == "A":
        personaje.atacar()
    if eleccion == "h" or eleccion == "H":
        hijos = juego.obtenerHijosPosicion()
        if len(hijos) > 0:
            print("Selecciona hijo: ")
            i = 0
            for hijo in hijos:
                print("    ",i,". ",hijo)
                i+=1
            el = input()
            el = int(el)
            if el < len(hijos) and el >= 0:
                hijos[el].entrar(personaje)
            else:
                print("Has introducido un índice incorrecto.")
        else:
            print("No hay hijos disponibles.")

    if eleccion == "c" or eleccion == "C":
        coms = personaje.obtenerComandos()
        if len(coms) > 0:
            print("Selecciona comando: ")
            i = 0
            for com in coms:
                print("    ",i,". ",com)
                i+=1
            el = input()
            el = int(el)
            if el < len(coms) and el >= 0:
                coms[el].ejecutar(personaje)
            else:
                print("Has introducido un índice incorrecto.")
        else:
            print("No hay comandos disponibles.")
'''
juego = Juego()
af = LaberintoBombasFactory()
juego.laberinto2EntregAF(af)
print(juego.laberinto)'''

