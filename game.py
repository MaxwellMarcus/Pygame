import pygame
pygame.init()

screen_width = 500
screen_height = 500

win = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption('Game')

x = 50
y = 300
width = 40
height = 60
vel = 5

is_jump = False
jump_vel = 5
highest_jump_vel = jump_vel

left = False
right = False
animation_frame = 0

run = True
while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 500-vel-width:
        x += vel
    if not is_jump:
        if keys[pygame.K_SPACE]:
            is_jump = True
    else:
        if jump_vel >= -highest_jump_vel:
            down = 1
            if jump_vel < 0:
                down = -1

            y -= (jump_vel**2/2)*down
            jump_vel -= 1
        else:
            is_jump = False
            jump_vel = highest_jump_vel


    win.fill((0,0,0))
    pygame.draw.rect(win, (255,0,0),(x,y,width,height))
    pygame.display.update()

pygame.quit()
