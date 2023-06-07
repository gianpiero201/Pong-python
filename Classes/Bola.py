import math
import random
import string
import pygame
from Classes.Entity import Entity
from Enumerators.Direction import EDirection
import Util


class Bola(Entity):
    def __init__(
        self,
        screen: pygame.Surface,
        start_pos: tuple[int, int] = None,
        start_direction_hor: int = None,
    ):
        Entity.__init__(self)
        self.__speed = 3
        self.width = screen.get_size()[0]
        self.height = screen.get_size()[1]
        if not start_pos:
            self.x = random.randrange(
                math.ceil(self.width / 20), math.ceil(self.width / 1.1)
            )
            self.y = random.randrange(
                math.ceil(self.height / 20), math.ceil(self.height / 2)
            )
        else:
            self.x = start_pos[0]
            self.y = start_pos[1]

        self.image = pygame.image.load(Util.resource_path("sprits/bola_2.0.png"))
        self.image = pygame.transform.scale(
            self.image, (self.width / 25, self.width / 25)
        )
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = pygame.draw.rect(
            screen,
            (0, 0, 0),
            pygame.Rect((self.x, self.y), (self.width / 25, self.width / 25)),
        )
        self.direction_move_x = start_direction_hor or (
            -1 if random.random() < 0.5 else 1
        )
        self.direction_move_y = -1 if random.random() < 0.5 else 1

    def update(self):
        self.x += self.direction_move_x * self.__speed
        self.y += self.direction_move_y * self.__speed
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = (self.x, self.y)

    def change_speed(self, speed: float):
        self.__speed = speed

    def change_direction(self, direction: EDirection):
        name = "_direction_" + direction.name
        method = getattr(self, name)
        method()

    def _direction_UP(self):
        self.direction_move_y = random.randrange(5, 10) / 10

    def _direction_DOWN(self):
        self.direction_move_y = (random.randrange(5, 10) / 10) * -1

    def _direction_LEFT(self):
        self.direction_move_x = random.randrange(5, 10) / 10

    def _direction_RIGHT(self):
        self.direction_move_x = (random.randrange(5, 10) / 10) * -1
