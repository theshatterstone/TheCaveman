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

joysticks = []
for i in range(pygame.joystick.get_count()):
    joysticks.append(pygame.joystick.Joystick(i))

for joystick in joysticks:
    joystick.init()

#Change FPS

FPS = 120
CMshowFPS = 0
movement = "Steady"
num = 0.1  

#Load font(s)

mainFont = pygame.font.SysFont('helvetica', 20)
pixelfont = pygame.font.Font('fonts/PublicPixel.ttf',20)
pixelfont_small = pygame.font.Font('fonts/PublicPixel.ttf',15)

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
wintitle = pygame.image.load('img/WinTitle.png')
intscore = 0
score = pixelfont.render(f'Score: {intscore}',1,(255,255,255))

#Change velocity (x and y)
x_vel = 10 
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

#other important variable declarations
toprand = random.randint(800,850)
botrand = random.randint(800,850)
sliprand = random.randint(800,850) 
stache = chr(170, 225)
top = TopRock(toprand, 50)
bottom = BottomRock(botrand, 290)
slip = SlipFloor(sliprand, 351)
num = random.randint(1,100)
clock = pygame.time.Clock()
cmshowfpsmultiplier = 20
cmshowfpsmultiplier_temp = cmshowfpsmultiplier 
endless = False
isTop = False
isBot = False
isSlip = False 
isjump = False
win = False
lose = False
Cavemanshow = False
startgame = False
multiplier = 5
d_dev = False
v_dev = False

#delaying function
def delay(multiplier):
    speed = 0.1/multiplier
    time.sleep(speed)

#start function
def start():
    screen.blit(bg_img, (0,0))
    screen.blit(screentitle, (308,150))
    startText = pixelfont_small.render('Press R to Start',1, (0,0,0))
    startText_endless = pixelfont_small.render('Press E for Endless Mode',1, (0,0,0))
    screen.blit(startText,(280,200))
    screen.blit(startText_endless,(220,230))
    
        
    
    
#main function

def mainGame(num,localstache,CMcount,localtop,localbottom,localslip,isTop,isBot,isSlip,Cavemanshow,intscore,multiplier): #add intscore
    #Background image
    screen.blit(bg_img, (0,0))
    localstache = chr.show(stache,screen)
    if Cavemanshow == True:
        if CMcount % 60 > 30:
            screen.blit(caveman2, (-30, 225))
        else:
            screen.blit(caveman2, (-30,230))
# Test
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
    if keys[pygame.K_SPACE] == False and stache.y == 225:  #space key here needs to be changed to joystick controls
        delay(multiplier)
    screen.blit(screentitle,(15,15))
    intscore +=1
    score = pixelfont.render(f'Score: {intscore}',1,(255,255,255)) 
    screen.blit(score,((screen_width - score.get_width() - 15), 15))
    pygame.display.update()
    return num, isTop, isBot, isSlip,intscore,multiplier

#game lose function

def gamelose():
        screen.blit(bg_img, (0,0))
        screen.blit(losetitle,(340,190))
        space = pixelfont_small.render('Press R to Restart',1,(0,0,0))
        screen.blit(space,(270,220))
        finalscore = pixelfont.render(f'Final score: {intscore}',1,(255,255,255))
        screen.blit(finalscore,((screen_width - score.get_width() - 200), 15))
        pygame.display.update()

def gamewin():
    screen.blit(bg_img, (0,0))
    screen.blit(wintitle,(340,190))
    space = pixelfont_small.render('Press R to Restart',1,(0,0,0))
    screen.blit(space,(270,220))
    finalscore = pixelfont.render(f'Final score: {intscore}',1,(255,255,255))
    screen.blit(finalscore,((screen_width - score.get_width() - 200), 15))
    pygame.display.update()
    
#run infinite loop
run = True
while run:
    clock.tick(FPS)
    keys = pygame.key.get_pressed()
    
    if startgame == False:
        start()
        if keys[pygame.K_e] == True:
            print('endless mode')
            endless = True
            startgame = True
        if keys[pygame.K_r] ==  True:
            print("Test")
            startgame = True
        if keys[pygame.K_d]:
            d_dev = True
        if keys[pygame.K_v]:
            v_dev = True
        if d_dev == True and v_dev == True:
            startgame = True
            win = True
            intscore = 5001
    if startgame == True:
        if lose == False and win == False:
            #Controls
            if keys[pygame.K_SPACE] ==  True:
                isjump = True
            if isjump == True: # jump
                if isjump == False:
                    isjump = True
                if isjump == True:
                    stache.y -= y_vel
                    y_vel -= 2
                    delay(multiplier)
                    if y_vel < -23:
                        isjump = False
                        y_vel = 23
            else: 
                if stache.y != 225:
                        stache.y -= y_vel
                        y_vel -= 2
                        delay(multiplier)
                        if y_vel < -23:
                            isjump = False
                            y_vel = 23
                        pygame.display.update()
            
            if keys[pygame.K_a] or keys[pygame.K_LEFT]: # left
                if stache.x - x_vel > 0:
                    stache.x -= x_vel
                else:
                    lose = True
            if movement == "Right" or keys[pygame.K_d]: # right
                if stache.x + stache.get_width() < screen_width:
                    stache.x += x_vel
            
            if keys[pygame.K_s] or keys[pygame.K_DOWN]: # right
                if stache.x + stache.get_width() < screen_width:
                    stache.y = 225
                    y_vel = 23

            num, isTop, isBot, isSlip, intscore, multiplier = mainGame(num,stache,cavemanCount,top,bottom,slip,isTop,isBot,isSlip,Cavemanshow,intscore,multiplier) #add intscore as both returned values and var
            if isTop or isBot or isSlip:
                topoffset = (stache.x - top.x), (stache.y - top.y)
                if top.mask.overlap(stache.mask, topoffset):
                    lose = True

                botoffset = (stache.x - bottom.x), (stache.y - bottom.y)
                if bottom.mask.overlap(stache.mask, botoffset):
                    lose = True
                slipoffset = (stache.x - slip.x), (stache.y - slip.y)
                if slip.mask.overlap(stache.mask, slipoffset) and Cavemanshow == False:
                    Cavemanshow = True
                    print('cmshow now is true')
                elif slip.mask.overlap(stache.mask, slipoffset) and Cavemanshow == True and CMshowFPS > cmshowfpsmultiplier:
                    lose = True
                if Cavemanshow == True:
                    if CMshowFPS < 900:
                        CMshowFPS += 1
                    else:
                        CMshowFPS = 0
                        Cavemanshow = False

            if endless == False:
                if intscore % 300 == 0 and intscore < 3001:
                    multiplier += 0.5
                    cmshowfpsmultiplier = cmshowfpsmultiplier_temp * multiplier
                elif intscore == 5000:
                    win = True
            elif endless == True:
                if intscore % 300 == 0 and intscore < 5000:
                    multiplier += 0.5
                    cmshowfpsmultiplier = cmshowfpsmultiplier_temp * multiplier

                
            #debugging
            '''print(f'num = {num}')
            print(f'isTop = {isTop}')
            print(f'isBot = {isBot}')
            print(f'isSlip = {isSlip}')
            print(f'Cavemanshow = {Cavemanshow}')
            print(f'CMshowFPS = {CMshowFPS}')'''

            cavemanCount += 1
        elif win == True:
            gamewin()
            isTop = False
            isBot = False
            isSlip = False 
            isjump = False
            Cavemanshow = False
            CMshowFPS = 0
            multiplier = 5
            top.x = toprand
            bottom.x = botrand
            slip.x = sliprand
            if keys[pygame.K_r]:
                print('restart working')
                win = False
                intscore = 0
            else: 
                win = True
        else:
            gamelose()
            isTop = False
            isBot = False
            isSlip = False 
            isjump = False
            Cavemanshow = False
            CMshowFPS = 0
            multiplier = 5
            top.x = toprand
            bottom.x = botrand
            slip.x = sliprand
            if keys[pygame.K_r]:
                print('restart working')
                lose = False
                intscore = 0
            else: 
                lose = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            run = False
        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == 0:
                movement = "Right"
                print("Correct")
            if event.button == 2:
                isjump = True



    pygame.display.update()

pygame.quit()