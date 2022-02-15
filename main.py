import random
import time
#setting up pygame
import pygame 
from pygame.locals import *
pygame.font.init()
pygame.init()

#setting up display
screen_width = 800
screen_height = 400

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('The Caveman') #Game title and icon go here

game_icon = pygame.image.load('img/CavemanIcon.png')
pygame.display.set_icon(game_icon)


#Change FPS

FPS = 60

#Load font(s)

mainFont = pygame.font.SysFont('helvetica', 20)
pixelfont = pygame.font.Font('fonts/PublicPixel.ttf',20)

#loading images

bg_img = pygame.transform.scale(pygame.image.load('img/new-bg.jpg'), (screen_width, screen_height) )
caveman = pygame.image.load('img/CavemanNormal.png')
caveman2 = pygame.image.load('img/CavemanTorch.png')
cavemanCount = 0
toprockimg = pygame.image.load('img/Stalactite.png')
bottomrockimg = pygame.image.load('img/Stalagmite.png')
slipfloorimg = pygame.image.load('img/water-1(x10).png')
stachepic = pygame.image.load('img/MainChr.png')
screentitle = pygame.image.load('img/TitleText.png')
intscore = 0
#score = pixelfont.render(f'Score: {intscore}',1,(255,255,255))

#Change velocity (x and y)
x_vel = 5 #change to 4 for game updates/optimisations/improvements
y_vel = 20

#main chr - Stache

class chr:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.img = stachepic
        self.mask = pygame.mask.from_surface(self.img) # used to detect collisions
    def show(self,window):
        window.blit(self.img, (self.x,self.y))
    def get_height(self):
        return self.img.get_height() 
    def get_width(self):
        return self.img.get_width()



#obstacles classes
'''class obstacle:
    def __init__(self,x,y):
        self.x = x
        self.y = y'''

class TopRock:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.img = toprockimg
        self.mask = pygame.mask.from_surface(self.img)
    def show(self,window):
        window.blit(self.img, (self.x,self.y))
    def get_height(self):
        return self.img.get_height() 
    def get_width(self):
        return self.img.get_width()

class BottomRock:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.img = bottomrockimg
        self.mask = pygame.mask.from_surface(self.img)
    def show(self,window):
        window.blit(self.img, (self.x,self.y))
    def get_height(self):
        return self.img.get_height() 
    def get_width(self):
        return self.img.get_width()

class SlipFloor:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.img = slipfloorimg
        self.mask = pygame.mask.from_surface(self.img)
    def show(self,window):
        window.blit(self.img, (self.x,self.y))
    def get_height(self):
        return self.img.get_height() 
    def get_width(self):
        return self.img.get_width()

stache = chr(170, 230)
top = TopRock(random.randrange(800,850), 20)
bottom = BottomRock(random.randrange(800,850), 225)
slip = SlipFloor(random.randrange(800,850), 227)
clock = pygame.time.Clock()

#main function

def mainGame(localstache,CMcount,localtop,localbottom,localslip):
    #Background image
    screen.blit(bg_img, (0,0))
    screen.blit(caveman2, (0, 225))
    localstache = chr.show(stache,screen)
    randnum = random.randint(1,100)
    '''if CMcount % 60 == 0:
        screen.blit(caveman2, (0, 225))
    else:
        screen.blit(caveman, (0,225))'''
    if randnum % 1 == 0:
        localtop = TopRock.show(top,screen)
    elif randnum % 3 == 0:
        localbottom  = BottomRock.show(bottom,screen)
    elif randnum % 7 == 0:
        localslip = SlipFloor.show(slip,screen)
    if localtop != top:
        localtop.x -= x_vel
    if localbottom != bottom:
        localbottom.x -= x_vel
    if localslip != slip:
        localslip.x -= x_vel
    #The Caveman Label
    screen.blit(screentitle,(15,15))
    #screen.blit(score,((screen_width - score.get_width() - 15), 15))
    pygame.display.update()

#game lose function; final score can be added here

def gamelose():
    print('You Lose!')
    
#run infinite loop
run = True
while run:
    clock.tick(FPS)
    mainGame(stache,cavemanCount,top,bottom,slip)
    cavemanCount += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            run = False
    #Controls
    keys = pygame.key.get_pressed()
    isjump = False 
    if keys[pygame.K_SPACE] == True: # jump
        if isjump == False :
            isjump = True
        if isjump == True:
            stache.y -= y_vel
            y_vel -= 2
            time.sleep(0.1)
            if y_vel < -20:
                isjump = False
                y_vel = 20
    else: 
        if stache.y != 230:
                stache.y = 230
                pygame.display.update()
        y_vel = 20
    if keys[pygame.K_a] or keys[pygame.K_LEFT]: # left
        if stache.x - x_vel > 0:
            stache.x -= x_vel
        else:
            gamelose()
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]: # right
        if stache.x + stache.get_width() < screen_width:
            stache.x += x_vel

        
    pygame.display.update()

pygame.quit()