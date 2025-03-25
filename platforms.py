import pygame

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.image.load("assets/terrain/Ground_surface.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))  
        self.rect = self.image.get_rect(topleft=(x, y))