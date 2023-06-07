import math
import sys
from ast import List

import pygame
from pygame.locals import QUIT

import GameOver
import Sound_Effects
import Util
from Classes.Bola import Bola
from Classes.Parede import Parede
from Classes.Raquete import Raquete
from Enumerators.Direction import EDirection


class Game:
    def __init__(self, screen: pygame.Surface):
        pygame.display.set_caption("Pong")
        self.tela = screen
        self.largura = self.tela.get_size()[0]
        self.altura = self.tela.get_size()[1]
        self.fonte = pygame.font.Font(None, 36)
        self.botao_posicao = pygame.Rect(self.largura // 2 - 50, 25, 50, 50)
        self.cor_texto = (255, 255, 255)
        self.cor_botao = (46, 139, 8)
        self.relogio = pygame.time.Clock()
        self.fundo = pygame.image.load(Util.resource_path("sprits/fundo_sigleplayer.png"))
        self.fundo = pygame.transform.scale(self.fundo, (self.largura, self.altura))
        self.__init_entities()
        self.runninggame = False
        self.pontuacao = 0
        self.texto_pause = self.fonte.render("| |", True, self.cor_texto)
        self.texto_pause_posicao = self.texto_pause.get_rect(
            center=self.botao_posicao.center
        )
        self.texto_pontuacao = pygame.font.Font(None, 26).render(
            "Pontuação: " + str(self.pontuacao), True, (0, 0, 0)
        )
        self.texto_pontuacao_posicao = self.texto_pontuacao.get_rect(left=16, top=16)
        self.endgame = False

    def __init_entities(self):
        self.entities = pygame.sprite.Group()
        self.entities_ball = pygame.sprite.Group()
        self.entities_wall = pygame.sprite.Group()

        self.parede_left = Parede(EDirection.LEFT, (-16, 0), 16, self.altura)
        self.parede_top = Parede(EDirection.UP, (0, -16), self.largura, 16)
        self.parede_right = Parede(EDirection.RIGHT, (self.largura, 0), 16, self.altura)
        self.parede_bottom = Parede(EDirection.DOWN, (0, self.altura), self.largura, 16)

        self.bola_array = [Bola(self.tela)]
        self.raquete = Raquete(1, (self.largura / 2, self.altura - 50), self.tela, [pygame.K_RIGHT, pygame.K_LEFT, pygame.K_LCTRL])

        self.entities_wall.add(self.parede_left)
        self.entities_wall.add(self.parede_top)
        self.entities_wall.add(self.parede_right)
        self.entities_wall.add(self.parede_bottom)
        self.entities_ball.add(self.bola_array)
        self.entities.add(self.raquete)

    def startGame(self):
        self.tela.blit(self.raquete.image, self.raquete.rect)

        self.runninggame = True
        self.pontuacao = 0
        self.endgame = False
        self.speed = 3
        self.started = False

        self.relogio.tick(60)

        Sound_Effects.game_easy_mode()

        while not self.endgame:
            self.largura = self.tela.get_size()[0]
            self.altura = self.tela.get_size()[1]
            mousepos = pygame.mouse.get_pos()

            if self.runninggame:
                self.collide_objects()
                self.update_game()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.botao_posicao.collidepoint(mousepos) or (
                            not self.runninggame
                        ):
                            self.runninggame = not self.runninggame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.runninggame = not self.runninggame
            pygame.display.update()

    def update_pontuacao(self):
        self.texto_pontuacao = pygame.font.Font(None, 26).render(
            "Pontuação: " + str(self.pontuacao), True, (0, 0, 0)
        )

    def update_game(self):
        self.tela.blit(self.fundo, (0, 0))
        pygame.draw.rect(self.tela, self.cor_botao, self.botao_posicao)
        self.tela.blit(self.texto_pause, self.texto_pause_posicao)
        self.tela.blit(self.texto_pontuacao, self.texto_pontuacao_posicao)
        self.tela.blit(self.raquete.image, self.raquete.rect)
        self.entities.update()
        self.entities_wall.update()
        self.entities_ball.update()
        self.entities.draw(self.tela)
        self.entities_wall.draw(self.tela)
        self.entities_ball.draw(self.tela)

    def collide_objects(self):
        for bola in self.bola_array:
            collide_wall: list[Parede] = pygame.sprite.spritecollide(
                bola, self.entities_wall, False, pygame.sprite.collide_mask
            )
            if collide_wall:
                bola.change_direction(
                    collide_wall[0].pos_direction,
                )
            if pygame.sprite.collide_mask(bola, self.parede_bottom):
                self.endgame = True
                GameOver.game_over_one(self.tela, True, self.pontuacao)

            if (
                pygame.sprite.collide_mask(bola, self.raquete)
                and bola.direction_move_y > 0
            ):
                bola.change_direction(self.raquete.direction)
                bola.change_direction(EDirection.DOWN)
                self.pontuacao += 1
                self.update_pontuacao()
                self.speed += 1
                bola.change_speed(self.speed)
                Sound_Effects.item_ball()
                if self.pontuacao == 5:
                    Sound_Effects.game_hard_mode()
                    self.fundo = pygame.image.load(Util.resource_path("sprits/fundo_sigleplayer_hard.png"))
                    self.fundo = pygame.transform.scale(self.fundo, (self.largura, self.altura))
