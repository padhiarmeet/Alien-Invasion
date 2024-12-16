import pygame.font

ORANGE = (230, 91, 24)
WHITE = (255, 255, 255)
BROWN = (80, 40, 20)
BLACK = (0, 0, 0)

class Button:

    def __init__(self, ai_game, msg):
       
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 200, 50
        # self.button_color = (0, 255, 0)
        # self.text_color = (255, 255, 255)
        self.button_color = ORANGE
        self.shadow_color = BROWN
        self.border_color = WHITE
        self.text_color = WHITE
        #########################
        self.font = pygame.font.SysFont(None, 45)
        
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        #############################
        self.shadow_offset = 10
        #############################
        self._prep_msg(msg)
    

    def _prep_msg(self,msg):

        self.msg_image = self.font.render(msg, True, self.text_color,self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center


    def _draw_button(self):
        
        # self.screen.fill(self.button_color,self.rect)
        # self.screen.blit(self.msg_image,self.msg_image_rect)
        shadow_rect = self.rect.move(self.shadow_offset, self.shadow_offset)
        pygame.draw.rect(self.screen, self.shadow_color, shadow_rect)
        
        # Draw button body
        pygame.draw.rect(self.screen, self.button_color, self.rect)
        
        # Draw border
        border_thickness = 6
        inner_rect = self.rect.inflate(-border_thickness, -border_thickness)
        pygame.draw.rect(self.screen, self.border_color, inner_rect, border_thickness)
        
        # Draw text
        self.screen.blit(self.msg_image, self.msg_image_rect)
