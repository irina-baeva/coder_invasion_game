class Settings():
# class to store all settings for game
    def __init__(self):
    # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255,255,136)
        #ship settings
        self.ship_speed_factor = 9.5
        self.ship_limit = 3
        # Bullet settings
        self.bullet_speed_factor = 10
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        #alien settings
        self.alien_speed_factor = 5
        self.fleet_drop_speed = 5
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1