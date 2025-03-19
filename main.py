import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
Player.containers = (updatable, drawable)
asteroids = pygame.sprite.Group()
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable,)
shots = pygame.sprite.Group()
player = Player(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, shots)

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y, shots)
    shot = Shot(x, y)
    clock = pygame.time.Clock()
    dt = 0
    asteroid_field = AsteroidField()
    updatable.add(asteroid_field)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for drawable_object in drawable:
            drawable_object.draw(screen)
        for updatable_object in updatable:
            updatable_object.update(dt)
            
            shots.update(dt)
        for shot in shots:
            shot.draw(screen)         
        for asteroid in asteroids:
            if asteroid.check_collision(player):
                sys.exit("Game over!")
            for shot in shots:
                if asteroid.check_collision(shot):
                    asteroid.split()
                    shot.kill()
                    break

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
