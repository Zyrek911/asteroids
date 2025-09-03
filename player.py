import sys
from constants import *
from circleshape import *
from infoboard import Lives

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
        self.dead = False
        self.respawn_time = 0
        self.invul = 0 
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        color ="white"
        if(self.invul > 0):
            color = "red"
        pygame.draw.polygon(screen, color, points=self.triangle(), width=2)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def shoot(self, dt):
        if(self.timer > 0):
            self.timer -= dt
        else:
            self.timer = PLAYER_SHOOT_COOLDOWN
            new_shot = Shot(self.position[0], self.position[1])
            new_shot.velocity = pygame.Vector2(0,1).rotate(self.rotation)
            new_shot.velocity += new_shot.velocity * PLAYER_SHOT_SPEED

    def isdead(self, lifecount, screen):
        if(self.dead):
            return
        self.dead = True
        self.kill()
        lifecount.life_decrease()
        if(lifecount.player_lives < 0):
            print("Game Over!")
            sys.exit()
        else:
            self.respawn_time = pygame.time.get_ticks() + PLAYER_RESPAWN_TIME
        
    def update(self, dt):
        if(self.invul > 0):
            self.invul = max(0, self.invul - dt)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot(dt)
            
class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
    
    def draw(self, screen):
        pygame.draw.circle(surface=screen, color="white", center=self.position, radius=self.radius, width=2)
    
    def update(self, dt):
        self.position += self.velocity * dt