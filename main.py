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

#loading images

bg_img = pygame.transform.scale(pygame.image.load('img/new-bg.jpg'), (screen_width, screen_height) )
caveman = pygame.image.load('img/CavemanNormal.png')
stache = pygame.image.load('img/MainChr.png')

#Load font(s)

mainFont = pygame.font.SysFont('helvetica', 20)

#main function

def mainGame():
    screen.blit(bg_img, (0,0))
    screen.blit(caveman, (50, 225))
    screen.blit(stache, (170,230))

#run infinite loop
run = True
while run:

    mainGame()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()