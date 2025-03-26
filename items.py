import pygame
from utils import load_frames

class Apple(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.animation = pygame.image.load("assets/items/Apple.png")
        self.animations = load_frames(self.animation, 32, 32, 17)

        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

        self.image = pygame.transform.flip(self.animations[self.frame_index], False, False)

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.hitbox = pygame.Surface((22,22))
        self.rect_hitbox = self.hitbox.get_rect()
        self.rect_hitbox.topleft = (x+10, y+7)

    def update(self):
        self.animation_moving()

    def animation_moving(self):
        cooldown_animation = 50  
        current_time = pygame.time.get_ticks()

        if current_time - self.update_time >= cooldown_animation:
            self.frame_index = (self.frame_index + 1) % len(self.animations)
            self.update_time = current_time
        
        self.image = self.animations[self.frame_index]

    def draw_hitbox(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect_hitbox, 2)