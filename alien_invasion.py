import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group

def run_game():
    #initialising game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    # Set the background color.
    bg_color = (92, 132, 92)
    #make a ship
    ship = Ship(ai_settings, screen)
    # Make a group to store bullets in.
    bullets = Group()
    aliens = Group()
    # Make an alien.
    alien = Alien(ai_settings, screen)
    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)
    #start the main loop for the game
    while True:
        #watch for keyboard and mouse events
        gf.check_events(ai_settings, screen, ship, bullets)
        #update events
        ship.update()
        gf.update_bullets(bullets)
        # print(len(bullets))
        #Redraw the screen during each pass through the loop.
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
run_game()