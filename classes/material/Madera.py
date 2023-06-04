from classes.material.Material import Material

class Madera(Material):

    def __init__(self):
        self.poder = 10
        self.usos = 2

    def esMadera(self):
        return True
    
    def __str__(self):
        return "Madera"
    
    def __repr__(self):
        return "Madera"