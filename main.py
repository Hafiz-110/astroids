import pygame
from constants import *
from logger import log_state    
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # groups    
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()       # hold the objects that can be upgraded
    drawable = pygame.sprite.Group()        # hold the objects that can be drawn

    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)       # assigned containers before instance
    AsteroidField.containers = (updatable, )

    # initiate player object
    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2
    player = Player(x, y)
    asteroid_field = AsteroidField()
    
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

        # update all updatable objects
        updatable.update(dt)

        # drawings
        screen.fill('black')
        for i in drawable:
            i.draw(screen)
            
        pygame.display.flip()
        
    ver = pygame.version.ver
    sc_height = SCREEN_HEIGHT
    sc_width = SCREEN_WIDTH

    print(f'Starting Asteroids with pygame version: {ver}')
    print(f'Screen width: {sc_width}\nScreen height: {sc_height}')
    

if __name__ == "__main__":
    main()
