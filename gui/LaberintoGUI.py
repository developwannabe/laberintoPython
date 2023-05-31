import pygame
import time
class LaberintoGUI():
    
    def __init__(self,largo,ancho):
        self.largo = largo
        self.ancho = ancho
        self.ventana = None
        self.fps = 30
        pygame.init()
        clock = pygame.time.Clock()
        clock.tick(self.fps)
    
    def crearVentana(self):
        self.ventana = pygame.display.set_mode((self.largo,self.ancho))
        pygame.display.set_caption("No banana, no monkey")
        self.ventana.fill((255,255,255))
    
    def ejecutar(self):
        while True:
            pygame.display.update()

    def terminar(self):
        pygame.quit()

lab = LaberintoGUI(1000,800)
lab.crearVentana()
lab.ejecutar()