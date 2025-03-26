import pygame

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.image.load("assets/terrain/Ground_surface.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))  
        self.rect = self.image.get_rect(topleft=(x, y))

        self.hitbox = pygame.Surface((width, height - 10))
        self.rect_hitbox = self.hitbox.get_rect()
        self.rect_hitbox.topleft = (x, y + 3)

    def draw_hitbox(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect_hitbox, 2)