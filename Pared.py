from ElementoMapa import ElementoMapa

class Pared(ElementoMapa):
    
    def entrar(self):
        print("Te has chocado con una pared.")

    def esPared(self):
        return True
    
    def __str__(self):
        return "Pared"
    
    def __repr__(self):
        return "Pared"