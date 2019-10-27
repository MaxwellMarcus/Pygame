import pygame
pygame.init()

screen_width = 1000
screen_height = 700

win = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption('Game')

class Player:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5

        self.is_jump = False
        self.jump_vel = 15
        self.highest_jump_vel = self.jump_vel

        self.direction = 1
        self.animation_frame = 0

        self.left = [pygame.image.load('Stick Man\\Left 1.png'),pygame.image.load('Stick Man\\Left 2.png'),pygame.image.load('Stick Man\\Left 3.png'),pygame.image.load('Stick Man\\Left 4.png'),pygame.image.load('Stick Man\\Left 5.png'),pygame.image.load('Stick Man\\Left 6.png'),pygame.image.load('Stick Man\\Left 7.png')]
        self.right = [pygame.image.load('Stick Man\\Right 1.png'),pygame.image.load('Stick Man\\Right 2.png'),pygame.image.load('Stick Man\\Right 3.png'),pygame.image.load('Stick Man\\Right 4.png'),pygame.image.load('Stick Man\\Right 5.png'),pygame.image.load('Stick Man\\Right 6.png'),pygame.image.load('Stick Man\\Right 7.png')]
        for i in self.right:
            size = i.get_rect().size
            x = size[0]
            y = size[1]
            self.right[self.right.index(i)] = pygame.transform.scale(i,(x//20,y//20))
        for i in self.left:
            size = i.get_rect().size
            x = size[0]
            y = size[1]
            self.left[self.left.index(i)] = pygame.transform.scale(i,(x//20,y//20))

    def render(self,win):
        if self.animation_frame > 20:
            self.animation_frame = 0
        if self.direction == 1:
            win.blit(self.right[self.animation_frame//3], (self.x,self.y))
        if self.direction == -1:
            win.blit(self.left[self.animation_frame//3], (self.x,self.y))


class Projectile:
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 10 * facing

    def draw(self,win):
        pygame.draw.circle(win,self.color,(self.x,self.y),self.radius,0)


player = Player(300,410,25,50)
bullets = []

run = True
while run:
    pygame.time.delay(50)

    win.fill((255,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for i in bullets:
        if i.x < screen_width and i.x > 0:
            i.x += i.vel
            i.draw(win)
        else:
            bullets.pop(bullets.index(i))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        if len(bullets) < 100:
            bullets.append(Projectile(round(player.x + player.width//2),round(player.y+player.height//2),6,(255,255,255),player.direction))

    if keys[pygame.K_LEFT] and player.x > player.vel:
        player.x -= player.vel
        player.direction = -1
        player.animation_frame += 1
    if keys[pygame.K_RIGHT] and player.x < screen_width-player.vel-player.width:
        player.x += player.vel
        player.direction = 1
        player.animation_frame += 1
    if not player.is_jump:
        if keys[pygame.K_UP]:
            player.is_jump = True
    else:
        if player.jump_vel >= -player.highest_jump_vel:
            down = 1
            if player.jump_vel < 0:
                down = -1

            player.y -= (player.jump_vel**2/2)*down
            player.jump_vel -= 1
        else:
            player.is_jump = False
            player.jump_vel = player.highest_jump_vel


    player.render(win)
    pygame.display.update()

pygame.quit()
