import arcade
import os
import sys
import random
import game.constants as c


class Character:

    def __init__(self):

        super().__init__()

        pass

    # def setup(self):
    #     self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/"
    #                                        "femalePerson_idle.png",
    #                                        c.PLAYER_SPRITE_SCALING)
    #     self.player_list.append(self.player_sprite)
    #     placed = False
    #     while not placed:

    #         self.player_sprite.center_x = random.randrange(c.AREA_WIDTH)
    #         self.player_sprite.center_y = random.randrange(c.AREA_HEIGHT)

    #         walls_hit = arcade.check_for_collision_with_list(self.player_sprite, self.wall_list)
    #         if len(walls_hit) == 0:
    #             placed = True

    #     self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
    #                                                      self.wall_list
    def draw(self):

        pass