import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats

def run_game():
    #initialising game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    # Set the background color.
    bg_color = (92, 132, 92)
    # keep statistic of the game
    stats = GameStats(ai_settings)
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
        #we check what parts of game executes when game_active true
        if stats.game_active:
            #update events
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            # print(len(bullets))
            gf.update_aliens(ai_settings, aliens, ship, stats, screen, bullets)
        #Redraw the screen during each pass through the loop.
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
run_game()