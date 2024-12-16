import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Retro Start Button")

# Colors
ORANGE = (230, 91, 24)
WHITE = (255, 255, 255)
BROWN = (80, 40, 20)
BLACK = (0, 0, 0)
# Fonts (Use a pixel font for more retro look if available)
def load_font(size):
    try:
        return pygame.font.Font("assets/pixel_font.ttf", size)  # Add your pixel font path
    except FileNotFoundError:
        return pygame.font.SysFont("Courier", size)  # Fallback to Courier

font = load_font(50)

class Button:
    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 200, 50
        self.button_color = ORANGE
        self.shadow_color = BROWN
        self.border_color = WHITE
        self.text_color = WHITE
        self.font =font
        
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.shadow_offset = 10

        self._prep_msg(msg)
    
    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def _draw_button(self):
        # Draw shadow
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

# Main game loop
class DummyGame:
    def __init__(self):
        self.screen = screen

dummy_game = DummyGame()
button = Button(dummy_game, "START")

running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if button.rect.collidepoint(mouse_x, mouse_y):
                print("START button clicked!")

    # Draw the button
    button._draw_button()

    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
