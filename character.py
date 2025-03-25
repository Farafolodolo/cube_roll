import pygame
from settings import MAIN_CHARACTER_HEIGHT, MAIN_CHARACTER_WIDTH, MAIN_CHARACTER_SPEED, MAIN_CHARACTER_SCALE
from utils import scale_img

class Main_character(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__() 
        self.run_image = pygame.image.load("assets/main_character/Run.png").convert_alpha()
        self.animations = self.load_frames(self.run_image, 32, 32, 12)
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

        self.flip = False
        self.image = pygame.transform.flip(self.animations[self.frame_index], self.flip, False)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.hitbox = pygame.Surface((34,34))
        self.rect_hitbox = self.hitbox.get_rect()
        self.rect_hitbox.topleft = (x+4,y+5)
        
    def update(self):
        self.update_position()

    def update_position(self):
        keys = pygame.key.get_pressed()
        running = False 

        if keys[pygame.K_LEFT]:
            self.rect.x -= MAIN_CHARACTER_SPEED
            self.rect_hitbox.x -= MAIN_CHARACTER_SPEED
            self.flip = True 
            running = True
            if self.rect.x < 0:
                self.rect.x = 0
                self.rect_hitbox.x = self.rect.x + 4

        if keys[pygame.K_RIGHT]:
            self.rect.x += MAIN_CHARACTER_SPEED
            self.rect_hitbox.x += MAIN_CHARACTER_SPEED
            self.flip = False  
            running = True
            if self.rect.x > 758.4:
                self.rect.x = 758.4 
                self.rect_hitbox.x = self.rect.x + 4
        
        if running:
            self.run_animation()
        else:
            self.frame_index = 0
            self.image = pygame.transform.flip(self.animations[self.frame_index], self.flip, False)

    def run_animation(self):
        cooldown_animation = 50  
        current_time = pygame.time.get_ticks()

        if current_time - self.update_time >= cooldown_animation:
            self.frame_index = (self.frame_index + 1) % len(self.animations)
            self.update_time = current_time

        self.image = pygame.transform.flip(self.animations[self.frame_index], self.flip, False)

    def load_frames(self, sheet, frame_width, frame_height, num_frames):
        frames = []
        for i in range(num_frames):
            rect = pygame.Rect(i * frame_width, 0, frame_width, frame_height)
            frame = sheet.subsurface(rect)
            frame = scale_img(frame, MAIN_CHARACTER_SCALE)
            frames.append(frame)
        return frames  

    def draw_hitbox(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect_hitbox, 2)