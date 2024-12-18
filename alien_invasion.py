import sys
import pygame
from time import sleep
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from gameStats import GameStats
from button import Button
from scorebord import Scorebord

class AlienInvasion:

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("alien Invasion")

        self.stats = GameStats(self)
        self.sb  =Scorebord(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group() # initializing bullets list
        self.aliens = pygame.sprite.Group() # initializing aliens list

        self._create_fleet()

        self.play_button = Button(self,"Play")
    

    def run_game(self):

        while True:
            
            self._check_event()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullet()
                self._update_aliens()

            self._check_update()

    
    def _check_event(self):

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_play_button(mouse_pos)

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
        self.sb.show_score()

        if not self.stats.game_active:
            self.play_button._draw_button()
        
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
        self._check_bullet_alien_collision()


    def _check_bullet_alien_collision(self):
            
            print(len(self.bullets))
            collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

            if collisions:
                for aliens in collisions.values():
                    self.stats.score += self.settings.alien_point * len(aliens)

                self.stats.score += self.settings.alien_point 
                self.sb.prep_score()
                self.sb.check_high_score()

            if not self.aliens:
                self.bullets.empty()
                self._create_fleet()
                self.settings.increse_speed()
                self.stats.level += 1
                self.sb.prep_level()


    def _create_fleet(self): 

        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien_width = alien.rect.width
        available_space_x = self.settings.screen_width - (2 * alien_width) # two spaces in both side
        number_alien_x = int(available_space_x / (2 * alien_width)) # 2 * alien_width because we want one alien then one space and so on...

        ship_height = self.ship.rect.height
        
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        for row_numbers in range(number_rows):
            for alien_number in range(number_alien_x):
                self._create_alien(alien_number,row_numbers)


    def _create_alien(self,alien_number,row_number):

        alien = Alien(self)
        alien_width,alien_height = alien.rect.size
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)
    

    def _update_aliens(self):

        self._check_fleet_edges()
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship,self.aliens):
           self._ship_hit()
           self._check_alien_bottom()
    

    def _check_fleet_edges(self):

        for alien in self.aliens.sprites():
            if alien.check_edge():
                self._change_fleet_direction()
                break
    

    def _change_fleet_direction(self):
        
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.drop_speed
        self.settings.fleet_direction *= -1


    def _ship_hit(self):

        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.sb.prep_ships()
            
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            self.ship._center_ship()

            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
    

    def _check_alien_bottom(self):

        screen_rect = self.screen.get_rect()

        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break
        

    def _check_play_button(self, mouse_pos):
       
        if self.play_button.rect.collidepoint(mouse_pos):

            button_clicked = self.play_button.rect.collidepoint(mouse_pos)
            
            if button_clicked and not self.stats.game_active:
                self.settings.initialize_dynamic_settings()
                self.stats.reset_stats()
                self.aliens.empty()
                self.bullets.empty()
                self._create_fleet()
                self.ship._center_ship()
                self.stats.game_active = True
                self.sb.prep_score()
                self.sb.prep_level()
                self.sb.prep_ships()
                pygame.mouse.set_visible(False)


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()