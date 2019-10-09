class Settings():
# class to store all settings for game
    def __init__(self):
    # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255,255,136)
        #ship settings
        self.ship_speed_factor = 1.5
        # Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60