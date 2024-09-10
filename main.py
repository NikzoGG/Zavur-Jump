import pygame
from sys import exit

#TO DO
#project done


pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('123')
clock = pygame.time.Clock()

#loading nikozavur
nikozavur = pygame.image.load('assets/nikozavur.png')
nikozavur_rect = nikozavur.get_rect(midbottom=(80,620))

#loadvane na font za pisane
font1 = pygame.font.Font('assets/score.ttf',40)
font2 = pygame.font.Font('assets/score.ttf',25)

#suzdavane ne funkciq za pisane na tekst
def drawtext(text,font,text_col,x,y):
    img = font.render(text,True,text_col)
    screen.blit(img,(x,y))

#loading obstacles
cactus1 = pygame.image.load('assets/cactus1.png')
cactus1_rect = cactus1.get_rect(midbottom=(1800,655))
cactus2 = pygame.image.load('assets/cactus2.png')
cactus2_rect = cactus2.get_rect(midbottom=(2200,655))
cactus3 = pygame.image.load('assets/cactus3.png')
cactus3_rect = cactus3.get_rect(midbottom=(1000,655))

#loading sky
sky = pygame.image.load('assets/sky.png')
sky_rect = sky.get_rect(midbottom=(100,100))
sky_rect.y = 0
sky_rect.x = 0

#loading endscreen
endscreen = pygame.image.load('assets/endscreen.png')
endscreen_rect = endscreen.get_rect(midbottom=(3000,3000))

#loading ground
ground = pygame.image.load('assets/ground.jpg')
ground_rect = ground.get_rect(midbottom=(640,1370))

#game variables
gravity = 0
score = 0
gamestarted = True
gameended = False
timer = 0
timer2 = 0
highjump = False
highjumpactivated = False
startedtimer1 = True
startedtimer2 = False

def showdeathscreen(ground_rect,sky_rect,cactus3_rect,cactus2_rect,cactus1_rect,nikozavur_rect):
    endscreen_rect.x = 0
    endscreen_rect.y = 0
    ground_rect.x = 3000
    ground_rect.y = 3000
    sky_rect.x = 3000
    sky_rect.y = 3000
    nikozavur_rect.x = 3000
    nikozavur_rect.y = 3000
    cactus3_rect.x = 3000
    cactus3_rect.y = 3000
    cactus2_rect.x = 3000
    cactus2_rect.y = 3000
    cactus1_rect.x = 3000
    cactus1_rect.y = 3000

running = True
while running:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and nikozavur_rect.colliderect(ground_rect):
                gravity -= 22

    #gravity
    gravity += 1
    nikozavur_rect.y += gravity

    #increasing score
    if gameended == False:
        score += 0.2

    #collsions
    if nikozavur_rect.colliderect(ground_rect):
        nikozavur_rect.y = 545
        gravity = -1


    #high jump
    if startedtimer1 == True:
        timer += 1

    if timer == 800:
        highjump = True
        timer = 0
        startedtimer1 = False

    if keys[pygame.K_g] and highjump == True:
        highjumpactivated = True

    if keys[pygame.K_SPACE] and highjumpactivated == True:
        gravity -= 2
        startedtimer2 = True
        
    
    if startedtimer2 == True:
        timer2 += 1


    if timer2 == 300:
        highjumpactivated = False
        timer2 = 0
        startedtimer2 = False
        highjump = False
        startedtimer1 = True


    #making the score integer
    points = int(score)

    #moving obstacles
    if gamestarted == True:
        cactus1_rect.x -= 5
        if cactus1_rect.x < -20:
            cactus1_rect.x = 2500
    
    if gamestarted == True:
        cactus2_rect.x -= 5
        if cactus2_rect.x < -20:
            cactus2_rect.x = 1600

    if gamestarted == True:
        cactus3_rect.x -= 5
        if cactus3_rect.x < -20:
            cactus3_rect.x = 2500


    #death
    if nikozavur_rect.colliderect(cactus1_rect) or nikozavur_rect.colliderect(cactus2_rect) or nikozavur_rect.colliderect(cactus3_rect):
        gameended = True
        gamestarted = False    

    if gamestarted == False:
        showdeathscreen(ground_rect,sky_rect,cactus3_rect,cactus2_rect,cactus1_rect,nikozavur_rect)
    

    screen.fill((0,0,0))
    screen.blit(sky,sky_rect)
    if gamestarted == True:
        drawtext('Tochki: ' + str(points),font1,(0,0,0),470,200)
    if highjump == True:
        drawtext('Press G to enable HighJump',font2,(0,0,0),410,370)
    screen.blit(endscreen,endscreen_rect)
    screen.blit(cactus3,cactus3_rect)
    screen.blit(cactus2,cactus2_rect)
    screen.blit(cactus1,cactus1_rect)
    screen.blit(ground,ground_rect)
    screen.blit(nikozavur,nikozavur_rect)
    pygame.display.flip()
    clock.tick(60)