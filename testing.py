import pygame
pygame.init()
win = pygame.display.set_mode((800, 600))
green = (0, 255, 0)
table = pygame.image.load('Capture.PNG')
103, 324
f = open('names.txt', 'r')
line = f.read()
word = line.split()
font = pygame.font.Font(None, 32)
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            quit()
    win.fill(green)
    win.blit(table, (100, 300))
    x = [104, 104, 104, 104, 104]
    y = [319, 338, 357, 357+19, 357+19+19]
    list = []
    for i in word:
        list.append(font.render(i, True, (0, 0, 0)))
    for i in range(6-1):
        win.blit(list[i], (x[i],y[i]))

    mouse = pygame.mouse.get_pos()
    print(mouse)
    pygame.display.update()
