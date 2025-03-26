import pygame
from settings import MAIN_CHARACTER_SPEED, MAIN_CHARACTER_SCALE, GRAVITY, MAIN_CHARACTER_JUMP
from utils import scale_img, load_frames

class Main_character(pygame.sprite.Sprite):
    def __init__(self, x, y, platforms, apples):
        super().__init__() 
        self.run_image = pygame.image.load("assets/main_character/Run.png").convert_alpha()
        self.animations = load_frames(self.run_image, 32, 32, 12)
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

        self.live = 75

        self.flip = False
        self.image = pygame.transform.flip(self.animations[self.frame_index], self.flip, False)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.hitbox = pygame.Surface((34,34))
        self.rect_hitbox = self.hitbox.get_rect()
        self.rect_hitbox.topleft = (x+4,y+5)

        self.platforms = platforms
        self.vel_y = 0 
        self.on_ground = False 

        self.apples = apples
        self.inventory = []
        self.apple_touched = False
        self.apple_touched_to_eliminate = object

    def update(self):
        self.update_keys()
        self.collides()

    def update_keys(self):
        keys = pygame.key.get_pressed()
        running = False 

        prev_x = self.rect.x
        prev_y = self.rect.y  

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

        self.vel_y += GRAVITY  
        if self.vel_y > 5: 
            self.vel_y = 5  

        if keys[pygame.K_SPACE] and self.on_ground:
            self.vel_y = -MAIN_CHARACTER_JUMP 

        if keys[pygame.K_k]:
            print('The inventory: ', len(self.inventory))
            print('The live: ', self.live)

        if keys[pygame.K_h]:
            if self.inventory:
                if self.live < 100:
                    self.live += 25
                if self.live > 100:
                    self.live = 100
                
                self.inventory.pop(0)
        
                

        self.rect.y += self.vel_y
        self.rect_hitbox.y += self.vel_y

        self.on_ground = False
        for platform in self.platforms:
            if self.rect_hitbox.colliderect(platform.rect_hitbox):  
                if self.vel_y > 0 and prev_y + self.rect.height <= platform.rect_hitbox.top:
                    self.rect.bottom = platform.rect_hitbox.top
                    self.rect_hitbox.bottom = platform.rect_hitbox.top
                    self.vel_y = 0 
                    self.on_ground = True
                elif prev_x + self.rect.width <= platform.rect.left:  
                    self.rect.right = platform.rect.left
                    self.rect_hitbox.right = platform.rect.left
                elif prev_x >= platform.rect.right: 
                    self.rect.left = platform.rect.right
                    self.rect_hitbox.left = platform.rect.right

        if running:
            self.run_animation()
        else:
            self.frame_index = 0
            self.image = pygame.transform.flip(self.animations[self.frame_index], self.flip, False)

    def collides(self):
        self.apple_touched = False
        for apple in self.apples:
            if self.rect_hitbox.colliderect(apple.rect_hitbox):
                if len(self.inventory) < 3:
                    self.inventory.append(apple)
                    self.apple_touched_to_eliminate = apple
                    self.apple_touched = True

    def run_animation(self):
        cooldown_animation = 50  
        current_time = pygame.time.get_ticks()

        if current_time - self.update_time >= cooldown_animation:
            self.frame_index = (self.frame_index + 1) % len(self.animations)
            self.update_time = current_time

        self.image = pygame.transform.flip(self.animations[self.frame_index], self.flip, False)  

    def draw_hitbox(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect_hitbox, 2)