import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Collision Sound Effect")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Load sound effect
collision_sound = pygame.mixer.Sound("image/laser.mp3")

# Create two rectangles
rect1 = pygame.Rect(200, 250, 100, 100)
rect2 = pygame.Rect(500, 250, 100, 100)

# Speeds for moving the rectangles
rect1_speed = 5
rect2_speed = -5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Move the rectangles
    rect1.x += rect1_speed
    rect2.x += rect2_speed

    # Check for collision
    if rect1.colliderect(rect2):
        # Play the collision sound
        collision_sound.play()

        # Reverse the direction of movement after collision
        rect1_speed = -rect1_speed
        rect2_speed = -rect2_speed

    # Draw the rectangles
    pygame.draw.rect(screen, RED, rect1)
    pygame.draw.rect(screen, BLUE, rect2)

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(10)

# Quit Pygame
pygame.quit()
