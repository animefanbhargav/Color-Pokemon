
from settings import *
from sprites import *


class Game:
    def __init__(self):
        self.window = pg.display.set_mode((WIDTH, HEIGHT))
        self.end_game = False
        self.clock = pg.time.Clock()

        self.all_sprites = pg.sprite.Group()

        self.poke_generator = PokemonGenerator()

        # Add a random pokemon sprite
        pokemon_pos = (WIDTH//2, HEIGHT//2)  # Center the pokemon
        pokemon_image = self.poke_generator.get_random_pokemon()
        pokemon_sprite = Pokemon(pokemon_image, pokemon_pos)

        self.all_sprites.add(pokemon_sprite)

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


pg.init()
game = Game()
game.game_loop()
