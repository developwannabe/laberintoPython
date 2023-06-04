from classes.comando.Comando import Comando

class Entrar(Comando):

    def ejecutar(self,ente):
        self.receptor.entrar(ente)

    def esEntrar(self):
        return True
    
    def __str__(self):
        return "Entrar en " + str(self.receptor)
    
    def __repr__(self):
        return "Entrar en " + str(self.receptor)
    
    def equals(self,comando):
        if comando.esEntrar():
            return True
        return False