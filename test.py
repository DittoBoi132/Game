import time
import pygame
import sys
import random
from pygame.locals import *
pygame.init()

#screen
screen = pygame.display.set_mode((800,600),RESIZABLE)
pygame.display.set_caption("test")

#colours
white = (255,255,255)
green = (0, 255, 0)
yellow = (255,255,0)
black = (0,0,0)
blue = (0,0,255)
red = (255,0,0)
cyan = (0,255,255)
pink = (255,153,255)
orange = (255,143,0)
purple = (255, 0, 255)
brown = (141, 111, 100)
darkBrown = (91, 74, 68)

#variables
score = 0
lives = 1
option = True
clock = pygame.time.Clock()

#menu
font = pygame.font.SysFont("Times_new_roman", 48)
text1 = font.render("EXIT", True, white)
text2 = font.render("CONTINUE", True, white)

def menu():
    menu = True
    while menu:
        rect1 = text1.get_rect(topleft = (screen.get_width() //2 - text1.get_width() // 2, screen.get_height() //2 + text1.get_height()))
        rect2 = text2.get_rect(topleft = (screen.get_width() //2 - text2.get_width() // 2, screen.get_height() //2 - text2.get_height()))
        screen.fill(black)
        screen.blit(text1, rect1)
        pygame.draw.rect(screen, (darkBrown),rect1, 5)
        screen.blit(text2, rect2)
        pygame.draw.rect(screen, (darkBrown),rect2, 5)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect1.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
                    running = False
                    menu = False
                if rect2.collidepoint(event.pos):
                    menu = False

#game over
text5 = font.render("RESTART", True, white)
text6 = font.render("QUIT", True, white)

def gameOver():
    global option
    if lives == 0:
        screen.fill(black)
        font = pygame.font.SysFont("Times_new_roman", 48)
        txtsurf = font.render("GAME OVER", True, white)
        screen.blit(txtsurf, (screen.get_width() //2  - txtsurf.get_width() // 2, screen.get_height() //2  - txtsurf.get_height() // 2))
        pygame.display.update()
        pygame.time.delay(3000)

        while option:
            rect1 = text5.get_rect(topleft = (screen.get_width() //2 - text5.get_width() // 2, screen.get_height() //2 + text4.get_height()))
            rect2 = text6.get_rect(topleft = (screen.get_width() //2 - text6.get_width() // 2, screen.get_height() //2 - text3.get_height()))
            screen.fill(black)
            screen.blit(text5, rect1)
            pygame.draw.rect(screen, (darkBrown),rect1, 5)
            screen.blit(text6, rect2)
            pygame.draw.rect(screen, (darkBrown),rect2, 5)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if rect1.collidepoint(event.pos):
                        main()
                        option = False
                    if rect2.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()

#win
def win():
    global option
    screen.fill(black)
    font = pygame.font.SysFont("Times_new_roman", 48)
    txtsurf = font.render("YOU WIN", True, white)
    screen.blit(txtsurf,(screen.get_width() //2 - txtsurf.get_width() // 2, screen.get_height() //2  - txtsurf.get_height() // 2))
    pygame.display.update()
    pygame.time.delay(3000)

    while option:
        rect1 = text5.get_rect(topleft = (screen.get_width() //2 - text5.get_width() // 2, screen.get_height() //2 + text4.get_height()))
        rect2 = text6.get_rect(topleft = (screen.get_width() //2 - text6.get_width() // 2, screen.get_height() //2 - text3.get_height()))
        screen.fill(black)
        screen.blit(text5, rect1)
        pygame.draw.rect(screen, (darkBrown),rect1, 5)
        screen.blit(text6, rect2)
        pygame.draw.rect(screen, (darkBrown),rect2, 5)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect1.collidepoint(event.pos):
                    game()
                    option = False
                if rect2.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
                        
def main():
    
if __name__ == '__main__':
    main()
