import pygame
from pygame.sprite import Sprite

class Bullet(Sprite): #Sprite is used for perform batch updates, collision detection, and drawing operations on all sprites in a group.

    def __init__(self,ai_game):

        super().__init__()
        self.screen = ai_game.screen;
        self.settings = ai_game.settings
        # self.color = self.settings.bullet_color
        self.image = pygame.image.load('C:\\Users\\mannm\\OneDrive\\Desktop\\PYTHON\\PYTHON\\Alien Invasion\\image\\laser_img6.png')
        self.image = pygame.transform.scale(self.image, (6,20))
    
        self.rect = self.image.get_rect()

        # self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)

        self.rect.midtop = ai_game.ship.rect.midtop

        self.y = float(self.rect.y)
    

    def update(self):
        self.y -= self.settings.bullet_speed #Update bulltet speed
        self.rect.y = self.y
    
    
    def draw_bullet(self):
        self.screen.blit(self.image, self.rect)



