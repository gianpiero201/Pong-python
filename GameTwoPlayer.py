import math
import sys

import pygame
from pygame.locals import QUIT

import GameOver
import Sound_Effects
import Util
from Classes.Bola import Bola
from Classes.Parede import Parede
from Classes.Raquete import Raquete
from Enumerators.Direction import EDirection


class GameTwoPlayer:
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
        self.fundo = pygame.image.load(Util.resource_path("sprits/fundo_multiplayer.PNG"))
        self.fundo = pygame.transform.scale(self.fundo, (self.largura, self.altura))
        self.__init_entities()
        self.runninggame = False
        self.pontuacao_player1 = 0
        self.pontuacao_player2 = 0
        self.pontuacao_max = 3
        self.texto_pause = self.fonte.render("| |", True, self.cor_texto)
        self.texto_pause_posicao = self.texto_pause.get_rect(
            center=self.botao_posicao.center
        )
        self.texto_pontuacao = pygame.font.Font(None, 26).render(
            str(self.pontuacao_player1) + " X " + str(self.pontuacao_player2),
            True,
            (0, 0, 0),
        )
        self.texto_pontuacao_posicao = self.texto_pontuacao.get_rect(
            center=self.botao_posicao.center,
            top=self.botao_posicao.top + self.botao_posicao.size[1] + 10,
        )
        self.endgame = False

    def __init_entities(self):
        self.entities_raquetes = pygame.sprite.Group()
        self.entities_ball = pygame.sprite.Group()
        self.entities_wall = pygame.sprite.Group()

        self.parede_left = Parede(EDirection.LEFT, (-16, 0), 16, self.altura)
        self.parede_top = Parede(EDirection.UP, (0, -16), self.largura, 16)
        self.parede_right = Parede(EDirection.RIGHT, (self.largura, 0), 16, self.altura)
        self.parede_bottom = Parede(EDirection.DOWN, (0, self.altura), self.largura, 16)

        self.bola_array = [Bola(self.tela, (self.largura / 2, self.altura / 2))]
        self.raquete1 = Raquete(
            2,
            (self.largura - (self.largura / 14), self.altura / 2),
            self.tela,
            [pygame.K_UP, pygame.K_DOWN, pygame.K_RCTRL],
            False,
            -180,
            EDirection.UP,
            multiplayer=True
        )
        self.raquete = Raquete(
            1,
            (self.largura / 14, self.altura / 2),
            self.tela,
            [pygame.K_w, pygame.K_s, pygame.K_LCTRL],
            False,
            -90.0,
            EDirection.UP,
            multiplayer=True
        )

        self.entities_wall.add(self.parede_left)
        self.entities_wall.add(self.parede_top)
        self.entities_wall.add(self.parede_right)
        self.entities_wall.add(self.parede_bottom)
        self.entities_ball.add(self.bola_array)
        self.entities_raquetes.add(self.raquete)
        self.entities_raquetes.add(self.raquete1)

    def restart(self, ball_direction: int = None):
        self.entities_ball.empty()
        self.speed = 3
        self.started = False
        self.runninggame = False
        self.bola_array = [
            Bola(self.tela, (self.largura / 2, self.altura / 2), ball_direction)
        ]
        self.entities_ball.add(self.bola_array)
        self.start_message = Util.exibe_mensagem(
            'Aperte "espaço" para iniciar o jogo.',
            math.ceil(self.largura / 35),
            (0, 0, 0),
        )

        self.update_game()
        self.tela.blit(
            self.start_message,
            (
                (self.largura / 2) - self.start_message.get_size()[0] / 2,
                (self.altura / 2) + 60 - self.start_message.get_size()[1] / 2,
            ),
        )

    def startGame(self):
        self.tela.blit(self.raquete.image, self.raquete.rect)

        self.pontuacao_player1 = 0
        self.pontuacao_player2 = 0
        self.endgame = False
        self.speed = 3
        self.started = False
        self.start_message = Util.exibe_mensagem(
            'Aperte "espaço" para iniciar o jogo.',
            math.ceil(self.largura / 35),
            (0, 0, 0),
        )
        Sound_Effects.game_easy_mode()
        self.update_game()
        self.tela.blit(
            self.start_message,
            (
                (self.largura / 2) - self.start_message.get_size()[0] / 2,
                (self.altura / 2) + 60 - self.start_message.get_size()[1] / 2,
            ),
        )

        self.relogio.tick(60)
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
            str(self.pontuacao_player1) + " X " + str(self.pontuacao_player2),
            True,
            (0, 0, 0),
        )
        self.update_game()

    def update_game(self):
        self.tela.blit(self.fundo, (0, 0))
        pygame.draw.rect(self.tela, self.cor_botao, self.botao_posicao)
        self.tela.blit(self.texto_pause, self.texto_pause_posicao)
        self.tela.blit(self.raquete.image, self.raquete.rect)
        self.tela.blit(self.texto_pontuacao, self.texto_pontuacao_posicao)
        self.entities_raquetes.update()
        self.entities_wall.update()
        self.entities_ball.update()
        self.entities_raquetes.draw(self.tela)
        self.entities_wall.draw(self.tela)
        self.entities_ball.draw(self.tela)

    def collide_objects(self):
        # collision ball and wall collision
        for bola in self.bola_array:
            collide_wall: list[Parede] = pygame.sprite.spritecollide(
                bola, self.entities_wall, False, pygame.sprite.collide_mask
            )
            collide_raquete: list[Raquete] = pygame.sprite.spritecollide(
                bola, self.entities_raquetes, False, pygame.sprite.collide_mask
            )
            if collide_wall:
                bola.change_direction(collide_wall[0].pos_direction)
            if pygame.sprite.collide_mask(bola, self.parede_left):
                self.pontuacao_player2 += 1
                self.update_pontuacao()
                Sound_Effects.item_score_multiplayer()
                if self.pontuacao_player2 < self.pontuacao_max:
                    self.restart(1)
            if pygame.sprite.collide_mask(bola, self.parede_right):
                self.pontuacao_player1 += 1
                self.update_pontuacao()
                Sound_Effects.item_score_multiplayer()
                if self.pontuacao_player1 < self.pontuacao_max:
                    self.restart(-1)

            if (
                self.pontuacao_player1 == self.pontuacao_max
                or self.pontuacao_player2 == self.pontuacao_max
            ):
                self.endgame = True
                player_winner = (
                    1 if self.pontuacao_player1 > self.pontuacao_player2 else 2
                )
                player_winner = (
                    1 if self.pontuacao_player1 > self.pontuacao_player2 else 2
                )
                GameOver.game_over_two(self.tela, True, player_winner)

            if collide_raquete:
                if collide_raquete[0].player == 1 and bola.direction_move_x < 0:
                    bola.change_direction(EDirection.LEFT)
                    bola.change_direction(collide_raquete[0].direction)
                    self.speed += 1
                    Sound_Effects.item_ball()
                elif collide_raquete[0].player == 2 and bola.direction_move_x > 0:
                    bola.change_direction(EDirection.RIGHT)
                    bola.change_direction(collide_raquete[0].direction)
                    self.speed += 1
                    Sound_Effects.item_ball()
                bola.change_speed(self.speed)
