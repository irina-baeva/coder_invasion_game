import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #initialising game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    # Set the background color.
    bg_color = (92, 132, 92)
    #make a ship
    ship = Ship(screen)
    #start the main loop for the game
    while True:
        #watch for keyboard and mouse events
        gf.check_events(ship)
        #update events
        ship.update()
        #Redraw the screen during each pass through the loop.
        gf.update_screen(ai_settings, screen, ship)
run_game()