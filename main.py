import pygame
from constants import *

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

        # Refresh Screen, Call last in loop
        pygame.display.flip()

    print(f"Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()