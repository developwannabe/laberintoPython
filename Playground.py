from Juego import Juego
from Director import Director
from Personaje import Personaje

#juego = Juego()

#juego.laberinto2Entrega()

#juego.abrirPuertas()

#juego.lanzarBichos()

#juego.cerrarPuerta(3,1)#Le pasamos los números de las habitaciones que conecta la puerta

#print(juego.laberinto)

director = Director()
director.procesar('/home/lln/lab4hab4bichostunel.json')
juego = director.obtenerJuego()
personaje = Personaje()
personaje.nick = "Illan"
personaje.juego=juego
hab = juego.obtenerHabitacion(1)
hab.entrar(personaje)
juego.personaje = personaje
print(juego.laberinto)
#juego.lanzarBichos()
juego.abrirPuertas()
personaje.atacar()
personaje.irAlEste()
personaje.atacar()
personaje.irAlSur()
personaje.atacar()
personaje.irAlOeste()
personaje.atacar()
print()