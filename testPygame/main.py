import pygame
import time
import random

pygame.init()

display_witdth = 800
display_height = 600
FPS = 25

direction = "right"

screen = pygame.display.set_mode((display_witdth, display_height))
white = (255,255,255)

pygame.display.set_caption("MY GAME")
clock = pygame.time.Clock()


apppleThickness = 30
block_size = 20

black = (0,0,0)
red = (255, 0,0)
white = (255,255,255)
green = (0, 155, 0)


img = pygame.image.load('snakeHead2.png')
appleImg = pygame.image.load('apple2.png')

icon = pygame.image.load('apple2.png')
pygame.display.set_icon(icon)

smallfont = pygame.font.SysFont("comicsansms", 25)
mediumfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)

def game_intro():
    intro = True
    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                intro = False

            if event.key == pygame.K_e:
                pygame.quit()
                quit()


        screen.fill(white)
        message_to_screen("welcome to snake", green, -130, "large")
        message_to_screen("take the red appples", black, -10, "small")
        message_to_screen("the more you eat, the larger you get", black, 50, "small")
        message_to_screen("dont run over the edges, or yourself", black, 180, "small")
        message_to_screen("press c: continue, press e: quit", black, 210, "small")
        pygame.display.update()
        clock.tick(15)


def snake(block_size, snakeList):

    if direction == "right":
        head = pygame.transform.rotate(img, 270)

    if direction == "left":
        head = pygame.transform.rotate(img, 90)

    if direction == "up":
        head = img

    if direction == "down":
        head = pygame.transform.rotate(img, 180)

    screen.blit(head, (snakeList[-1][0], snakeList[-1][1]))

    for XnY in snakeList[:-1]:
        pygame.draw.rect(screen, green, [XnY[0], XnY[1], block_size, block_size])

        # pygame.draw.rect(screen, red, [randAppleX, randAppleY, block_size, block_size])

def text_objects(text, color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = mediumfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_to_screen(msg, color, y_displace = 0, size= "small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (display_witdth / 2), (display_height / 2) + y_displace
    screen.blit(textSurf, textRect)
    # screen_text = font.render(msg, True, color)
    # screen.blit(screen_text, [display_witdth/2, display_height/2])


def score(score):
    text = smallfont.render("Score: " + str(score), True, black)
    screen.blit(text, [0,0])

def pause():
    paused = True

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False

                elif event.key == pygame.K_e:
                    pygame.quit()
                    quit()

            screen.fill(white)
            message_to_screen("Paused", black, -100, "large")

            message_to_screen("press C to continue or e to quit", black, -25, "small")

            pygame.display.update()
            clock.tick(5)

def gameLoop():
    global direction

    direction = 'right'

    len_x = display_witdth / 2
    len_y = display_height / 2

    len_x_change = 10
    len_y_change = 0

    snakeList = []
    snakeLength = 1

    randAppleX = round(random.randrange(0, display_witdth - block_size))  #/ 10.0) * 10.0
    randAppleY = round(random.randrange(0, display_height - block_size))  #/ 10.0) * 10.0


    gameExit = False
    gameOver = False
    while not gameExit:

        while gameOver:
            screen.fill(white)
            message_to_screen("game over", red, -50, "large")
            message_to_screen("Press c to play again or e to quit", black, 50, "medium")
            pygame.display.update()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()




        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                gameOver = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    len_x_change = -block_size
                    len_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    len_x_change = 10
                    len_y_change = 0
                elif event.key == pygame.K_UP:
                    direction = "up"
                    len_y_change = -block_size
                    len_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    len_y_change = block_size
                    len_x_change = 0

                elif event.key == pygame.K_p:
                    pause()

            if len_x >= display_witdth or len_x < 0 or len_y >= display_height or len_y < 0:
                gameOver = True

            # if event.type == pygame.KEYUP:
            #     if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            #         len_x_change = 0
            #
            # if event.type == pygame.KEYUP:
            #     if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            #         len_y_change = 0

        len_x += len_x_change
        len_y += len_y_change
        screen.fill(white)


       # pygame.draw.rect(screen, red, [randAppleX, randAppleY, apppleThickness, apppleThickness])
        screen.blit(appleImg, (randAppleX, randAppleY))

        snakeHead = []
        snakeHead.append(len_x)
        snakeHead.append(len_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True

        snake(block_size, snakeList)
        #pygame.draw.rect(screen, green, [len_x, len_y, block_size, block_size])

        score(snakeLength -1)
        pygame.display.update()

        # if(len_x == randAppleX and len_y == randAppleY):
        #     randAppleX = round(random.randrange(0, display_witdth - block_size) / 10.0) * 10.0
        #     randAppleY = round(random.randrange(0, display_height - block_size) / 10.0) * 10.0
        #     snakeLength += 1


        # if len_x >= randAppleX and len_x <= randAppleX + apppleThickness:
        #     if len_y >= randAppleY and len_y <= randAppleY  + apppleThickness:
        #         randAppleX = round(random.randrange(0, display_witdth - block_size)) # / 10.0) * 10.0
        #         randAppleY = round(random.randrange(0, display_height - block_size)) # / 10.0) * 10.0
        #         snakeLength += 1

        if len_x > randAppleX and len_x < randAppleX + apppleThickness or len_x + block_size > randAppleX and len_x + block_size < randAppleX + apppleThickness:
            if len_y > randAppleY and len_y < randAppleY + apppleThickness:
                print(" X + Y crossorver")
                randAppleX = round(random.randrange(0, display_witdth - apppleThickness)) # / 10.0) * 10.0
                randAppleY = round(random.randrange(0, display_height - apppleThickness)) # / 10.0) * 10.0
                snakeLength += 1

            elif len_y + block_size > randAppleY and len_y + block_size < randAppleY + apppleThickness:
                print(" X + Y crossorver")
                randAppleX = round(random.randrange(0, display_witdth - apppleThickness)) # / 10.0) * 10.0
                randAppleY = round(random.randrange(0, display_height - apppleThickness)) # / 10.0) * 10.0
                snakeLength += 1

        clock.tick(FPS)

    # message_to_screen("Game over", red)
    # pygame.display.update()
    # time.sleep(2)
    pygame.quit()
    quit()

game_intro()
gameLoop()