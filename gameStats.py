class GameStats:

    def __init__(self,ai_game):
        
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False
        self.high_score = 0

    
    def reset_stats(self): # we will initialize most of statistic here instand of __init()__ because we have to call method many time in one game which is not posiible in init..

        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.game_active = True 
        self.level = 1