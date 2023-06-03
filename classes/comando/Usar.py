from classes.comando.Comando import Comando

class Usar(Comando):
    
    def ejecutar(self,ente):
        self.receptor.usar(ente)

    def esUsar(self):
        return True
    
    def equals(self, com):
        if com.esUsar():
            return True
        return False
    
    def __str__(self):
        return "Usar " + str(self.receptor)
    
    def __repr__(self):
        return "Usar " + str(self.receptor)