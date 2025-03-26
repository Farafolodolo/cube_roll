import pygame
from settings import WIDTH, HEIGHT, FPS
from characters import Main_character, Enemies
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
        self.platforms_sprites.add(Platform(390,  435.6, 48, 48))
        self.platforms_sprites.add(Platform(435,  435.6, 48, 48))
        self.platforms_sprites.add(Platform(480,  435.6, 48, 48))
        self.platforms_sprites.add(Platform(525,  435.6, 48, 48))
        self.platforms_sprites.add(Platform(570,  435.6, 48, 48))
        self.platforms_sprites.add(Platform(615,  435.6, 48, 48))
        self.platforms_sprites.add(Platform(660,  435.6, 48, 48))
        self.platforms_sprites.add(Platform(705,  435.6, 48, 48))
        self.platforms_sprites.add(Platform(750,  435.6, 48, 48))

        self.all_sprites = pygame.sprite.Group()
        self.sprite_items = pygame.sprite.Group()
        self.sprite_enemies = pygame.sprite.Group()

        self.apple1 = Apple(30,400)
        self.sprite_items.add(self.apple1)

        self.enemie1 = Enemies(750, 390, self.platforms_sprites)
        self.all_sprites.add(self.enemie1)
        self.sprite_enemies.add(self.enemie1)

        self.player = Main_character(0, 390, self.platforms_sprites, self.sprite_items, self.sprite_enemies)
        self.all_sprites.add(self.player)

        self.font = pygame.font.Font('freesansbold.ttf', 12)
       
        self.text_life = f'Life: {str(self.player.live)}'
        self.text = self.font.render(self.text_life, True, 'green')
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (30,30)

        self.text_inventory = f"Apples: {str(len(self.player.inventory))}"
        self.text_inventory_show = self.font.render(self.text_inventory, True, 'green')
        self.text_inventory_rect = self.text_inventory_show.get_rect()
        self.text_inventory_rect.center = (30, 50)


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def new(self):
        self.__init__()
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
        
        self.text_life = f'Life: {str(self.player.live)}'
        self.text = self.font.render(self.text_life, True, 'green')

        self.text_inventory = f"Apples: {str(len(self.player.inventory))}"
        self.text_inventory_show = self.font.render(self.text_inventory, True, 'green')

        if self.player.live <= 0:
            self.game_over_screen()

    def draw(self):
        self.screen.fill((0, 0, 0)) 
        self.screen.blit(self.background_image, (0,0)) 

        self.screen.blit(self.text, self.text_rect)

        self.screen.blit(self.text_inventory_show, self.text_inventory_rect)

        self.all_sprites.draw(self.screen)
        self.sprite_items.draw(self.screen)  
        #self.player.draw_hitbox(self.screen)
        #self.apple1.draw_hitbox(self.screen)
        #self.enemie1.draw_hitbox(self.screen)
        draw_particles(self.screen)
        for platform in self.platforms_sprites:
            self.screen.blit(platform.image, platform.rect.topleft)
            #platform.draw_hitbox(self.screen)
        pygame.display.flip() 
    
    def game_over_screen(self):
        self.screen.fill((0, 0, 0))
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render('Game Over', True, 'red')
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.screen.blit(text, text_rect)
        
        font_small = pygame.font.Font('freesansbold.ttf', 20)
        restart_text = font_small.render('Press R to Restart', True, 'white')
        restart_rect = restart_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
        self.screen.blit(restart_text, restart_rect)

        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:  
                        self.new()
                        waiting = False


if __name__ == '__main__':
    game = Game()
    game.run()