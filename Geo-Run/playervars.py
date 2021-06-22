from Player import *

"""
    This file creates and holds all the variables related to the players.
    Defines their initial positions, and holds the step size for them.
    Also defines certain variables for movement:
    key_x defines whether the 'x' key is pressed or not
"""
player1 = Player()
player1.rect.x = 740
player1.rect.y = 800
player_list = pygame.sprite.Group()
player_list.add(player1)
player2 = Player()
player2.rect.x = 740
player2.rect.y = 800
steps = 1.6
pressed_left = False
pressed_right = False
pressed_up = False
pressed_down = False
player_finish = False
player = player1

"""
    Defines the variables for keeping score, like score and timer.
    Also initializes the font with which the score is displayed
"""
score = 0
timer = 0
rec = 10000
font = pygame.font.Font('freesansbold.ttf', 32)
master_score = 'Score: ' + str(score)
text = font.render(master_score, True, GREEN, BROWN)
textRect = text.get_rect()
textRect.center = (100, 22)
round_completed = False
