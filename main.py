import pygame
import sys
from shot import Shot
from asteroidfield import AsteroidField
from asteroid import Asteroid
from player import Player
from logger import log_state, log_event
from constants import * 


def main():
    dt = 0

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    print(f"Starting Asteroids with pygame version {pygame.version.ver}")
    print(f'Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}')
    # create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    

    # add classes to groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable) 
    Shot.containers = (shots, updatable, drawable)


    # initiate objects
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # updaters
        updatable.update(dt)
        for obj in asteroids:
            if obj.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

            for shot in shots:
                if shot.collides_with(obj):
                    log_event("asteroid_shot")
                    shot.kill()
                    obj.kill()

        # rendering
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
