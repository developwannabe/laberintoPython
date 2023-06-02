from classes.elementoMapa.contenedor.Contenedor import Contenedor

class Armario(Contenedor):
    
    def __init__(self,num):
        super().__init__(num)

    def aceptar(self,visitor):
        print("Visitar armario")
        visitor.visitarArmario(self)
        for hijo in self.hijos:
            hijo.aceptar(visitor)
        self.forma.aceptar(visitor)

    def abrir(self,ente):
        for ori in self.forma.orientaciones:
            if (pu:=ori.obtenerElementoEn(self.forma)).esPuerta():
                pu.abrir()
        
    def obtenerComandos(self,ente):
        listaComandos = []
        listaComandos.extend(self.comandos)
        if ente.posicion == self:
            for hijo in self.hijos:
                listaComandos.extend(hijo.obtenerComandos(ente))
        listaComandos.extend(self.forma.obtenerComandos(ente))
        return listaComandos
    
    def entrar(self,ente):
        ente.posicion = self 

    def esArmario(self):
        return True
    
    def __str__(self):
        return "Armario " + str(self.num)
    
    def __repr__(self):
        return "Armario" + str(self.num)