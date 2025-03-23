import pygame
from settings import MAIN_CHARACTER_COLOR, MAIN_CHARACTER_HEIGHT, MAIN_CHARACTER_WIDTH

class Main_character(pygame.sprite.Sprite):
    def __init__(self, x, y):
        #This calls the constructor of the sprite
        super().__init__() 
        self.image = pygame.Surface((MAIN_CHARACTER_WIDTH, MAIN_CHARACTER_HEIGHT))  
        self.image.fill(MAIN_CHARACTER_COLOR)  
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update(self):
        keys = pygame.key.get_pressed()
        if self.rect.x>0:
            if keys[pygame.K_LEFT]:
                self.rect.x -= 5
                if self.rect.x < 0:
                    self.rect.x = 0
                    
        if self.rect.x<780:
            if keys[pygame.K_RIGHT]:
                self.rect.x += 5
                if self.rect.x > 780:
                    self.rect.x = 780  
                    
        if self.rect.y > 0:         
            if keys[pygame.K_UP]:
                self.rect.y -= 5
                if self.rect.y < 0:
                    self.rect.y = 0
             
        if self.rect.y < 580:         
            if keys[pygame.K_DOWN]:
                self.rect.y += 5
                if self.rect.y >580:
                    self.rect.y = 580
            
