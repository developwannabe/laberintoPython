from classes.comando.Comando import Comando

class Soltar(Comando):
    
    def ejecutar(self,ente):
        self.receptor.soltar(ente)

    def esSoltar(self):
        return True
    
    def equals(self, com):
        if com.esSoltar():
            return True
        return False
    
    def __str__(self):
        return "Soltar " + str(self.receptor)
    
    def __repr__(self):
        return "Soltar " + str(self.receptor)