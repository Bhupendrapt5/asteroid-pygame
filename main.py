import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")

    # Initialize Pygame 
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock  = pygame.time.Clock()
    dt: float = 0.0

    # Main game loop
    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        # Clear the screen
        screen.fill("black")
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000
        print("dt > ", dt)

if __name__ == "__main__":
    main()
