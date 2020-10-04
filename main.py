import pygame
pygame.init()
win = pygame.display.set_mode((800,600))
class testing(pygame.sprite.Sprite):
    def __init__(self,width,height,pos_x,pos_y,color):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x,pos_y]
pos_x = 100
pos_y = 100
test = testing(100,100,pos_x,pos_y,(255,255,255))
test_group = pygame.sprite.Group()
test_group.add(test)
while True:

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    win.fill((0,0,0))
    pygame.display.flip()
    
        
