from classes.comando.Comando import Comando

class Cerrar(Comando):

    def ejecutar(self,ente):
        self.receptor.cerrar(ente)

    def esCerrar(self):
        return True
    
    def __str__(self):
        return "Cerrar " + str(self.receptor)
    
    def repr(self):
        return "Cerrar " + str(self.receptor)
    
    def equals(self,comando):
        if comando.esCerrar():
            return True
        return False