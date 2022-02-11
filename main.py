#setting up pygame
import pygame 
from pygame.locals import *

pygame.init()
#setting up display
screen_width = 800
screen_height = 400

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('The Caveman') #Game title and icon go here

#loading images

bg_img = pygame.image.load('img/blank_bg.jpg')
caveman = pygame.image.load('img/CavemanNormal.png')

#run infinite loop
run = True
while run:

    screen.blit(bg_img, (0,0))
    screen.blit(caveman, (100, 20))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()