import pygame
from settings import WIDTH, HEIGHT, FPS
from characters import Main_character
from platforms import Platform

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("CubeRoll")
        self.running = True
        self.clock = pygame.time.Clock()

        self.platforms_sprites = pygame.sprite.Group()
        self.platforms_sprites.add(Platform(0, 435.6, 48, 48))
        self.platforms_sprites.add(Platform(45, 435.6, 48, 48))
        self.platforms_sprites.add(Platform(91, 435.6, 48, 48))

        self.all_sprites = pygame.sprite.Group()
        self.player = Main_character(0, 390, self.platforms_sprites)
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
        update_particles()
        
    def draw(self):
        self.screen.fill((0, 0, 0))  
        self.all_sprites.draw(self.screen)  
        self.player.draw_hitbox(self.screen)
        pygame.display.flip() 

if __name__ == '__main__':
    game = Game()
    game.run()