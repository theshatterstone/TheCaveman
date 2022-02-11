import time
import random 
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

#loading images

bg_img = pygame.transform.scale(pygame.image.load('img/new-bg.jpg'), (screen_width, screen_height) )
caveman = pygame.image.load('img/CavemanNormal.png')
#stache = pygame.image.load('img/MainChr.png')
screentitle = pygame.image.load('img/TitleText.png')
# score = 
#Load font(s)

mainFont = pygame.font.SysFont('helvetica', 20)

#main chr - Stache

class chr:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def show(self,window):
        pygame.draw.rect(window, (0,0,0),(self.x,self.y, 20,20))

stache = chr(170, 230)
clock = pygame.time.Clock()
#main function

def mainGame(localstache):
    #Background image
    screen.blit(bg_img, (0,0))
    screen.blit(caveman, (50, 225))
#    screen.blit(stache, (170, 230))
    localstache = chr.show(stache,screen)
    #The Caveman Label
    screen.blit(screentitle,(15,15))
    # screen.blit(score,(screen_width score.getwidth() - 15, 15))
    pygame.display.update()

#run infinite loop
run = True
while run:
    clock.tick(FPS)
    mainGame(stache)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]: #jump
        stache.y -= 15
    
pygame.quit()