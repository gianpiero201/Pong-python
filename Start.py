import sys

import pygame

import Sound_Effects
import Util
from Game import Game
from GameTwoPlayer import GameTwoPlayer


def tela_start():
    pygame.init()

    BLACK = (0, 0, 0)
    GRAY = (50, 50, 50)
    WHITE = (255, 255, 255)

    WINDOW_WIDTH = 1280
    WINDOW_HEIGHT = 720

    FONT_SIZE = 48

    menu_options = ['Singleplayer', 'Multiplayer', 'Exit']
    selected_option = 0

    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Menu")

    font = pygame.font.Font('Fonts/ARCADECLASSIC.TTF', FONT_SIZE)
    font_title = pygame.font.Font('Fonts/ARCADECLASSIC.TTF', 2 * FONT_SIZE)
    font_arrow = pygame.font.Font('Fonts/Giant Gnome Regular Ltd.ttf', FONT_SIZE)

    desktop_size = pygame.display.get_desktop_sizes()[0]
    WINDOW_WIDTH = desktop_size[0] - 100
    WINDOW_HEIGHT = desktop_size[1] - 100
    tela = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    def draw_menu():
        window.fill(BLACK)
        
        title_text = font_title.render("Pong!", True, WHITE)
        title_rect = title_text.get_rect(center=(WINDOW_WIDTH / 1.97, WINDOW_HEIGHT / 5))
        tela.blit(title_text, title_rect)
        
        menu_height = len(menu_options) * FONT_SIZE
        
        menu_start_y = (WINDOW_HEIGHT - menu_height) / 1.5
        
        for i, option in enumerate(menu_options):
            text = font.render(option, True, WHITE if i == selected_option else GRAY)
            text_rect = text.get_rect(center=(WINDOW_WIDTH / 2, menu_start_y + i * FONT_SIZE))
            tela.blit(text, text_rect)

            if i == selected_option:
                arrow_text = font_arrow.render("▶", True, WHITE)
                arrow_rect = arrow_text.get_rect(right=text_rect.left - 20, centery=text_rect.centery)
                tela.blit(arrow_text, arrow_rect)

    game = Game(tela)
    game_two_players = GameTwoPlayer(tela)
    Sound_Effects.start_sound()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(menu_options)
                    Sound_Effects.item_menu()
                elif event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(menu_options)
                    Sound_Effects.item_menu()
                elif event.key == pygame.K_RETURN:
                    if selected_option == 0:
                        game.startGame()
                    elif selected_option == 1:
                        game_two_players.startGame()
                    elif selected_option == 2:
                        print("Opção Opções selecionada")
                    elif selected_option == 3:
                        print("Opção Sobre selecionada")
                    elif selected_option == 4:
                        print("Opção Sair selecionada")
                        pygame.quit()
                        sys.exit()

        draw_menu()
        pygame.display.update()
