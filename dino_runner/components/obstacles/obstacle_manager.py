import pygame
import random
from dino_runner.components.obstacles.cactus import Cactus, LargeCactus, Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS,BIRD
from dino_runner.components.lives import Lives


class ObstacleManager:

    def __init__(self):
        self.obstacles = []


    def update(self, game):
        if len(self.obstacles) == 0:
            if random.randint(0, 2) == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS))
            elif random.randint(0, 2) == 1:
                self.obstacles.append(LargeCactus(LARGE_CACTUS))
            elif random.randint(0, 2) == 2:
                self.obstacles.append(Bird(BIRD))



        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)

            if game.player.dino_rect.colliderect(obstacle.rect):
                if game.player.shield:
                    self.obstacles.remove(obstacle)
                elif game.lives_manager.counter_lives() == 1:
                    game.lives_manager.delete_live()
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count += 1
                    break
                else:
                    game.lives_manager.delete_live()
                    if obstacle in self.obstacles:
                        self.obstacles.remove(obstacle)


    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []


