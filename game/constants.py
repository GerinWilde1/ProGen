import os
import sys
import arcade
import random

# SCREEN_WIDTH = 1000
# SCREEN_HEIGHT = 650

# PLAYER_SIZE = .5

# CHARACTER_SCALING = .4
# TILE_SCALING= 0.2

# MOVEMENT_SPEED = 5

# more of the map.
WALL_SPRITE_SCALING = 0.5
PLAYER_SPRITE_SCALING = 0.25

WALL_SPRITE_SIZE = int(128 * WALL_SPRITE_SCALING)

# How big the grid is
GRID_WIDTH = 100
GRID_HEIGHT = 100

AREA_WIDTH = GRID_WIDTH * WALL_SPRITE_SIZE
AREA_HEIGHT = GRID_HEIGHT * WALL_SPRITE_SIZE

# How fast the player moves
MOVEMENT_SPEED = 5

# How close the player can get to the edge before we scroll.
VIEWPORT_MARGIN = 300

# How big the window is
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_TITLE = "Caves"

MERGE_SPRITES = False