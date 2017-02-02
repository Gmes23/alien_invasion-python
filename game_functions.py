import sys

import pygame

def check_events(ship):
    """Respond to keypresses and mouse evnets."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
                # # # Move the ship to the right.
                # ship.rect.centerx += 1
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship_moving = False
            elif event.key == pygame.K_LEFT:
                ship_moving = False


def update_screen(ai_settings, screen, ship):
    """Update images on the screen and flip to the new screen."""
    # Redraws the screen during each pass through loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # Make the most recently drawn screen visible.
    pygame.display.flip()
