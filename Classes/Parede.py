import string
import pygame

from Classes.Entity import Entity
from Enumerators.Direction import EDirection


class Parede(Entity):
    def __init__(
        self,
        pos_direction: EDirection,
        pos: tuple[int, int],
        width: int,
        height: int,
    ):
        Entity.__init__(self)
        self.pos_direction = pos_direction
        self.image = pygame.Surface((width, height))
        self.image.fill((255, 155, 77))
        self.rect = pygame.Rect(pos[0], pos[1], width, height)
