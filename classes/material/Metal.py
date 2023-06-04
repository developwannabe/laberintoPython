from classes.material.Material import Material

class Metal(Material):

    def __init__(self):
        self.poder = 20
        self.usos = 5

    def esMetal(self):
        return True
    
    def __str__(self):
        return "Metal"
    
    def __repr__(self):
        return "Metal"