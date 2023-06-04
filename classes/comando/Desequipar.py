from classes.comando.Comando import Comando

class Desequipar(Comando):

    def ejecutar(self,ente):
        self.receptor.desequipar(ente)

    def esDesequipar(self):
        return True
    
    def __str__(self):
        return "Desequipar " + str(self.receptor)
    
    def equals(self,comando):
        if comando.esDesequipar():
            return True
        return False