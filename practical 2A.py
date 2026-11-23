import pygame 
from pygame.locals import * 

pygame.init() 
window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Aditya 40")

window.fill((255, 255, 255)) 
pygame.draw.line(window, (0, 0, 0), [100, 300], [500, 300], 5)

pygame.display.update() 
