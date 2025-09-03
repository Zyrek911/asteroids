import sys
import pygame
from player import Player, Shot
from infoboard import *
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

    board = ScoreBoard(10,10)
    life_counter = Lives(SCREEN_WIDTH -10 , 10)

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill(color="black")
        board.draw(screen)
        life_counter.draw(screen)

        updatables.update(dt)
        for enemy in asteroids:
            if(ship.collision_check(enemy) and ship.invul <= 0):
                ship.isdead(life_counter, screen)
            for bullet in shots:
                if(bullet.collision_check(enemy)):
                    bullet.kill()
                    enemy.split()
                    board.score_increase()
                    break

        if(ship.dead and pygame.time.get_ticks() >= ship.respawn_time):
            ship = Player(x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2)
            ship.respawn_time = 0
            ship.invul = PLAYER_INVUL
        
        if(board.score == 50):
            print("You have won!")
            sys.exit()

        for items in drawables:
            items.draw(screen)
        pygame.display.flip()
        dt = (fps_timer.tick(60)/1000)

if __name__ == "__main__":
    main()
