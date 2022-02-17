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
toprockimg = pygame.image.load('img/Stalactite-new.png')
bottomrockimg = pygame.image.load('img/Stalagmite-new.png')
slipfloorimg = pygame.image.load('img/water-1(x10)-new.png')
stachepic = pygame.image.load('img/MainChr.png')
screentitle = pygame.image.load('img/TitleText.png')
losetitle = pygame.image.load('img/LoseTitle.png')
intscore = 0
#score = pixelfont.render(f'Score: {intscore}',1,(255,255,255))

#Change velocity (x and y)
x_vel = 10 #change to 4 for game updates/optimisations/improvements
y_vel = 23

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



#obstacles classes inheritance problems with obstacle class, so is currently not used
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
toprand = random.randint(800,850)
botrand = random.randint(800,850)
sliprand = random.randint(800,850) 
stache = chr(170, 225)
top = TopRock(toprand, 50)
bottom = BottomRock(botrand, 290)
slip = SlipFloor(sliprand, 351)
num = random.randint(1,100)
clock = pygame.time.Clock()
isTop = False
isBot = False
isSlip = False 
lose = False
#main function

def mainGame(num,localstache,CMcount,localtop,localbottom,localslip,isTop,isBot,isSlip):
    #Background image
    screen.blit(bg_img, (0,0))
    #screen.blit(caveman2, (-30, 225))
    localstache = chr.show(stache,screen)
    if CMcount % 60 > 30:
        screen.blit(caveman2, (-30, 225))
    else:
        screen.blit(caveman, (-30,225))
    if (num % 90 == 0 or isTop) and isBot == False and isSlip == False:
        if top.x > -55:
            TopRock.show(top,screen)
            top.x -= x_vel
            isTop = True
        else:
            isTop = False
            top.x = random.randint(800,850)
    if (num % 40 == 0 or isBot) and isTop == False and isSlip == False:
        if bottom.x > -60:
            BottomRock.show(bottom,screen)
            bottom.x -= x_vel
            isBot = True
            print(f'bottom.x = {bottom.x}')
        else:
            isBot = False
            bottom.x = random.randint(800,850)
    if (num % 50 == 0 or isSlip) and isTop == False and isBot == False:
        if slip.x > -60:
            SlipFloor.show(slip,screen)
            slip.x -= x_vel
            isSlip = True
        else:
            isSlip = False
            slip.x = random.randint(800,850)

    '''if top.x != -55 and isTop:
        top.x -= x_vel
    if bottom.x != -60 and isBot:
        bottom.x -= x_vel
    if slip.x != -125 and isSlip:
        slip.x -= x_vel'''
    num += 1
    if keys[pygame.K_SPACE] == False and stache.y == 225:
        time.sleep(0.1)
    #The Caveman Label
    screen.blit(screentitle,(15,15))
    #screen.blit(score,((screen_width - score.get_width() - 15), 15))
    pygame.display.update()
    return num, isTop, isBot, isSlip

#game lose function; final score can be added here

def gamelose():
        screen.blit(bg_img, (0,0))
        screen.blit(losetitle,(340,190))
        #finalscore = pixelfont.render(f'Final score: {intscore}',1,(255,255,255))
        #screen.blit(finalscore,((screen_width - score.get_width() - 15), 15))
        pygame.display.update()
    
#run infinite loop
run = True
while run:
    clock.tick(FPS)
    if lose == False:
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
                if y_vel < -23:
                    isjump = False
                    y_vel = 23
        else: 
            if stache.y != 225:
                    stache.y -= y_vel
                    y_vel -= 2
                    time.sleep(0.1)
                    if y_vel < -23:
                        isjump = False
                        y_vel = 23
                    pygame.display.update()
        
        if keys[pygame.K_a] or keys[pygame.K_LEFT]: # left
            if stache.x - x_vel > 0:
                stache.x -= x_vel
            else:
                lose = True
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]: # right
            if stache.x + stache.get_width() < screen_width:
                stache.x += x_vel
        
        if keys[pygame.K_s] or keys[pygame.K_DOWN]: # right
            if stache.x + stache.get_width() < screen_width:
                stache.y = 225
                y_vel = 23

        num, isTop, isBot, isSlip = mainGame(num,stache,cavemanCount,top,bottom,slip,isTop,isBot,isSlip)
        if isTop or isBot or isSlip:
            topoffset = (stache.x - top.x), (stache.y - top.y)
            if top.mask.overlap(stache.mask, topoffset):
                lose = True

            botoffset = (stache.x - bottom.x), (stache.y - bottom.y)
            if bottom.mask.overlap(stache.mask, botoffset):
                lose = True
            slipoffset = (stache.x - slip.x), (stache.y - slip.y)
            if slip.mask.overlap(stache.mask, slipoffset):
                lose = True

        print(f'num = {num}')
        print(f'isTop = {isTop}')
        print(f'isBot = {isBot}')
        print(f'isSlip = {isSlip}')
        cavemanCount += 1
    else:
        gamelose()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            run = False

    pygame.display.update()

pygame.quit()