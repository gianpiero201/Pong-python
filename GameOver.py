import math
import sys

import pygame
from pygame.locals import QUIT

import Game
import GameTwoPlayer
import Start
import Util


def game_over_one(tela: pygame.Surface, mostrar_pontuacao: bool, pontuacao: int):
    largura = tela.get_size()[0]
    altura = tela.get_size()[1]

    while mostrar_pontuacao:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    Game.Game(tela).startGame()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    Start.tela_start()

        game_over = Util.exibe_mensagem(
            "GAME OVER: " + str(pontuacao), math.ceil(largura / 35), (0, 0, 0)
        )
        tela.blit(
            game_over,
            (
                (largura / 2) - game_over.get_size()[0] / 2,
                (altura / 2) - game_over.get_size()[1] / 2,
            ),
        )
        restart = Util.exibe_mensagem(
            "PRESSIONE (R) PARA REINICIAR O JOGO OU (E) PARA SAIR",
            math.ceil(largura / 35),
            (0, 0, 0),
        )
        tela.blit(
            restart,
            (
                (largura / 2) - restart.get_size()[0] / 2,
                (altura / 2) + 60 - restart.get_size()[1] / 2,
            ),
        )
        pygame.display.update()


def game_over_two(tela: pygame.Surface, mostrar_pontuacao: bool, player: int):
    largura = tela.get_size()[0]
    altura = tela.get_size()[1]

    while mostrar_pontuacao:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    GameTwoPlayer.GameTwoPlayer(tela).startGame()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    Start.tela_start()

        game_over = Util.exibe_mensagem("Vencedor:", math.ceil(largura / 35), (0, 0, 0))
        tela.blit(
            game_over,
            (
                (largura / 2) - game_over.get_size()[0] / 2,
                (altura / 2 - 60) - game_over.get_size()[1] / 2,
            ),
        )
        player_winner = Util.exibe_mensagem(
            "Player " + str(player), math.ceil(largura / 35), (0, 0, 0)
        )
        tela.blit(
            player_winner,
            (
                (largura / 2) - player_winner.get_size()[0] / 2,
                (altura / 2) - player_winner.get_size()[1] / 2,
            ),
        )
        restart = Util.exibe_mensagem(
            "PRESSIONE (R) PARA REINICIAR O JOGO OU (E) PARA SAIR",
            math.ceil(largura / 35),
            (0, 0, 0),
        )
        tela.blit(
            restart,
            (
                (largura / 2) - restart.get_size()[0] / 2,
                (altura / 2) + 60 - restart.get_size()[1] / 2,
            ),
        )
        pygame.display.update()
