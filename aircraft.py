# importing all modules
import math
import os
import pickle
import random
import sys
import pygame
import time
# to create countdown
time1 = True

# initiating pygame
pygame.init()
clock = pygame.time.Clock()
display_height = 1000
display_width = 700
win = pygame.display.set_mode(
    (display_height, display_width))  # creating window

# loading all images
icon = pygame.image.load('player.png')
caption = pygame.display.set_caption('Jet shooter')
player = pygame.image.load('player.png')
bullet3 = pygame.image.load('bullet1.png')
player_bullet = pygame.image.load('bullet.png')
#  loaded background
back = pygame.image.load('back.png').convert_alpha()
back1 = pygame.image.load('back.png').convert_alpha()
crashimage = pygame.image.load('gameover.png')
input_back = pygame.image.load('input_back.png')
game_intro = pygame.image.load('background.png')
table = pygame.image.load('Capture.PNG')

# intialising icon for pygame window
icon1 = pygame.display.set_icon(icon)

# getting the player size
player_size = player.get_size()
c, d = player_size
square = player_bullet.get_rect()
# converted to images to rect

user_text = ''
bullet2 = bullet3.get_rect()
rect = player.get_rect()

basic_font = pygame.font.Font('font.ttf', 32)
back_size = back.get_size()
w, h = back_size
rect1 = back.get_rect()
rect1.x = w
rect1.y = 0
# to display the name of the player after player crashes
name = []

# loading all sounds and music
button = pygame.mixer.Sound('BUTTON.wav')
pygame.mixer.music.load('music.mp3')
crash_sound = pygame.mixer.Sound('crash.wav')

# loaded intro background
user_text1 = ' '
# background
rect2 = back1.get_rect()
rect2.x = 0
rect2.y = 0

active = False
pause = False

# creating color
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
k = (118, 131, 0)
black = 0, 0, 0
white = (255, 255, 255)
unknown = (27, 5, 102)
bright_green = (0, 200, 0)
bright_red = (200, 0, 0)
bright_blue = (0, 0, 200)
cloud1 = []
low_black = (26, 25, 27)
light_black = (43, 43, 45)

# cloud displaying
num = 5
cloud_x = [534, 124, 654, 856, 123, 645]
cloud_y = [534, 124, 321, 546, 123, 491]
# inserting cloud images in list to display randomly
for i in range(num - 1):
    cloud1.append(pygame.image.load('cloud.png'))


# creating bullet list
bulletlist = []
bulletx = []
bullety = []
num_bullet = 9
for i in range(num_bullet - 1):
    bulletlist.append(pygame.image.load('bullet1.png'))
    a = random.randint(1000, 1500)
    b = random.randint(0, 650)
    bulletx.append(a)
    bullety.append(b)
bullet_x = []
bullet_state = 'ready'


# added a unpause function to exit pause fucntion


def unpaused():
    global pause
    pause = False


# create a function to fire bullet


def fire(bullet, x, y):
    global bullet_state
    bullet_state = 'fire'
    win.blit(bullet, (x + 16, y + 16))


# to change the bullet_state

def test1():
    global bullet_state
    bullet_state = 'ready'

# created a function to display text


def text_object(text, font, color):
    textsurf = font.render(text, True, color)
    return textsurf, textsurf.get_rect()


def message_display(text, a, b, color):
    largetext = pygame.font.Font('Consolas.ttf', 115)
    textsurf, textrect = text_object(text, largetext, color)
    textrect.center = (a, b)
    win.blit(textsurf, textrect)
    pygame.display.update()


def message_display1(text, a, b, color):
    largetext = pygame.font.Font('Consolas.ttf', 115)
    textsurf, textrect = text_object(text, largetext, color)
    textrect.center = (int(a), int(b))
    win.blit(textsurf, textrect)

# added message display function to blit text on to the window


def message_display2(text, a, b, color):
    smalltext = pygame.font.Font('font.ttf', 30)
    textsurf, textrect = text_object(text, smalltext, color)
    textrect.center = (int(a), int(b))
    win.blit(textsurf, textrect)


# to display text


def crash1():
    message_display1('Fighter', display_height / 2, 300, k)


def scoreboard():
    f = open('names.txt', 'r')
    f2 = open('score.txt', 'r')
    line1 = f2.read()
    word1 = line1.split()
    line = f.read()
    word = line.split()

    font = pygame.font.Font('font.ttf', 40)
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                quit()
        win.fill(green)
        win.blit(table, (100, 300))
        message_display2('Player_name', 185, 273, black)
        message_display2('Score', 510, 273, black)
        x = [473, 473, 473, 473, 473, 473]
        y = [304, 310 + 40, 310 + 40 + 50, 310 + 40 + 40 + 54,
             310 + 40 + 40 + 30 + 25, 310 + 40 + 40 + 30 + 60 + 100]

        x1 = [104, 104, 104, 104, 104]
        y1 = [300, 350, 350 + 40, 350 + 40 + 55, 350 + 40 + 40 + 57]
        xnew = []
        ynew = []
        xnew1 = []
        ynew1 = []
        list = []
        for i in word:
            list.append(font.render(i, True, (0, 0, 0)))
        score12 = []
        for p in word1:
            score12.append(font.render(p, True, (0, 0, 0)))

        if len(word) == 1:
            xnew.clear()
            ynew.clear()
            for i in range(1):
                xnew.append(x[i])
                ynew.append(y[i])
                xnew1.append(x1[i])
                ynew1.append(y1[i])
                win.blit(score12[i], (xnew[i], ynew[i]))
                win.blit(list[i], (xnew1[i], ynew1[i]))

        if len(word) == 2:
            xnew.clear()
            ynew.clear()
            for i in range(2):
                xnew.append(x[i])
                ynew.append(y[i])
                xnew1.append(x1[i])
                ynew1.append(y1[i])
                win.blit(score12[i], (xnew[i], ynew[i]))
                win.blit(list[i], (xnew1[i], ynew1[i]))
        if len(word) == 3:
            xnew.clear()
            ynew.clear()
            for i in range(3):
                xnew.append(x[i])
                ynew.append(y[i])
                xnew1.append(x1[i])
                ynew1.append(y1[i])
                win.blit(score12[i], (xnew[i], ynew[i]))
                win.blit(list[i], (xnew1[i], ynew1[i]))
        if len(word) == 4:
            xnew.clear()
            ynew.clear()
            for i in range(4):
                xnew.append(x[i])
                ynew.append(y[i])
                xnew1.append(x1[i])
                ynew1.append(y1[i])
                win.blit(score12[i], (xnew[i], ynew[i]))
                win.blit(list[i], (xnew1[i], ynew1[i]))
        if len(word) == 5:
            xnew.clear()
            ynew.clear()
            for i in range(5):
                xnew.append(x[i])
                ynew.append(y[i])
                xnew1.append(x1[i])
                ynew1.append(y1[i])
                win.blit(score12[i], (xnew[i], ynew[i]))
                win.blit(list[i], (xnew1[i], ynew1[i]))

        mouse = pygame.mouse.get_pos()
        print(mouse)
        pygame.display.update()


# created a crash function to display when crashed


def crash12(playerimage, score):
    win.fill(white)
    message_display('Game over', 500, 350, black)
    font = pygame.font.Font('font.ttf', 20)
    for i in name:
        input = i + " score:"

    input_name = font.render(input + str(score), True, white)
    win.blit(input_name, (10, 10))
    while True:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        mouse = pygame.mouse.get_pos()
        if 430 < mouse[0] < 430 + 150 and 450 < mouse[1] < 50 + 450:
            pygame.draw.rect(win, low_black, (420, 430, 150, 50))
            pygame.draw.rect(win, white, (420, 570, 150, 50),2)
            message_display2('Scoreboard', (420 + 420 + 150) /
                             2, (570 + 570 + 50) / 2, green)
            message_display2('Play Again', (420 + 420 + 150) /
                             2, (430 + 430 + 50) / 2, green)
            pygame.draw.rect(win, white, (420, 500, 150, 50),2)
            message_display2('Quit', (420 + 420 + 150) / 2,
                             (500 + 500 + 50) / 2, green)
        elif 420 < mouse[0] < 420 + 150 and 520 < mouse[1] < 520 + 50:
            pygame.draw.rect(win, white, (420, 430, 150, 50),2)
            pygame.draw.rect(win, low_black, (420, 500, 150, 50))
            pygame.draw.rect(win, white, (420, 570, 150, 50),2)
            message_display2('Scoreboard', (420 + 420 + 150) /
                             2, (570 + 570 + 50) / 2, green)
            message_display2('Quit', (420 + 420 + 150) / 2,
                             (500 + 500 + 50) / 2, green)
            message_display2('Play Again', (420 + 420 + 150) /
                             2, (430 + 430 + 50) / 2, green)
        elif 420 < mouse[0] < 420 + 150 and 570 < mouse[1] < 570 + 50:
            pygame.draw.rect(win, white, (420, 430, 150, 50),2)
            pygame.draw.rect(win, white, (420, 500, 150, 50),2)
            pygame.draw.rect(win, low_black, (420, 570, 150, 50))
            message_display2('Scoreboard', (420 + 420 + 150) /
                             2, (570 + 570 + 50) / 2, green)
            message_display2('Quit', (420 + 420 + 150) / 2,
                             (500 + 500 + 50) / 2, green)
            message_display2('Play Again', (420 + 420 + 150) /
                             2, (430 + 430 + 50) / 2, green)
        else:
            pygame.draw.rect(win, white, (420, 430, 150, 50),2)
            pygame.draw.rect(win, white, (420, 500, 150, 50),2)
            pygame.draw.rect(win, white, (420, 570, 150, 50),2)
            message_display2('Scoreboard', (420 + 420 + 150) /
                             2, (570 + 570 + 50) / 2, green)
            message_display2('Play Again', (420 + 420 + 150) /
                             2, (430 + 430 + 50) / 2, green)
            message_display2('Quit', (420 + 420 + 150) / 2,
                             (500 + 500 + 50) / 2, green)
        click = pygame.mouse.get_pressed()
        if click[0] == 1 and 420 < mouse[0] < 420 + 150 and 430 < mouse[1] < 50 + 430:
            pygame.mixer.Sound.play(button)

            bulletx = []
            bullety = []
            num_bullet = 9
            for i in range(num_bullet - 1):
                a = random.randint(1000, 1500)
                b = random.randint(0, 650)
                bulletx.append(a)
                bullety.append(b)
            pygame.mixer.music.unpause()
            gameloop(playerimage)
        elif click[0] == 1 and 420 < mouse[0] < 420 + 150 and 520 < mouse[1] < 520 + 50:
            pygame.mixer.Sound.play(button)
            pygame.quit()
            sys.exit()
        elif click[0] == 1 and 420 < mouse[0] < 420 + 150 and 570 < mouse[1] < 570 + 50:
            scoreboard()
        pygame.display.update()


# created a input box for the player input their name


def playerinput(playerimage):
    global active
    color = black
    global user_text
    while True:
        win.blit(input_back, (0, 0))
        message_display2('Please Enter Your name:', 500, 200, low_black)
        a = 100
        d = 50
        rect_x = 450
        rect_y = 300
        text_surface = basic_font.render(user_text, True, black)
        win.blit(text_surface, (rect_x + 4, rect_y + 4))
        a = max(100, text_surface.get_width() + 10)
        if a > 120:
            rect.x -= 0.5

        p = pygame.draw.rect(win, color, (rect_x, rect_y, a, d), 2)
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
                quit()
            if events.type == pygame.MOUSEBUTTONDOWN:
                if p.collidepoint(events.pos):
                    active = True
                    color = red
                else:
                    active = False
                    color = black
            if events.type == pygame.KEYDOWN:
                if active == True:
                    if events.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        user_text += events.unicode
            keys = pygame.key.get_pressed()
            text = user_text
            trying = ''
            for a in text:
                if a.isalpha():
                    trying += a
            if keys[pygame.K_RETURN]:
                name.append(trying)
                f = open('names.txt', 'r')
                line = f.read()
                word = line.split()
                for i in name:
                    if len(word) >= 5:
                        f = open('names.txt', 'w')
                        f.write(i)
                        f.write('\n')
                    else:
                        f = open('names.txt', 'a+')
                        f.write(i)
                        f.write('\n')
                f.close()
                gameintro(playerimage)

            pygame.display.update()


def controls(playerimage):
    win.fill(white)
    while True:
        message_display2('USE arrow or WASD keys to move', 500, 350, black)
        message_display2('Press Space to fire the bullet', 500, 150, black)
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        mouse = pygame.mouse.get_pos()
        if 420 < mouse[0] < 420 + 150 and 450 < mouse[1] < 50 + 450:
            pygame.draw.rect(win, low_black, (420, 450, 150, 50))
            message_display2('Play ', (420 + 420 + 150) /
                             2, (450 + 450 + 50) / 2, black)
            pygame.draw.rect(win, black, (420, 520, 150, 50),2)
            message_display2('Quit', (420 + 420 + 150) / 2,
                             (520 + 520 + 50) / 2, black)
        elif 420 < mouse[0] < 420 + 150 and 520 < mouse[1] < 520 + 50:
            pygame.draw.rect(win, black, (420, 450, 150, 50),2)
            pygame.draw.rect(win, low_black, (420, 520, 150, 50),2)
            message_display2('Quit', (420 + 420 + 150) / 2,
                             (520 + 520 + 50) / 2, black)
            message_display2('Play ', (420 + 420 + 150) /
                             2, (450 + 450 + 50) / 2, black)
        else:
            pygame.draw.rect(win, black, (420, 450, 150, 50),2)
            pygame.draw.rect(win, black, (420, 520, 150, 50),2)
            message_display2('Play ', (420 + 420 + 150) /
                             2, (450 + 450 + 50) / 2, black)
            message_display2('Quit', (420 + 420 + 150) / 2,
                             (520 + 520 + 50) / 2, black)
        click = pygame.mouse.get_pressed()
        click = pygame.mouse.get_pressed()
        if click[0] == 1 and 420 < mouse[0] < 420 + 150 and 450 < mouse[1] < 50 + 450:
            pygame.mixer.Sound.play(button)
            pygame.mixer.music.unpause()
            gameloop(playerimage)
        elif click[0] == 1 and 420 < mouse[0] < 420 + 150 and 520 < mouse[1] < 520 + 50:
            pygame.mixer.Sound.play(button)
            pygame.quit()
            sys.exit()
        pygame.display.update()


# score function


def scoreimage(text):
    font = pygame.font.Font('font.ttf', 30)
    img2 = font.render('Score:' + str(text), True, (0, 0, 0))
    win.blit(img2, (0, 0))


# created a game intro scene to initialize start of the game
def escape(playerimage):
    while pause:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        message_display2('Paused', display_height / 2, 300, k)
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pos()
        if 420 < mouse[0] < 420 + 150 and 460 < mouse[1] < 50 + 460:
            pygame.draw.rect(win, black, (420, 580, 150, 50),2)
            pygame.draw.rect(win, low_black, (420, 460, 150, 50))
            pygame.draw.rect(win, black, (420, 520, 150, 50),2)
            message_display2('Continue', (420 + 420 + 150) /
                             2, (460 + 460 + 50) / 2, black)
            message_display2('Quit', (420 + 420 + 150) / 2,
                             (520 + 520 + 50) / 2, black)
            message_display2('Controls', (420 + 420 + 150) /
                             2, (580 + 580 + 50) / 2, black)
        elif 420 < mouse[0] < 420 + 150 and 520 < mouse[1] < 520 + 50:
            pygame.draw.rect(win, black, (420, 580, 150, 50),2)
            pygame.draw.rect(win, black, (420, 460, 150, 50),2)
            pygame.draw.rect(win, low_black, (420, 520, 150, 50))
            message_display2('Controls', (420 + 420 + 150) /
                             2, (580 + 580 + 50) / 2, black)
            message_display2('Quit', (420 + 420 + 150) / 2,
                             (520 + 520 + 50) / 2, black)
            message_display2('Continue', (420 + 420 + 150) /
                             2, (460 + 460 + 50) / 2, black)
        elif 420 < mouse[0] < 420 + 150 and 580 < mouse[1] < 580 + 50:
            pygame.draw.rect(win, low_black, (420, 580, 150, 50))
            pygame.draw.rect(win, black, (420, 460, 150, 50),2)
            pygame.draw.rect(win, black, (420, 520, 150, 50),2)
            message_display2('Controls', (420 + 420 + 150) /
                             2, (580 + 580 + 50) / 2, black)
            message_display2('Continue', (420 + 420 + 150) /
                             2, (460 + 460 + 50) / 2, black)
            message_display2('Quit', (420 + 420 + 150) / 2,
                             (520 + 520 + 50) / 2, black)
        else:
            pygame.draw.rect(win, black, (420, 580, 150, 50),2)
            pygame.draw.rect(win, black, (420, 460, 150, 50),2)
            pygame.draw.rect(win, black, (420, 520, 150, 50),2)
            message_display2('Controls', (420 + 420 + 150) /
                             2, (580 + 580 + 50) / 2, black)
            message_display2('Continue', (420 + 420 + 150) /
                             2, (460 + 460 + 50) / 2, black)
            message_display2('Quit', (420 + 420 + 150) / 2,
                             (520 + 520 + 50) / 2, black)
        click = pygame.mouse.get_pressed()
        if click[0] == 1 and 420 < mouse[0] < 420 + 150 and 450 < mouse[1] < 50 + 450:
            pygame.mixer.Sound.play(button)
            pygame.mixer.music.unpause()
            unpaused()
        elif click[0] == 1 and 420 < mouse[0] < 420 + 150 and 520 < mouse[1] < 520 + 50:
            pygame.mixer.Sound.play(button)
            pygame.quit()
            sys.exit()
        elif click[0] == 1 and 420 < mouse[0] < 420 + 150 and 580 < mouse[1] < 580 + 50:
            pygame.mixer.Sound.play(button)
            controls(playerimage)
        pygame.display.update()

def countdown_background(playerimage,cloudimage,bulletimage,cloudx,cloudy,bulletx,bullety,playerectx,playerrecty):
    win.blit(back.png)
    win.blit(playerimage,(playerectx,playerrecty))
    win.blit(cloudimage,(cloudx,cloudy))
    win.blit(bulletimage,(bulletx,bullety))
def gameintro(playerimage):
    while True:
        win.blit(game_intro, (0, 0))

        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        crash1()
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pos()
        message_display2('Score  50 to reach next level', 490, 400, white)
        message_display2('  Press s to Start', 300, 678, k)
        message_display2(
            '                          Press q to Quit', 520, 678, k)

        if 420 < mouse[0] < 420 + 150 and 460 < mouse[1] < 50 + 460:
            pygame.draw.rect(win, white, (420, 580, 150, 50),2)
            pygame.draw.rect(win, low_black, (420, 460, 150, 50))
            pygame.draw.rect(win, white, (420, 520, 150, 50),2)
            message_display2('Start', (420 + 420 + 150) /
                             2, (460 + 460 + 50) / 2, black)
            message_display2('Quit', (420 + 420 + 150) / 2,
                             (520 + 520 + 50) / 2, black)
            message_display2('Controls', (420 + 420 + 150) /
                             2, (580 + 580 + 50) / 2, black)
        elif 420 < mouse[0] < 420 + 150 and 520 < mouse[1] < 520 + 50:
            pygame.draw.rect(win, white, (420, 580, 150, 50),2)
            pygame.draw.rect(win, white, (420, 460, 150, 50),2)
            pygame.draw.rect(win, low_black, (420, 520, 150, 50))
            message_display2('Controls', (420 + 420 + 150) /
                             2, (580 + 580 + 50) / 2, black)
            message_display2('Quit', (420 + 420 + 150) / 2,
                             (520 + 520 + 50) / 2, black)
            message_display2('Start', (420 + 420 + 150) /
                             2, (460 + 460 + 50) / 2, black)
        elif 420 < mouse[0] < 420 + 150 and 580 < mouse[1] < 580 + 50:
            pygame.draw.rect(win, low_black, (420, 580, 150, 50))
            pygame.draw.rect(win, white, (420, 460, 150, 50),2)
            pygame.draw.rect(win, white, (420, 520, 150, 50),2)
            message_display2('Controls', (420 + 420 + 150) /
                             2, (580 + 580 + 50) / 2, black)
            message_display2('Start', (420 + 420 + 150) /
                             2, (460 + 460 + 50) / 2, black)
            message_display2('Quit', (420 + 420 + 150) / 2,
                             (520 + 520 + 50) / 2, black)
        else:
            pygame.draw.rect(win, white, (420, 580, 150, 50),2)
            pygame.draw.rect(win, white, (420, 460, 150, 50),2)
            pygame.draw.rect(win, white, (420, 520, 150, 50),2)
            message_display2('Controls', (420 + 420 + 150) /
                             2, (580 + 580 + 50) / 2, black)
            message_display2('Start', (420 + 420 + 150) /
                             2, (460 + 460 + 50) / 2, black)
            message_display2('Quit', (420 + 420 + 150) / 2,
                             (520 + 520 + 50) / 2, black)
        click = pygame.mouse.get_pressed()
        if click[0] == 1 and 420 < mouse[0] < 420 + 150 and 450 < mouse[1] < 50 + 450 or keys[pygame.K_s]:
            # pygame.mixer.Sound.play(button)
            countdown(playerimage)
        elif click[0] == 1 and 420 < mouse[0] < 420 + 150 and 520 < mouse[1] < 520 + 50 or keys[pygame.K_q]:
            pygame.mixer.Sound.play(button)
            pygame.quit()
            quit()
        elif click[0] == 1 and 420 < mouse[0] < 420 + 150 and 580 < mouse[1] < 580 + 50:
            pygame.mixer.Sound.play(button)
            controls(playerimage)
        pygame.display.update()


def won(playerimage):
    p = pygame.image.load('background.png')
    win.blit(p, (0, 0))
    pygame.mixer.music.pause()
    i = 1000
    while i > 100:
        message_display('You won Congrats', display_height /
                        2, display_width / 2, white)
        pygame.display.update()
        i = i - 1
    gameloop2(playerimage)


def iscollision(playerimage, bulletx, bullety, playerx, playery):
    collision = math.sqrt(math.pow((playerx - bulletx), 2) +
                          math.pow((playery - bullety), 2))
    return collision
testing = True
def untesting():
    global testing
    testing = False
def testing1():
    while testing:
        win.fill(white)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        message_display('3', display_height / 2, 300, black)
        clock.tick(1)
        untesting()
def countdown(playerimage):
    countdown = True
    while countdown:
        win.fill(white)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        time.sleep(0.1)
        testing1()
        untesting()
        pygame.display.update()
        clock.tick(1)
        win.fill(white)
        message_display('2', display_height / 2, 300, black)
        pygame.display.update()
        clock.tick(1)
        win.fill(white)
        message_display('1', display_height / 2, 300, black)
        pygame.display.update()
        clock.tick(1)
        win.fill(white)
        message_display('GO!!', display_height / 2, 300, black)
        clock.tick(1)
        pygame.display.update()
        gameloop(playerimage)
def gameloop2(playerimage):
    score = 0  # score
    player_speed = 4
    cloud_speed = 5
    player_bullet_speed = 5
    bullet_speed = 5
    global bullet_state  # initialising global num_bullet
    global pause
    bullet_state = 'ready'
    x = 0
    rect.x = 10
    rect.y = int(display_height / 2 - 200)
    square.x = rect.x
    square.y = rect.y
    bulletx = []
    bullety = []
    num_bullet = 9
    for i in range(num_bullet - 1):
        a = random.randint(1000, 1500)
        b = random.randint(0, 650)
        bulletx.append(a)
        bullety.append(b)
    pygame.mixer.music.play(-1)
    while True:
        win.fill(white)  # filling background with white
        scorelist = []
        win.blit(back, rect1)  # blitting images
        win.blit(back1, rect2)  # blitting images
        win.blit(playerimage, rect)  # blitting images
        list = []
        for i in range(num_bullet - 1):
            list.append(bulletlist[i].get_rect())
        for i in range(num_bullet - 1):
            win.blit(bulletlist[i], (bulletx[i], bullety[i]))
            bulletx[i] -= bullet_speed
            if bulletx[i] <= 0:
                # after the bullet moving out of the windows and then bltting it again at a diff pos
                bulletx[i] = random.randint(1000, 1500)
                bullety[i] = random.randint(0 + i, 700)
        # score for the game
        score += 1 / 100
        # getting all the events in pygame window
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                scorelist.append(score)
                pygame.quit()
                sys.exit()
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_SPACE:
                    if bullet_state is 'ready':
                        square.x = rect.x
                        square.y = rect.y
                        fire(player_bullet, square.x, square.y)
        # Bullet movement
        if bullet_state == 'fire':
            fire(player_bullet, square.x, square.y)
            square.x += player_bullet_speed
        if square.x > 1000:
            square.x = rect.x
            test1()
        keys = pygame.key.get_pressed()
        # player movement
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            rect.y += player_speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            rect.y -= player_speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            rect.x += player_speed

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            rect.x -= player_speed
        # pause function
        if keys[pygame.K_ESCAPE]:
            pause = True
            pygame.mixer.music.pause()
            escape(playerimage)
        if rect.x < 0:
            rect.x = 0
        if rect.y < 0:
            rect.y = 0
        if rect.y > display_width - player.get_rect().height:
            rect.y = display_width - player.get_rect().height

        # cloud movement
        for i in range(num - 1):  # displaying clouds
            win.blit(cloud1[i], (cloud_x[i], cloud_y[i]))
            cloud_x[i] -= cloud_speed
            if cloud_x[i] < 0 - cloud1[i].get_rect().width:
                cloud_x[i] = random.randint(1000, 1500)
        scoreimage(int(score))
        list23 = []
        for i in range(9 - 1):
            list23.append(bulletlist[i].get_rect())
        for i in range(9 - 1):  # collision
            testing = iscollision(
                playerimage, bulletx[i], bullety[i], rect.x, rect.y)
            if testing < 27:
                scorelist.append(str(int(score)))
                f2 = open('score.txt', 'r')
                line2 = f2.read()
                word2 = line2.split()
                h = open('highscore.bin', 'wb')
                pickle.dump(scorelist, h)
                h.close()
                for t in scorelist:
                    if len(word2) > 5:
                        f2 = open('score.txt', 'w')
                        f2.write(t)
                        f2.write('\n')

                    else:
                        f2 = open('score.txt', 'a')
                        f2.write(t)
                        f2.write('\n')
                    f2.close()
                pygame.mixer.music.pause()
                crash12(playerimage, int(score))
        # bullet collision with the player bullet
        for i in range(num_bullet - 1):
            if square.colliderect(list23[i]):
                test1()
                bulletx[i] = random.randint(1000, 1500)
                bullety[i] = random.randint(50, 700)
        if score > 50:  # creating a 2nd level
            won(playerimage)
        pygame.display.update()


def gameloop(playerimage):  # mainloop
    score = 0  # score
    player_speed = 4
    cloud_speed = 5
    player_bullet_speed = 5
    bullet_speed = 4
    global bullet_state  # initialising global num_bullet
    global pause
    bullet_state = 'ready'
    x = 0
    rect.x = 10
    rect.y = int(display_height / 2 - 200)
    square.x = rect.x
    square.y = rect.y
    bulletx = []
    bullety = []
    num_bullet = 9
    for i in range(num_bullet - 1):
        a = random.randint(1000, 1500)
        b = random.randint(0, 650)
        bulletx.append(a)
        bullety.append(b)
    pygame.mixer.music.play(-1)
    while True:
        win.fill(white)  # filling background with white
        scorelist = []
        win.blit(back, rect1)  # blitting images
        win.blit(back1, rect2)  # blitting images
        win.blit(playerimage, rect)  # blitting images
        list = []
        for i in range(num_bullet - 1):
            list.append(bulletlist[i].get_rect())
        for i in range(num_bullet - 1):
            win.blit(bulletlist[i], (bulletx[i], bullety[i]))
            bulletx[i] -= bullet_speed
            if bulletx[i] <= 0:
                # after the bullet moving out of the windows and then bltting it again at a diff pos
                bulletx[i] = random.randint(1000, 1500)
                bullety[i] = random.randint(0 + i, 700)
        # score for the game
        score += 1 / 100
        # getting all the events in pygame window
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                scorelist.append(score)
                pygame.quit()
                sys.exit()
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_SPACE:
                    if bullet_state == 'ready':
                        square.x = rect.x
                        square.y = rect.y
                        fire(player_bullet, square.x, square.y)
        # Bullet movement
        if bullet_state == 'fire':
            fire(player_bullet, square.x, square.y)
            square.x += player_bullet_speed
        if square.x > 1000:
            square.x = rect.x
            test1()
        keys = pygame.key.get_pressed()
        # player movement
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            rect.y += player_speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            rect.y -= player_speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            rect.x += player_speed

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            rect.x -= player_speed
        # pause function
        if keys[pygame.K_ESCAPE]:
            pause = True
            pygame.mixer.music.pause()
            escape(playerimage)
        if rect.x < 0:
            rect.x = 0
        if rect.y < 0:
            rect.y = 0
        if rect.y > display_width - player.get_rect().height:
            rect.y = display_width - player.get_rect().height

        # cloud movement
        for i in range(num - 1):  # displaying clouds
            win.blit(cloud1[i], (cloud_x[i], cloud_y[i]))
            cloud_x[i] -= cloud_speed
            if cloud_x[i] < 0 - cloud1[i].get_rect().width:
                cloud_x[i] = random.randint(1000, 1500)
        scoreimage(int(score))
        list23 = []
        for i in range(9 - 1):
            list23.append(bulletlist[i].get_rect())
        for i in range(9 - 1):  # collision
            testing = iscollision(
                playerimage, bulletx[i], bullety[i], rect.x, rect.y)
            if testing < 27:
                scorelist.append(str(int(score)))
                f2 = open('score.txt', 'r')
                line2 = f2.read()
                word2 = line2.split()
                h = open('highscore.bin', 'wb')
                pickle.dump(scorelist, h)
                h.close()
                for t in scorelist:
                    if len(word2) > 5:
                        f2 = open('score.txt', 'w')
                        f2.write(t)
                        f2.write('\n')

                    else:
                        f2 = open('score.txt', 'a')
                        f2.write(t)
                        f2.write('\n')
                    f2.close()
                pygame.mixer.music.pause()
                crash12(playerimage, int(score))
        # bullet collision with the player bullet
        for i in range(num_bullet - 1):
            if square.colliderect(list23[i]):
                test1()
                bulletx[i] = random.randint(1000, 1500)
                bullety[i] = random.randint(50, 700)
        if score > 50:  # creating a 2nd level
            won(playerimage)
        pygame.display.update()


clock.tick(200)  # setting the fps
playerinput(player)  # called the function playerinput the enter the name
