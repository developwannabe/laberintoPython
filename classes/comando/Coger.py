from classes.comando.Comando import Comando

class Coger(Comando):
    
    def ejecutar(self,ente):
        self.receptor.entrar(ente)

    def esCoger(self):
        return True
    
    def equals(self, com):
        if com.esCoger():
            return True
        return False
    
    def __str__(self):
        return "Coger " + str(self.receptor)
    
    def __repr__(self):
        return "Coger " + str(self.receptor)