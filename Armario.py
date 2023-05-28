from Contenedor import Contenedor

class Armario(Contenedor):
    
    def __init__(self,num):
        super().__init__(num)

    def entrar(self,ente):
        print("Estás en un armario")

    def esArmario(self):
        return True
    
    def __str__(self):
        return "Armario " + str(self.num)
    
    def __repr__(self):
        return "Armario" + str(self.num)