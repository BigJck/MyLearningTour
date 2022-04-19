import time
from enum import Enum, unique
from math import sqrt
from math import sin
from math import cos
from math import atan
from random import randint

import pygame


class Ball(object):
    def __init__(self, x, y, radius=10, sx=0, sy=3, color=(0, 0, 0)):
        self.x = x
        self.y = y
        self.radius = radius
        self.sx = sx
        self.sy = sy
        self.color = color

    def move_to(self, screen):
        self.x += self.sx
        self.y += self.sy
        if self.x - self.radius < 0 or self.x + self.radius >= screen.get_width():
            self.sx = -self.sx
        if self.y - self.radius < 0 or self.y + self.radius >= screen.get_height():
            self.sy = -self.sy

    def collide(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        juli = sqrt(dx**2 + dy**2)
        if juli <= self.radius + other.radius:
            if self.sx == 0:


            v1 = sqrt(self.sx**2 + self.sy**2)
      #      v2 = sqrt(other.sx**2 + other.sy**2)
            angle1 = atan(self.sy / self.sx)
     #       angle2 = atan(other.sy / other.sx)
            self.sx = v1 * sin(angle1)
            self.sy = v1 * cos(angle1)
  #          other.sx = v2 * sin(angle2)
       #     other.sy = v2 * cos(angle2)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius, 0)


def main():
    balls = []
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Collide Ball')
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                ball = Ball(x, y)
                balls.append(ball)
        screen.fill((255, 255, 255))
        for ball in balls:
            ball.draw(screen)
        pygame.display.flip()
        pygame.time.delay(20)
        for ball in balls:
            ball.move_to(screen)
            for other in balls:
                if ball != other:
                    ball.collide(other)


if __name__ == '__main__':
    main()