from Juego import Juego
from Director import Director
from Personaje import Personaje


director = Director()
director.procesar('/home/lln/lab4hab4bichostunel.json')
juego = director.obtenerJuego()
personaje = Personaje()
personaje.nick = "Illan"
juego.agregarPersonaje(personaje)
juego.personaje = personaje
while(True):
    print("¿Qué deseas hacer?\n    A. Atacar\n    1. Mover al norte\n    2. Mover al este\n    3. Mover al oeste\n    4. Mover al sur\n",
          "   5. Abrir Puertas\n    6. Lanzar bichos\n    H. Obtener hijos")
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
        print("Selecciona hijo: ")
        i = 0
        for hijo in hijos:
            print("    ",i,". ",hijo)
            i+=1
        el = input()
        hijos[int(el)].entrar(personaje)
        