import pygame
from settings import WIDTH, HEIGHT, FPS
from characters import Main_character
from platforms import Platform
from items import Apple
from particles import draw_particles, update_particles

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("CubeRoll")
        self.running = True
        self.clock = pygame.time.Clock()

        self.background_image = pygame.image.load('assets/background/Background.png')
        self.background_image = pygame.transform.scale(self.background_image,(WIDTH, HEIGHT))

        self.platforms_sprites = pygame.sprite.Group()
        self.platforms_sprites.add(Platform(0, 435.6, 48, 48))
        self.platforms_sprites.add(Platform(45, 435.6, 48, 48))
        self.platforms_sprites.add(Platform(90, 435.6, 48, 48))
        self.platforms_sprites.add(Platform(300, 435.6, 48, 48))
        self.platforms_sprites.add(Platform(345, 435.6, 48, 48))

        self.all_sprites = pygame.sprite.Group()
        self.sprite_items = pygame.sprite.Group()

        self.apple1 = Apple(30,400)
        self.sprite_items.add(self.apple1)

        self.player = Main_character(0, 390, self.platforms_sprites, self.sprite_items)
        self.all_sprites.add(self.player)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def new(self):
        self.run()
        
    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
        pygame.quit()
    
    def update(self):
        self.all_sprites.update()
        self.sprite_items.update()
        if self.player.apple_touched:
            self.sprite_items.remove(self.player.apple_touched_to_eliminate)
        update_particles()
        
    def draw(self):
        self.screen.fill((0, 0, 0)) 
        self.screen.blit(self.background_image, (0,0)) 
        self.all_sprites.draw(self.screen)
        self.sprite_items.draw(self.screen)  
        #self.player.draw_hitbox(self.screen)
        #self.apple1.draw_hitbox(self.screen)
        draw_particles(self.screen)
        for platform in self.platforms_sprites:
            self.screen.blit(platform.image, platform.rect.topleft)
            #platform.draw_hitbox(self.screen)
        pygame.display.flip() 

if __name__ == '__main__':
    game = Game()
    game.run()