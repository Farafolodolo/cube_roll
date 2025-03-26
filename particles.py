import pygame
import random
from settings import WIDTH, HEIGHT, MAIN_PARTICLES_COLOR

class Particle:
    def __init__(self):
        self.x = random.randint(0, WIDTH)  # Random horizontal position
        self.y = random.randint(-20, 0)  # They start from the top
        self.speed = random.uniform(1, 3)  # Random drop speed

    def update(self):
        self.y += self.speed  # Move down
        if self.y > HEIGHT:  # If it reaches the bottom, it reappears at the top
            self.y = random.randint(-20, 0)
            self.x = random.randint(0, WIDTH)

    def draw(self, screen):
        pygame.draw.circle(screen, MAIN_PARTICLES_COLOR, (int(self.x), int(self.y)), 2)

# Create a list of particles
particles = [Particle() for _ in range(60)]

def update_particles():
    """Upgrades all particles"""
    for particle in particles:
        particle.update()

def draw_particles(screen):
    """Draw all particles on the screen"""
    for particle in particles:
        particle.draw(screen)
