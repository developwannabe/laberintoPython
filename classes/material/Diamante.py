from classes.material.Material import Material

class Diamante(Material):

    def __init__(self):
        self.poder = 30

    def esDiamante(self):
        return True
    
    def __str__(self):
        return "Diamante"
    
    def __repr__(self):
        return "Diamante"