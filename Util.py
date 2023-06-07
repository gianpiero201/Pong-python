import os
import sys

import pygame


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def exibe_mensagem(msg, tamanho, cor):
    fonte = pygame.font.SysFont("comicsansms", tamanho, True, False)
    mensagem = str(msg)
    texto_formatado = fonte.render(mensagem, True, cor)
    return texto_formatado
