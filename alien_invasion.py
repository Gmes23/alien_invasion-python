import sys

import pygame
from pygame.sprite import Group

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
    ship = Ship(ai_settings, screen)

    # Make a group to store bullets in.
    bullets = Group()

    # Set Main Background Color.
    bg_color = (230, 230, 230)

    # Start the main loop for the game.
    while True:

        # game functions imported from game_functions.py.
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        # bullets.update()
        gf.update_bullets(bullets)

        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()
