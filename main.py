import pygame
from constants import *
from logger import log_state    

def main():
    # game loop
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # created clock object
    clock = pygame.time.Clock()
    dt = 0

    # infinte game loop
    while True:
        log_state()
    # working window close button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # setting up the delta time to seconds        
        delta_time = clock.tick(60)
        dt = delta_time/1000
    
    screen.fill('black')
    pygame.display.flip()
    ver = pygame.version.ver
    sc_height = SCREEN_HEIGHT
    sc_width = SCREEN_WIDTH

    print(f'Starting Asteroids with pygame version: {ver}')
    print(f'Screen width: {sc_width}\nScreen height: {sc_height}')
    

if __name__ == "__main__":
    main()
