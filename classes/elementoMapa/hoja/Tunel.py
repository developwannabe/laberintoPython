from classes.elementoMapa.hoja.Hoja import Hoja

class Tunel(Hoja):
    
    def __init__(self):
        super().__init__()
        self.laberinto = None

    def entrar(self,ente):
        if self.laberinto is None:
            self.laberinto = ente.juego.clonarLaberinto()
            hab = self.laberinto.obtenerHabitacion(self.padre.num)
            for hijo in hab.hijos:
                if hijo.esTunel():
                    hijo.laberinto = self.padre
        self.laberinto.entrar(ente)

    def aceptar(self,visitor):
        print("Visitar tunel")
        visitor.visitarTunel(self)

    def esTunel(self):
        return True
    
    def __str__(self):
        return "Túnel"
    
    def __repr__(self):
        return "Túnel"