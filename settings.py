class Settings:

    def __init__(self):
        #Screen settings are here.....
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (31,36,33)
        #(61,64,91)
        self.ship_speed = 2.4
        self.ship_limit = 3

        self.bullet_speed = 2.2
        self.bullet_width = 6
        self.bullet_height = 15
        self.bullet_color = (239,35,60)
        self.bullet_allowed = 5

        self.alien_speed = 1
        self.drop_speed = 9
        self.fleet_direction = 1 # 1 = right and -1 = left

        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()
        

    def initialize_dynamic_settings(self):

        self.ship_speed = 3
        self.bullet_speed = 6.0
        self.alien_speed = 2.5

        self.fleet_direction = 1
        self.alien_point = 50


    def increse_speed(self):
        
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_point = int(self.alien_point * self.speedup_scale)
