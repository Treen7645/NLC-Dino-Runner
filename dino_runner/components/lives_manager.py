
from dino_runner.components.lives import Lives


class LivesManager:
    def __init__(self):
        self.live_list = []

    def fill_lives(self):
        pos_x = 900
        for i in range(0, 3):
            self.live_list.append(Lives(pos_x))
            pos_x += 30

    def draw(self, screen):
        for live in self.live_list:
            live.draw(screen)

    def delete_live(self):
        self.live_list.pop()

    def counter_lives(self):
        return len(self.live_list)