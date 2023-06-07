import os
import sys

import pygame

import Util


def start_sound():
    pygame.mixer.music.load(Util.resource_path('Sounds/fundo_start.mp3'))
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)


def item_menu():
    menu_sound = pygame.mixer.Sound(Util.resource_path('Sounds/item_menu.mp3'))
    menu_sound.set_volume(0.1)
    menu_sound.play()

def game_easy_mode():
    pygame.mixer.music.load(Util.resource_path('Sounds/game_easy_mode.mp3'))
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)

def game_hard_mode():
    pygame.mixer.music.load(Util.resource_path('Sounds/game_hard_mode.mp3'))
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)

def item_ball():
    menu_sound = pygame.mixer.Sound(Util.resource_path('Sounds/item_ball.mp3'))
    menu_sound.set_volume(0.1)
    menu_sound.play()

def item_score_multiplayer():
    menu_sound = pygame.mixer.Sound(Util.resource_path('Sounds/multiplayer_score.mp3'))
    menu_sound.set_volume(0.1)
    menu_sound.play()