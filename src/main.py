#! /usr/bin/env python3 

# Import statements
import pygame

# Local imports
import constants
from snake_game import Game

# Initialize pygame
pygame.init()

# Constants
BACKGROUND_COLOR = (0, 0, 0)
SNAKE_COLOR = (0, 255, 0)
FOOD_COLOR = (255, 0, 0)
SCORE_COLOR = (255, 255, 255)
FONT_SIZE = 40
CLOCK_SPEED = 15

# Dynamically create pygame screen
MONITOR_H = pygame.display.Info().current_h
WINDOW_SIZE = int(MONITOR_H * 0.9)
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))

NUM_GRIDS = 20  # 20x20 board
GRID_SIZE = int(WINDOW_SIZE / NUM_GRIDS)

clock = pygame.time.Clock()
running = True


def render_game(screen, game):
    # Draw snake
    for seg in game.snake.body:
        seg_x = seg[1] * GRID_SIZE
        seg_y = seg[0] * GRID_SIZE
        seg_rect = pygame.Rect(seg_x, seg_y, GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(screen, SNAKE_COLOR, seg_rect)

    # Draw food
    food_radius = GRID_SIZE/2
    food_x = game.food.position[1] * GRID_SIZE + food_radius
    food_y = game.food.position[0] * GRID_SIZE + food_radius
    pygame.draw.circle(screen, FOOD_COLOR, (food_x, food_y), food_radius)

    # Display score 
    score_font = pygame.font.Font(size=FONT_SIZE)
    score_text = score_font.render(f"Score: {game.score}", True, SCORE_COLOR)
    screen.blit(score_text, (int(WINDOW_SIZE/2) - int(score_text.get_size()[0]/2), 10))

# Initialize game 
game = Game(GRID_SIZE, (WINDOW_SIZE, WINDOW_SIZE))

while running:
    # Poll for inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False 
            elif event.key == pygame.K_UP:
                game.snake.change_direction(constants.UP)
            elif event.key == pygame.K_DOWN:
                game.snake.change_direction(constants.DOWN)
            elif event.key == pygame.K_LEFT:
                game.snake.change_direction(constants.LEFT)
            elif event.key == pygame.K_RIGHT:
                game.snake.change_direction(constants.RIGHT)

    # Update game 
    game.update()
    if game.game_over: game.reset()

    # Wipe away last frame with background color
    screen.fill(BACKGROUND_COLOR)

    # RENDER GAME HERE
    render_game(screen, game)

    # flip() rendered display onto screen
    pygame.display.flip()

    # Limit game fps
    clock.tick(CLOCK_SPEED) 

# Close out the game
pygame.quit()