import pygame
import random

BLACK = (0, 0, 0)


class Ball(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        self.velocity = [5, -5]
        self.rect = self.image.get_rect()

        # Draw the ball
        pygame.draw.ellipse(self.image, color, [0, 0, width, height])

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        rand_num = random.random()
        if rand_num < 0.5:
            self.velocity[1] *= -1
        else:
            self.velocity[0] *= -1
            self.velocity[1] *= -1