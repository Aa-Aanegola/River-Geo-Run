import pygame


"""
    The pygame related variables; screen size, clock and FPS
    Sets up the game for gameplay
    Also has the Collided for collision detection
"""
pygame.init()
width, height = 1500, 840
screen = pygame.display.set_mode((width, height))
fpsclock = pygame.time.Clock()
FPS = 120
Collided = False

"""
    Color presets for all colors used in the game in (R,G,B) format
"""
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
LBLUE = (0, 156, 200)
BROWN = (128, 96, 70)
GREEN = (0, 255, 0)

font = pygame.font.Font('freesansbold.ttf', 32)


starttext = font.render('START', True, WHITE)
starttextRect = starttext.get_rect()
endtext = font.render('END', True, WHITE)
endtextRect = endtext.get_rect()
gotextl = font.render('You collided :(', True, WHITE)
gotextRectl = gotextl.get_rect()
gotextRectl.center = (width / 2, height / 2)
gotextw = font.render('Good job!!', True, WHITE)
gotextRectw = gotextw.get_rect()
gotextRectw.center = (width / 2, height / 2)

roundtext1 = font.render('Player 1 wins round!', True, WHITE)
roundtextRect1 = roundtext1.get_rect()
roundtextRect1.center = (width / 2, height / 2)
roundtext2 = font.render('Player 2 wins round!', True, WHITE)
roundtextRect2 = roundtext2.get_rect()
roundtextRect2.center = (width / 2, height / 2)