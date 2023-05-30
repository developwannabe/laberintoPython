from classes.Comando import Comando

class Entrar(Comando):

    def ejecutar(self,ente):
        self.receptor.entrar(ente)

    def esEntrar(self):
        return True
    
    def __str__(self):
        return "Entrar en " + str(self.receptor)