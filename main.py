import pygame
from constants import *
from player import Player

# Set FPS limit prior to game loop
# Create time clock object
clock = pygame.time.Clock()
# Delta time setup 
dt = 0
# Instantiate a player object
p1 = Player(
    x= (SCREEN_WIDTH / 2),
    y= (SCREEN_HEIGHT / 2)
)

def main():
    # Initialize pygame
    pygame.init()
    # Set new GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Game Loop
    while True:
        # Check if user closes window/close game if they do
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Fill screen with color black
        screen.fill((0,0,0))

        # Render the player
        p1.draw(screen)

        # Refresh Screen, Call last in loop
        pygame.display.flip()

        # Wait 1/60th of second, limit to 60FPS
        clock.tick(60)
        # Save Delta time value in milliseconds
        dt = clock.tick(60) / 1000

    print(f"Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()