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

#Change FPS

FPS = 60

#Load font(s)

mainFont = pygame.font.SysFont('helvetica', 20)
pixelfont = pygame.font.Font('fonts/PublicPixel.ttf',20)

#loading images

bg_img = pygame.transform.scale(pygame.image.load('img/new-bg.jpg'), (screen_width, screen_height) )
caveman = pygame.image.load('img/CavemanNormal.png')
stache = pygame.image.load('img/MainChr.png')
screentitle = pygame.image.load('img/TitleText.png')
intscore = 0
#score = pixelfont.render(f'Score: {intscore}',1,(255,255,255))

#Change velocity (x and y)
x_vel = 5
y_vel = 20

#main chr - Stache

class chr:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.img = stache
        self.mask = pygame.mask.from_surface(self.img) # used to detect collisions
    def show(self,window):
        window.blit(self.img, (self.x,self.y))
    def get_height(self):
        return self.img.get_height() 
    def get_width(self):
        return self.img.get_width()

stache = chr(170, 230)
clock = pygame.time.Clock()
#main function

def mainGame(localstache):
    #Background image
    screen.blit(bg_img, (0,0))
    screen.blit(caveman, (50, 225))
    localstache = chr.show(stache,screen)
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
    mainGame(stache)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    isjump = False
    keys = pygame.key.get_pressed()
    
    if isjump == False and keys[pygame.K_SPACE]:
        isjump = True
    if isjump == True:
        stache.y -= y_vel
        y_vel -= 2
        time.sleep(0.1)
        if y_vel < -20:
            isjump = False
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