from classes.comando.Comando import Comando

class Abrir(Comando):

    def ejecutar(self,ente):
        self.receptor.abrir(ente)

    def esAbrir(self):
        return True
    
    def __str__(self):
        return "Abrir " + str(self.receptor)
    
    def __repr__(self):
        return "Abrir " + str(self.receptor)
    
    def equals(self,comando):
        if comando.esAbrir():
            return True
        return False