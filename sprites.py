import pygame as pg
from random import randint as rand, choice


class Spritesheet:
    def __init__(self, filename: str, sprite_size: tuple = (96, 96)) -> None:
        self.sheet = pg.image.load(filename).convert_alpha()
        self.rect = self.sheet.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height
        self.columns = self.width//sprite_size[0]
        self.rows = self.height//sprite_size[1]
        self.sprite_size = sprite_size

    def get_sprite(self, r: int, c: int, scale: tuple = (1.0, 1.0)) -> pg.Surface:
        w = self.sprite_size[0]
        h = self.sprite_size[1]
        x = c*self.sprite_size[0]
        y = r*self.sprite_size[1]
        surf = pg.Surface((w, h))
        surf.blit(self.sheet, (0, 0), [x, y, w, h])
        surf = pg.transform.scale(surf, (w*scale[0], h*scale[1]))
        return surf

    def get_random_sprite(self, scale: tuple = (1.0, 1.0)) -> pg.Surface:
        x = rand(0, self.columns-1)
        y = rand(0, self.rows - 1)
        return self.get_sprite(
            x*self.sprite_size[0],
            y*self.sprite_size[1],
            self.sprite_size[0],
            self.sprite_size[1],
            scale)


class Pokemon(pg.sprite.Sprite):
    def __init__(self, sprite: pg.Surface, x: int, y: int) -> None:
        super().__init__()
        self.image = sprite
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)


class PokemonGenerator:
    def __init__(self, filepath: str = r"E:\pygame\poke games\Pokefarm\Images\Pokemon\Sprites"):
        self.types = [
            'Bug',
            'Dark',
            'Dragon',
            'Electric',
            'Fairy',
            'Fighting',
            'Fire',
            'Flying',
            'Ghost',
            'Grass',
            'Ground',
            'Ice',
            'Normal',
            'Poison',
            'Psychic',
            'Rock',
            'Steel',
            'Water'
        ]
        self.sheets = {}
        for type in self.types:
            self.sheets[type] = Spritesheet(f'{filepath}/{type}.png')

    def get_pokemon_by_loc_and_type(self, type: str, row: int, col: int, scale: int = 1.0) -> pg.Surface:
        return self.sheets[type].get_sprite(row, col, scale)

    def get_random_pokemon(self) -> pg.Surface:
        typ = choice(self.types)
        return self.sheets[typ].get_random_pokemon()
