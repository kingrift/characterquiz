import pygame
import pygame_textinput
import os
import random

## INITIALIZATION
screen_size = [800, 600]

pygame.init()

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Rift's Character Quiz")
pygame.display.set_icon(pygame.image.load('Assets/Images/icon.png'))

font = pygame.font.SysFont(None, 40)


## COLORS
black = (0, 0, 0)
pink = (255, 105, 180)


## VARIABLES
points = 0
index = 0
musicIndex = 0

nameInput = pygame_textinput.TextInputVisualizer(cursor_width=0, font_color=pink)
imagedir = 'Assets/Images/Characters/'
audiodir = 'Assets/Audio/'

images = os.listdir(imagedir)
random.shuffle(images)

music = os.listdir(audiodir)
random.shuffle(music)

## Functions

def checkAnswer(characterFile, nameInput):
    correct = characterFile.split('.')
    correct1 = correct[0]
    correct2 = correct[0].split('_')
    if len(correct2) == 2:
        correct2 = correct2[1] + ' ' + correct2[0]
    else:
        correct2 = False
    correct1 = correct1.replace('_', ' ')

    if correct1.lower() == nameInput.lower():
        return True
    elif correct2 != False:
        if correct2 == nameInput.lower():
            return True
        else:
            return False
    else:
        return False

def playMusic(index):
    pygame.mixer.music.load(audiodir + music[index])
    pygame.mixer.music.play()
    pygame.mixer.music.set_endevent(pygame.USEREVENT)
    return index + 1

## GAME LOOP

musicIndex = playMusic(musicIndex)

running = True
while running:
    screen.fill(black)
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.USEREVENT:
            if musicIndex >= len(music):
                musicIndex = 0
            pygame.mixer.music.unload()
            musicIndex = playMusic(musicIndex)

    if index < len(images):
        characterImg = pygame.image.load(imagedir + images[index])

        pointsText = font.render('Score: ' + str(points), True, pink)
        screen.blit(pointsText, (300, 50))

        nameText = font.render('Name: ', True, pink)
        screen.blit(nameText, (300, 100))

        nameInput.update(events)
        screen.blit(nameInput.surface, (400, 100))
        screen.blit(characterImg, (50, 50))

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    a = checkAnswer(images[index], nameInput.value)
                    if a == True:
                        points += 1
                    index += 1
                    nameInput.value = ''
    else:
        percentile = points / len(images)
        title = ''
        if percentile == 1:
            title = 'Supreme Weeb'
        elif percentile >= 0.9:
            title = 'Master Weeb'
        elif percentile >= 0.75:
            title = 'Average Weeb'
        elif percentile >= 0.5:
            title = 'Rookie Weeb'
        else:
            title = 'Non-Weeb'
        
        screen.fill(black)

        titleText = pygame.font.SysFont(None, 80).render(title, True, pink)
        screen.blit(titleText, titleText.get_rect(center=(screen_size[0]*0.5, screen_size[1]*0.15)))

        scoreText = font.render("You got {} out of {} points!".format(points, len(images)), True, pink)
        screen.blit(scoreText, scoreText.get_rect(center=(screen_size[0]*0.5, screen_size[1]*0.45)))

        retryText = pygame.font.SysFont(None, 50).render('Retry!', True, pink)
        screen.blit(retryText, retryText.get_rect(center=(screen_size[0]*0.5, screen_size[1]*0.75)))

        quitText = pygame.font.SysFont(None, 50).render('Quit game!', True, pink)
        screen.blit(quitText, quitText.get_rect(center=(screen_size[0]*0.5, screen_size[1]*0.85)))

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if screen_size[0]*0.5-100 <= mouse[0] <= screen_size[0]*0.5+100:
                    if screen_size[1]*0.75-15 <= mouse[1] <= screen_size[1]*0.75+15:
                        index = 0
                        points = 0
                        title = ''
                        random.shuffle(images)
                    elif screen_size[1]*0.85-15 <= mouse[1] <= screen_size[1]*0.85+15:
                        running = False


    pygame.display.update()

pygame.quit()