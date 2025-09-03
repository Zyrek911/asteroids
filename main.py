import sys
import pygame
from player import Player, Shot
from asteroidfield import * 
from constants import *

def main():
    pygame.init()
    fps_timer = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables,)
    Shot.containers = (shots, updatables, drawables)

    ship = Player(x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color="black")
        updatables.update(dt)
        for enemy in asteroids:
            if(ship.collision_check(enemy)):
                print("Game over!")
                sys.exit()
            for bullet in shots:
                if(bullet.collision_check(enemy)):
                    bullet.kill()
                    enemy.split()
                    break
        for items in drawables:
            items.draw(screen)
        pygame.display.flip()
        dt = (fps_timer.tick(60)/1000)

if __name__ == "__main__":
    main()
