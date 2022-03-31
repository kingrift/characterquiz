import pygame
import pygame_textinput
import os

## INITIALIZATION

pygame.init()

screen = pygame.display.set_mode([800, 600])


## COLORS
black = (0, 0, 0)
pink = (255, 105, 180)


## VARIABLES
nameInput = pygame_textinput.TextInputVisualizer(cursor_width=0, font_color=pink)
imagedir = 'Assets/Images/'
audiodir = 'Assets/Audio/'

images = os.listdir(imagedir)
print(images)

## GAME LOOP

running = True
while running:
    index = 0

    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            running = False

    screen.fill(black)


    characterImg = pygame.image.load(imagedir + images[index])


    nameInput.update(events)
    screen.blit(nameInput.surface, (400, 50))



    screen.blit(characterImg, (50, 50))
    pygame.display.update()

pygame.quit()