import pygame
def scale_img(image, scale):
    w = image.get_width()
    h = image.get_height()
    new_image = pygame.transform.scale(image, (w*scale, h*scale))
    return new_image