class Settings:

    def __init__(self):
        #Screen settings are here.....
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (31,36,33)
        #(61,64,91)
        self.ship_speed = 2.4

        self.bullet_speed = 2.2
        self.bullet_width = self.screen_width
        self.bullet_height = 15
        self.bullet_color = (239,35,60)
        self.bullet_allowed = 5

        self.alien_speed = 1.0
        self.drop_speed = 9
        self.fleet_direction = 1 # 1 = right and -1 = left