import pygame
from constants import *
pygame.init()

class InfoBoard:
    def __init__(self, x, y):
        self.infoposition = pygame.Vector2(x,y)
        self.font = pygame.font.Font(None, 50)
    
    def display():
        pass

    def update():
        pass

class ScoreBoard(InfoBoard):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.score = 0
        
    def draw(self, screen):
        self.score_count = self.font.render(f"Score: {self.score}", True, (255,255,255))
        self.score_box = self.score_count.get_rect(topleft=(self.infoposition.x, self.infoposition.y))
        screen.blit(self.score_count, self.score_box)

    def score_increase(self):
        self.score += 1

class Lives(InfoBoard):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.player_lives = PLAYER_MAX_LIVES
        
    def draw(self, screen):
        self.life_count = self.font.render(f"Life: {self.player_lives}", True, (255,255,255))
        self.life_box = self.life_count.get_rect(topright=(self.infoposition.x, self.infoposition.y))
        screen.blit(self.life_count, self.life_box)

    def life_decrease(self):
        self.player_lives -= 1