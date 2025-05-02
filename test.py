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
direction = "left"
score = 0
lives = 1
option = True
pause = False
clock = pygame.time.Clock()

def jump():
    pass
    #player.rect.y += 5

def crouch():
    pass
        
#player
class PLAYER(pygame.sprite.Sprite):
    def __init__(self, color, radius):
        super().__init__()
        self.image = pygame.Surface([radius * 2, radius * 2], pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (radius, radius), radius) 
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = (screen.get_width() //2 , screen.get_height() // 2)

    def move(self, direction):
        old_x, old_y = self.rect.x, self.rect.y
        if direction == "right":
            self.rect.x += 2
        if direction == "left":
            self.rect.x -= 2
        if direction == "up" :
            jump()
        if direction == "down":
            crouch()
        print(self.rect.x, self.rect.y)

player = PLAYER(brown, 15)

#menu
font = pygame.font.SysFont("Times_new_roman", 48)
text1 = font.render("EXIT", True, white)
text2 = font.render("CONTINUE", True, white)

def menu():
    menu = True
    while menu:
        rect1 = text1.get_rect(topleft = (screen.get_width() //2 - text1.get_width() // 2, screen.get_height() //2 + text1.get_height()))
        rect2 = text2.get_rect(topleft = (screen.get_width() //2 - text2.get_width() // 2, screen.get_height() //2 - text2.get_height()))
        screen.fill(green)
        screen.blit(text1, rect1)
        pygame.draw.rect(screen, (blue),rect1, 5)
        screen.blit(text2, rect2)
        pygame.draw.rect(screen, (blue),rect2, 5)
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
#restart?
text5 = font.render("RESTART", True, white)
text6 = font.render("QUIT", True, white)

def restart():
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
    
#game over
def gameOver():
    global option
    if lives == 0:
        screen.fill(black)
        font = pygame.font.SysFont("Times_new_roman", 48)
        txtsurf = font.render("GAME OVER", True, white)
        screen.blit(txtsurf, (screen.get_width() //2  - txtsurf.get_width() // 2, screen.get_height() //2  - txtsurf.get_height() // 2))
        pygame.display.update()
        pygame.time.delay(3000)

        restart()

#win
def win():
    global option
    screen.fill(black)
    font = pygame.font.SysFont("Times_new_roman", 48)
    txtsurf = font.render("YOU WIN", True, white)
    screen.blit(txtsurf,(screen.get_width() //2 - txtsurf.get_width() // 2, screen.get_height() //2  - txtsurf.get_height() // 2))
    pygame.display.update()
    pygame.time.delay(3000)

    restart()

#display score
def displayScore():
    disScore = f"Score: {score}"
    font = pygame.font.SysFont("Times_new_roman", 12)
    txtsurf = font.render(disScore, True, black)
    screen.blit(txtsurf, (20,35))
    pygame.display.update()
    
#display lives
def displayLives():
    disLives = f"Lives: {lives}"
    font = pygame.font.SysFont("Times_new_roman", 12)
    txtsurf = font.render(disLives, True, black)
    screen.blit(txtsurf, (20,20))
    pygame.display.update()
    
#loose life
def looseLife():
    global lives
    lives -= 1

#gain score
def scoreGain(num):
    global score
    for i in range(0,num):
        score += 1
        screen.fill(black)
        display(Score)
        display(Lives)
        clock.tick(20)
        
#tests
def test():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                menu()

#start         
def main():
    global score
    global lives
    global pause
    global direction
    
    #start
    starting = True
    while starting:
        screen.fill(green)
        rect = pygame.draw.rect(screen, darkBrown, pygame.Rect(screen.get_width() //2 - 150,screen.get_height() //2 - 50, 300, 100),10)
        font = pygame.font.SysFont("Times_new_roman", 72)
        txtsurf = font.render("welcome", True, black)
        screen.blit(txtsurf,(screen.get_width() //2  - txtsurf.get_width() // 2, screen.get_height() //2  - txtsurf.get_height() // 2))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect.collidepoint(event.pos):
                    starting = False
                    
    score = 0
    lives = 1
    running = True
    while running:
        screen.fill(green)
        displayLives()
        displayScore()        
        screen.blit(player.image, player.rect)
        pygame.display.update()
    
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    direction = "right"
                if event.key == K_LEFT:
                    direction = "left"
                if event.key == K_UP:
                    direction = "up"
                if event.key == K_DOWN:
                    direction = "down"
                if event.key == K_ESCAPE:
                    menu()
        
        # Move
        player.move(direction)

    pygame.display.update()
    pygame.display.flip()  
    clock.tick(200)
                    
if __name__ == '__main__':
    main()
