import pygame
import sys



BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN=(0,255,0)


segment_width = 15
segment_height = 15

segment_margin = 3

x_change = segment_width + segment_margin
y_change = 0


class Segment(pygame.sprite.Sprite):
    """ Class to represent one segment of the snake. """
    def __init__(self, x, y):
        
        

        
        self.image = pygame.Surface([segment_width, segment_height])
        self.image.fill(GREEN)

        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


pygame.init()


screen = pygame.display.set_mode([800, 600])


pygame.display.set_caption('Hungry Snake')

allspriteslist = pygame.sprite.Group()


snake_segments = []
for i in range(15):
    x = 250 - (segment_width + segment_margin) * i
    y = 30
    segment = Segment(x, y)
    snake_segments.append(segment)
    allspriteslist.add(segment)


clock = pygame.time.Clock()
done = False

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = (segment_width + segment_margin) * -1
                y_change = 0
            if event.key == pygame.K_RIGHT:
                x_change = (segment_width + segment_margin)
                y_change = 0
            if event.key == pygame.K_UP:
                x_change = 0
                y_change = (segment_height + segment_margin) * -1
            if event.key == pygame.K_DOWN:
                x_change = 0
                y_change = (segment_height + segment_margin)

    
    old_segment = snake_segments.pop()
    allspriteslist.remove(old_segment)

    
    x = snake_segments[0].rect.x + x_change
    y = snake_segments[0].rect.y + y_change
    segment = Segment(x, y)

    
    snake_segments.insert(0, segment)
    allspriteslist.add(segment)

    
    # Clear screen
    screen.fill(BLACK)

    allspriteslist.draw(screen)

    # Flip screen
    pygame.display.flip()

    # Pause
    clock.tick(5)

pygame.quit()
