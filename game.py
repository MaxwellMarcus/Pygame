import pygame
pygame.init()

screen_width = 500
screen_height = 500

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
        self.jump_vel = 5
        self.highest_jump_vel = self.jump_vel

        self.right = False
        self.left = False
        self.animation_frame = 0



player = Player(300,410,64,64)


run = True
while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > player.vel:
        player.x -= player.vel
    if keys[pygame.K_RIGHT] and player.x < 500-player.vel-player.width:
        player.x += player.vel
    if not player.is_jump:
        if keys[pygame.K_SPACE]:
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


    win.fill((0,0,0))
    pygame.draw.rect(win, (255,0,0),(player.x,player.y,player.width,player.height))
    pygame.display.update()

pygame.quit()
