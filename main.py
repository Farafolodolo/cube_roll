import pygame
from settings import WIDTH, HEIGHT, FPS
from character import Main_character

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("CubeRoll")
        self.running = True
        self.clock = pygame.time.Clock()
        
        # Grupo de sprites para manejar todos los objetos del juego
        self.all_sprites = pygame.sprite.Group()
        
        # Crear el personaje principal y agregarlo al grupo
        self.player = Main_character(50, 50)
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
        
    def draw(self):
        self.screen.fill((0, 0, 0))  
        self.all_sprites.draw(self.screen)  
        pygame.display.flip() 

if __name__ == '__main__':
    game = Game()
    game.run()