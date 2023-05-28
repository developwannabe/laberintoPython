from Juego import Juego
from Director import Director

#juego = Juego()

#juego.laberinto2Entrega()

#juego.abrirPuertas()

#juego.lanzarBichos()

#juego.cerrarPuerta(3,1)#Le pasamos los números de las habitaciones que conecta la puerta

#print(juego.laberinto)

director = Director()
director.procesar('/home/lln/lab4hab4bichostunel.json')
juego = director.obtenerJuego()
print(juego.laberinto)
juego.lanzarBichos()
juego.abrirPuertas()