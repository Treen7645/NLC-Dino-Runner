from dino_runner.utils.constants import HEART
from pygame.sprite import Sprite


class Lives(Sprite):
    def __init__(self, pos_x):
        self.image = HEART
        self.pos_x = pos_x
        self.life_rect = self.image.get_rect()
        self.life_rect.x = self.pos_x
        self.life_rect.y = 20

    def draw(self, screen):
        screen.blit(self.image, (self.life_rect.x, self.life_rect.y))