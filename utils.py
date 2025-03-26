import pygame
from settings import MAIN_CHARACTER_SCALE

def scale_img(image, scale):
    w = image.get_width()
    h = image.get_height()
    new_image = pygame.transform.scale(image, (w*scale, h*scale))
    return new_image

def load_frames(sheet, frame_width, frame_height, num_frames):
        frames = []
        for i in range(num_frames):
            rect = pygame.Rect(i * frame_width, 0, frame_width, frame_height)
            frame = sheet.subsurface(rect)
            frame = scale_img(frame, MAIN_CHARACTER_SCALE)
            frames.append(frame)
        return frames