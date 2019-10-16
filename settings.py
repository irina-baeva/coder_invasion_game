class Settings():
# class to store all settings for game
    def __init__(self):
    # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255,255,136)
        #ship settings
        self.ship_limit = 3
        # Bullet settings
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = 255, 0, 0
        self.bullets_allowed = 3
        #alien settings
        self.alien_speed_factor = 3
        self.fleet_drop_speed = 10
        
        # How quickly the game speeds up
        self.speedup_scale = 1.5
        # How quickly the alien point values increase
        self.score_scale = 1.5
        self.initialize_dynamic_settings()
      
    def initialize_dynamic_settings(self):
        # initialize settings that change throughout the game.
        self.ship_speed_factor = 9.5
        self.bullet_speed_factor = 8
        self.alien_speed_factor = 3
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
       # Scoring
        self.alien_points = 50
    def increase_speed(self):
    # increase speed settings
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)