
from settings import *
from sprites import *


class Game:
    def __init__(self):
        self.window = pg.display.set_mode((WIDTH, HEIGHT))
        self.end_game = False

        self.all_sprites = pg.sprite.Group()

    def draw(self):
        self.window.fill(-1)

        self.all_sprites.draw(self.window)
        self.all_sprites.update()

        pg.display.flip()

    def game_loop(self):
        while not self.end_game:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.end_game = True
                    pg.quit()

            self.draw()


game = Game()
game.game_loop()
