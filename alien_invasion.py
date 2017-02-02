import sys

import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # Initialize game and creates a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Space Invaders")

    # Make a ship
    ship = Ship(screen)

    # Set Main Background Color.
    bg_color = (230, 230, 230)

    # Start the main loop for the game.
    while True:

        # game functions imported from game_functions.py.
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)

run_game()
