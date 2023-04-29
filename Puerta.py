from ElementoMapa import ElementoMapa

class Puerta(ElementoMapa):

    def __init__(self): 
        super().__init__()
        self.abierta = False
        self.lado1 = None
        self.lado2 = None

    def entrar(self):
        if self.abierta:
            print("Puedes pasar al otro lado.")
        else:
            print("La puerta está cerrada.")

    def abrir(self):
        self.abierta = True
    
    def esPuerta(self):
        return True

    def __str__(self):
        return "Puerta: Lado 1 es Hab " + str(self.lado1.num) +", Lado 2 es hab " + str(self.lado2.num) + '. Abierta: ' +str(self.abierta)
    
    def __repr__(self):
        return "Puerta: Lado 1 es Hab " + str(self.lado1.num) +", Lado 2 es hab " + str(self.lado2.num) + '. Abierta: ' +str(self.abierta)
