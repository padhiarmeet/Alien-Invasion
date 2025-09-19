import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self,ai_game):

        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

<<<<<<< HEAD
        self.image = pygame.image.load('image/jetha.png')
=======
        self.image = pygame.image.load('C:\\Users\\mannm\\OneDrive\\Desktop\\PYTHON\\PYTHON\\Alien Invasion\\image\\ship.png')
>>>>>>> f5a5a8b4c394d39771f640ac082a084aeebe603d
        
        self.image = pygame.transform.scale(self.image, (110,110))
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)#Strting where ship will be placed

        self.moving_right = False
        self.moving_left = False


    def update(self):

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        self.rect.x = self.x #updatethe position of ship


    def blitme(self):
        
        self.screen.blit(self.image, self.rect)


    def _center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

