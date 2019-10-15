import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        #  starting position of allien
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/alien2.bmp')
        self.rect = self.image.get_rect()
        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # Store the alien's exact position.
        self.x = float(self.rect.x)
        self.alien_speed_factor = 1

    def blitme(self):
    #    draw the alien at its current location.
        self.screen.blit(self.image, self.rect)
        # Alien settings
    def check_edges(self):
    #return true if alien is at edge of screen.
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
    def update(self):
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x