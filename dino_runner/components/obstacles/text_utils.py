import pygame.font

from dino_runner.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH

FONT_STYLE = "freesansbold.ttf"
black_color = (0, 0, 0)


def get_score_element(points):
    font = pygame.font.Font(FONT_STYLE, 30)
    text = font.render('Point: {}'.format(points), True, black_color)
    text_rect = text.get_rect()
    text_rect.center = (100, 40)
    return text, text_rect


def get_centered_message(message, width=SCREEN_WIDTH // 2, height=SCREEN_HEIGHT // 2):
    font = pygame.font.Font(FONT_STYLE, 30)
    text = font.render(message, True, black_color)
    text_rect = text.get_rect()
    text_rect.center = (width, height)
    return text, text_rect


def get_number_deaths(deaths, x=800, y=400):
    font = pygame.font.Font(FONT_STYLE, 30)
    text = font.render(deaths, True, black_color)
    text_rect = text.get_rect()
    text_rect.center = (x, y)
    return text, text_rect



