import sys

import pygame

from settings import Settings
from ship import Ship

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

        # Wacth for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Redraws the screen during each pass through loop
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

run_game()
