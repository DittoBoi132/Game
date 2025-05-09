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
tan = (188, 164, 97)

#variables
direction = "down"
score = 0
lives = 1
collisionF =False
collisionWL =False
collisionWR =False
collisionD =False
collisionBD = False
option = True
pause = False
isJump = False
changed = False
jumpCount = 10
v = 5
clock = pygame.time.Clock()
collision = False
temp = K_DOWN
stageX = 1

def crouch():
    pass
        
#player
class PLAYER(pygame.sprite.Sprite):
    def __init__(self, color, radius):
        super().__init__()
        self.image = pygame.Surface([radius * 2, radius * 2], pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (radius, radius), radius) 
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = (50 , screen.get_height()*(3/4) - 30)

    def move(self, direction):
        global isJump, jumpCount, changed
        old_x, old_y = self.rect.x, self.rect.y
        if direction == "right":
            self.rect.x += 5
        if direction == "left":
            self.rect.x -= 5
        if direction == "down":
            crouch()
        if not(isJump):
            if direction == "up":
                isJump = True
                changed = True
        else:
            if isJump and jumpCount >= -10:
                self.rect.y -= (jumpCount * abs(jumpCount)) * 0.5
                jumpCount -= 1
            else:
                jumpCount = 10
                isJump = False
        #print(self.rect.x, self.rect.y)

player = PLAYER(brown, 15)

#blocks
class BLOCK(pygame.sprite.Sprite):
    def __init__(self, color, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

#menu
font = pygame.font.SysFont("Times_new_roman", 48)
text1 = font.render("EXIT", True, black)
text2 = font.render("CONTINUE", True, black)

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
    screen.blit(txtsurf, (20,20))
    
#display lives
def displayLives():
    disLives = f"Lives: {lives}"
    font = pygame.font.SysFont("Times_new_roman", 12)
    txtsurf = font.render(disLives, True, black)
    screen.blit(txtsurf, (20,5))
    
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

#collide
def floorCollision():
    global collisionF, collisionWL,collisionWR, collisionD, collisionBD
    if pygame.sprite.spritecollide(player, Floor, False):
        collisionF = True
    if pygame.sprite.spritecollide(player, WallL, False):
        collisionWL = True
    if pygame.sprite.spritecollide(player, WallR, False):
        collisionWR = True
    if pygame.sprite.spritecollide(player, Door, False):
        collisionD = True
    if pygame.sprite.spritecollide(player, BackDoor, False):
        collisionBD = True
        
#stages
def stage():
    global colorFill
    global Floor, WallL, WallR, Door, BackDoor
    global stageX
    if stageX == 1:
        colorFill = green
        floor = BLOCK(tan, 0, screen.get_height()*(3/4), screen.get_width(), screen.get_height()*(3/4))
        wall = BLOCK(tan, 0, 0, 10, screen.get_height())
        wallR = BLOCK(tan, screen.get_width(), 0, 10, screen.get_height())
        door = BLOCK(black, screen.get_width()-10, screen.get_height()*(3/4)-50, 10, 50)
        backDoor = BLOCK(tan, 0, 0, 0, 0)
        if not isJump:
            player.rect.y = (screen.get_height()*(3/4) - 30)
            
    if stageX == 2:
        colorFill = cyan
        floor = BLOCK(tan, 0, screen.get_height()*(3/4), screen.get_width(), screen.get_height()*(3/4))
        wall = BLOCK(tan, 0, 0, 10, screen.get_height())
        wallR = BLOCK(tan, screen.get_width(), 0, 10, screen.get_height())
        door = BLOCK(black, screen.get_width()-10, screen.get_height()*(3/4)-50, 10, 50)
        backDoor = BLOCK(black, 0, screen.get_height()*(3/4)-50, 10, 50)
        if not isJump:
            player.rect.y = (screen.get_height()*(3/4) - 30)
    Floor = pygame.sprite.Group(floor)
    WallL = pygame.sprite.Group(wall)
    WallR = pygame.sprite.Group(wallR)
    Door = pygame.sprite.Group(door)
    BackDoor = pygame.sprite.Group(backDoor)
    
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
    global score, stageX
    global lives, colorFill
    global pause
    global direction
    global collisionF, collisionWL, collisionWR, collisionD, collisionBD
    global changed
    
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
    player.rect.y = (screen.get_height()*(3/4) - 30)
    while running:
        stage()
        screen.fill(colorFill)
        displayLives()
        displayScore()        
        screen.blit(player.image, player.rect)
        Floor.draw(screen)
        WallL.draw(screen)
        WallR.draw(screen)
        Door.draw(screen)
        BackDoor.draw(screen)
    
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    direction = "right"
                    temp = K_RIGHT
                if event.key == K_LEFT:
                    direction = "left"
                    temp = K_LEFT
                if event.key == K_DOWN:
                    direction = "down"
                    temp = K_DOWN
                if not isJump:
                    if event.key == K_UP:
                        direction = "up"
                if event.key == K_ESCAPE:
                    menu()

        #check collision
        floorCollision()

        # Move
        player.move(direction)
        if changed:
            direction = "down"
            changed = False
        pygame.display.update()

        #collision
        if collisionWL:
            player.rect.x += 10
            collisionWL = False
            direction = "down"
        if collisionWR:
            player.rect.x -= 10
            collisionWR = False
            direction = "down"
        if collisionD:
            stageX += 1
            player.rect.x, player.rect.y = (15 , screen.get_height()*(3/4) - 30)
            collisionD = False
        if collisionBD:
            stageX -= 1
            player.rect.x, player.rect.y = (screen.get_width()-50, screen.get_height()*(3/4) - 30)
            collisionBD = False
        if not isJump:
            if collisionF:
                pass
                player.rect.y = screen.get_height()*(3/4) - 30
                collisionF = False
        
        pygame.display.update()
        clock.tick(30)
                    
if __name__ == '__main__':
    main()


