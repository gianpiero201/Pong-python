import pygame

import Util
from Classes.Entity import Entity
from Enumerators.Direction import EDirection


class Raquete(Entity):
    def __init__(
        self,
        player: int,
        pos: tuple[int, int],
        screen: pygame.Surface,
        move_keys: list[int] = [],
        image_flip_horizontal: bool = True,
        rotate_raquete: float = 0,
        direction: EDirection = EDirection.LEFT,
        multiplayer: bool = False
    ):
        Entity.__init__(self)
        self.size = screen.get_size()[0]
        self.images = [pygame.image.load(Util.resource_path("sprits/raquete_2.0.png"))]
        self.images[0] = pygame.transform.scale(
            self.images[0], (self.size / 12, self.size / 12)
        )
        self.images[0] = pygame.transform.rotate(self.images[0], rotate_raquete)
        self.player = player
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.image_flip_horizontal = image_flip_horizontal
        self.mask = pygame.mask.from_surface(self.image)
        self.multiplayer = multiplayer
        self.rect.center = pos
        self.direction = direction
        self.move_keys = move_keys
        self.movement_form = "mouse_pos" if len(self.move_keys) == 0 else "keys"

    def update(self):
        if self.movement_form == "mouse_pos":
            mousepos = pygame.mouse.get_pos()
            mouse_click = pygame.mouse.get_pressed()
            self.rect.centerx = mousepos[0]
            if mouse_click[2] and not self.is_clicked:
                self.is_clicked = True
                self.direction = (
                    EDirection.RIGHT
                    if self.direction == EDirection.LEFT
                    else EDirection.LEFT
                )
            elif not mouse_click[2]:
                self.is_clicked = False
        elif self.movement_form == "keys":
            keys = pygame.key.get_pressed()
            if self.multiplayer:
                if keys[self.move_keys[0]]:
                    self.rect.centery -= 7
                elif keys[self.move_keys[1]]:
                    self.rect.centery += 7
                elif keys[self.move_keys[2]] and not self.is_clicked:
                    self.is_clicked = True
                    if self.direction == EDirection.LEFT:
                        self.direction = EDirection.RIGHT
                    elif self.direction == EDirection.RIGHT:
                        self.direction = EDirection.LEFT
                    elif self.direction == EDirection.UP:
                        self.direction = EDirection.DOWN
                    elif self.direction == EDirection.DOWN:
                        self.direction = EDirection.UP
                elif not keys[self.move_keys[2]]:
                    self.is_clicked = False
            else:
                if keys[self.move_keys[0]]:
                    self.rect.centerx += 7
                elif keys[self.move_keys[1]]:
                    self.rect.centerx -= 7

                elif keys[self.move_keys[2]] and not self.is_clicked:
                    self.is_clicked = True
                    if self.direction == EDirection.LEFT:
                        self.direction = EDirection.RIGHT
                    elif self.direction == EDirection.RIGHT:
                        self.direction = EDirection.LEFT
                    elif self.direction == EDirection.UP:
                        self.direction = EDirection.DOWN
                    elif self.direction == EDirection.DOWN:
                        self.direction = EDirection.UP
                elif not keys[self.move_keys[2]]:
                    self.is_clicked = False

        if self.direction == EDirection.LEFT or (self.direction == EDirection.UP):
            self.image = self.images[0]
        else:
            self.image = pygame.transform.rotate(self.images[0], 60.0)
            self.image = pygame.transform.flip(
                self.images[0],
                self.image_flip_horizontal,
                not self.image_flip_horizontal,
            )
        self.mask = pygame.mask.from_surface(self.image)
