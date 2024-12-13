import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group() # initializing bullets list
        self.aliens = pygame.sprite.Group() # initializing aliens list

        self._create_fleet()
    
    def run_game(self):
        while True:
            self._check_event()
            self.ship.update()
            self._update_bullet()
            self._check_update()

    

    def _check_event(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = True
                    if event.key == pygame.K_LEFT:
                        self.ship.moving_left = True
                    
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = False  
                    if event.key == pygame.K_LEFT:
                        self.ship.moving_left = False  
                    elif event.key == pygame.K_q:
                        sys.exit()
                    elif event.key == pygame.K_SPACE:
                        self._fire_bullet()
                    
    

    def _check_update(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        
        pygame.display.flip()

    def _fire_bullet(self):

        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullet(self):
         
         self.bullets.update()
         for bullet in self.bullets.copy(): #To delete bulltes
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
                print(len(self.bullets))

    def _create_fleet(self): 

        alien = Alien(self)
        self.aliens.add(alien)  
         

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()