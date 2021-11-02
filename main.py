import pygame
from settings import *

# create color constants
WHITE = (255, 255, 255)
RED = (87, 9, 9)
GREEN = (12, 148, 37)
BLUE = (2, 0, 94)
BLACK = (0, 0, 0)

# width by height
FPS = 60
DISPLAY_WIDTH = 1000
DISPLAY_HEIGHT = 800

# Player
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50

# Game Layout
LAYOUT = ['11111111111111111111',
          '10000000000000000001',
          '10000000000000000001',
          '10000000000000000001',
          '10000000000000000001',
          '10000000000000000001',
          '10000000000000000001',
          '10000000000000000001',
          '10000000000000000001',
          '11111111111111111111', ]

WALL_BRICK_WIDTH = DISPLAY_WIDTH // len(LAYOUT[0])
WALL_BRICK_HEIGHT = DISPLAY_HEIGHT // len(LAYOUT)


class Player:
    def __init__(self, display, color, x, y, width, height):
        self.display = display
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velo = 5
        self.x_velo = 0
        self.y_velo = 3

    def draw_player(self):
        pygame.draw.rect(self.display, self.color,
                         (self.x, self.y, self.width, self.height))

    def player_keys(self):
        pass

    def move_player(self):
        pass

        # player movement is jumping, going up

        # player movement is falling, going down

    def control_player(self):
        # call all player movement functions
        pass


class Ball:
    def __init__(self, display, color, x, y, width, height):
        self.display = display
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height


class Walls():
    def __init__(self, display, color, x, y, width, height):
        self.display = display
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def make_walls(self):
        pygame.draw.rect(self.display, self.color,
                         (self.x, self.y, self.width, self.height))


pygame.init()

screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Game Title")

clock = pygame.time.Clock()
player = Player(screen, BLUE,
                WALL_BRICK_WIDTH * 2,
                DISPLAY_HEIGHT - WALL_BRICK_HEIGHT - PLAYER_HEIGHT,
                PLAYER_WIDTH, PLAYER_HEIGHT)

wall_blocks = []
for row in range(len(LAYOUT)):
    y_loc = row * WALL_BRICK_HEIGHT

    for col in range(len(LAYOUT[0])):
        x_loc = col * WALL_BRICK_WIDTH

        if LAYOUT[row][col] == '1':
            brick = Walls(screen, RED, x_loc, y_loc, WALL_BRICK_WIDTH, WALL_BRICK_HEIGHT)
            wall_blocks.append(brick)

running = True

while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    make_walls()
    player.control_player()

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()

