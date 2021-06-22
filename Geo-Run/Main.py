"""
    Importing all the required modules, defined in the folder and external.
    sys and pygame for pygame usage
    time for pausing between player transitions
    random for the slow randomization of the dynamic enemies
"""
import sys
import time
from playervars import *
from enemycreate import *
from pygame.locals import *
import random


def toggle_player():
    """
        uses all the defined global variables to set the player's variables
        and then switches player to the other player
        also resets the score display, and Collided.
    """
    global player
    global score
    global timer
    global rec
    global Collided
    global font

    if player == player1:
        player = player2
    else:
        player = player1

    score = 0
    timer = 0
    rec = 10000
    master_score = 'Score: ' + str(score)
    text = font.render(master_score, True, GREEN, BROWN)
    textRect = text.get_rect()
    textRect.center = (100, 22)
    Collided = False


def round_completed_func():
    """
        Called after player2 plays. Compares the scores/ times of player1
        and player2, and displays the winner. Also changes the speed of
        the winner and updates the rounds variable in the player who won.
    """
    global round_completed
    global roundtext1
    global roundtext2
    global roundtextRect1
    global roundtextRect2

    round_completed = False

    if player1.score > player2.score:
        screen.blit(roundtext1, roundtextRect1)
        pygame.display.flip()
        if player1.speed > 10:
            player1.speed -= 10
        time.sleep(3)
        player1.rounds += 1
    elif player2.score > player1.score:
        screen.blit(roundtext2, roundtextRect2)
        pygame.display.flip()
        if player2.speed > 10:
            player2.speed -= 10
        time.sleep(3)
        player2.rounds += 1
    elif player1.time < player2.time:
        screen.blit(roundtext1, roundtextRect1)
        pygame.display.flip()
        if player1.speed > 10:
            player1.speed -= 10
        time.sleep(3)
        player1.rounds += 1
    else:
        screen.blit(roundtext2, roundtextRect2)
        pygame.display.flip()
        if player2.speed > 10:
            player2.speed -= 10
        time.sleep(3)
        player2.rounds += 1


def collision():
    """
        Defines what happens when a collision takes place.
        Displays a losing message, resets score and timer
        and calls toggle_player().
        Also determines whether the round has ended or not
    """
    global Collided
    global score
    global timer
    global round_completed
    global rec
    global player_finish
    global height
    global width
    global player_list
    global player
    global gotextl
    global gotextRectl

    Collided = False
    screen.blit(gotextl, gotextRectl)
    pygame.display.flip()
    time.sleep(3)
    player_list.remove(player)

    player.time = timer
    player.score = score
    score = 0
    timer = 0
    if player == player2:
        round_completed = True

    toggle_player()
    if player == player1:
        player.rect.x = 740
        player.rect.y = 800
        rec = 1000
    else:
        player.rect.x = 740
        player.rect.y = 0
        rec = 0

    player_list.add(player)


def victory_func():
    """
        Called when a player reaches the end. Displays a victory message,
        resets the score and timer variables and resets the player's position
        Also resets all the round variables like Collided
    """
    global Collided
    global score
    global timer
    global round_completed
    global rec
    global player_finish
    global height
    global width
    global player_list
    global player
    global gotextw
    global gotextRectw

    if player_finish:
        screen.blit(gotextw, gotextRectw)
        pygame.display.flip()
        time.sleep(3)
        player_list.remove(player)

        player.time = timer
        player.score = score
        score = 0
        timer = 0
        player.victory = True

        if player == player2:
            round_completed = True

        toggle_player()
        if player == player1:
            player.rect.x = 740
            player.rect.y = 800
            rec = 1000
        else:
            player.rect.x = 740
            player.rect.y = 0
            rec = 0

    player_list.add(player)
    player_finish = False
    Collided = False


def draw():
    """
        Called every time the screen refreshes. Draws the rivers and land
        Displays the score, round score and player icons
        Draws the obstacles and updates the moving obstacles
    """
    global score
    global width
    global height
    global starttext
    global endtext
    global starttextRect
    global endtextRect

    master_score = 'Score: ' + str(score)
    text = font.render(master_score, True, GREEN, BROWN)

    round_score = 'Round Score: ' + \
        str(player1.rounds) + '-' + str(player2.rounds)
    round = font.render(round_score, True, GREEN, BROWN)
    roundRect = round.get_rect()
    roundRect.center = (1300, 20)

    for x in range(0, 5):
        pygame.draw.rect(screen, BROWN, (0, x * 160, 1500, 40))
        pygame.draw.rect(screen, LBLUE, (0, 40 + x * 160, 1500, 120))
    pygame.draw.rect(screen, BROWN, (0, 800, 1500, 40))

    if player == player1:
        starttextRect.center = (width / 2, height - 17)
        endtextRect.center = (width / 2, 17)
        screen.blit(starttext, starttextRect)
        screen.blit(endtext, endtextRect)
    else:
        starttextRect.center = (width / 2, 17)
        endtextRect.center = (width / 2, height - 17)
        screen.blit(starttext, starttextRect)
        screen.blit(endtext, endtextRect)

    screen.blit(text, textRect)
    screen.blit(round, roundRect)
    player_list.draw(screen)
    stat.draw(screen)
    dynam.draw(screen)


def player_move():
    """
        Function that reads the keys_pressed() from pygame and passes the
        correct arguments to player.control() to move the sprite
        Right and Down controls are multiplied because pygame has
        lower movement speeds for these directions
    """
    global player
    keys = pygame.key.get_pressed()
    if player == player1:
        if keys[pygame.K_LEFT]:
            player.control(-steps, 0)
        if keys[pygame.K_RIGHT]:
            player.control(steps * 1.6, 0)
        if keys[pygame.K_UP]:
            player.control(0, -steps)
        if keys[pygame.K_DOWN]:
            player.control(0, steps * 1.6)
    else:
        if keys[pygame.K_a]:
            player.control(-steps, 0)
        if keys[pygame.K_d]:
            player.control(steps * 1.6, 0)
        if keys[pygame.K_w]:
            player.control(0, -steps)
        if keys[pygame.K_s]:
            player.control(0, steps * 1.6)


def score_collide():
    """
        Function that takes care of collision detection and score updates
        Also moves the dynamic enemies based on the player speed
        THe hitboxes for the enemies are the same size and hence are
        hardcoded. The dynamic update is inside the static update to
        ensure smooth and relatively fast movement of the enemies
        Score updates whenever the player crosses a dynamic or static layer
        and is also hardcoded. Here rec holds a value that will ensure that
        the score isn't updated every time the screen refreshes.
        Also slightly randomizes the positions of the dynamic obstacles
        over time to increase difficulty.
        Respawns new dynamic enemies when old ones move out of the frame
    """
    global stat
    global dynam
    global Collided
    global player
    global timer
    global player_finish
    global score
    global rec
    for i in stat:
        if i.rect.x <= player.rect.x < i.rect.x + 82:
            if i.rect.y <= player.rect.y < i.rect.y + 82:
                Collided = True

        corner_x = player.rect.x + 34
        corner_y = player.rect.y + 32

        if i.rect.x <= corner_x < i.rect.x + 82:
            if i.rect.y <= corner_y < i.rect.y + 82:
                Collided = True

        corner_x = player.rect.x
        corner_y = player.rect.y + 32

        if i.rect.x <= corner_x < i.rect.x + 82:
            if i.rect.y <= corner_y < i.rect.y + 82:
                Collided = True

        corner_x = player.rect.x + 34
        corner_y = player.rect.y

        if i.rect.x <= corner_x < i.rect.x + 82:
            if i.rect.y <= corner_y < i.rect.y + 82:
                Collided = True

        timer += 1

        if player == player1 and player.rect.y == 0:
            player_finish = True
        elif player == player2 and player.rect.y == 802:
            player_finish = True

        if player == player1:
            if player.rect.y <= 20 < rec:
                score += 10
                rec = 20
            elif player.rect.y <= 140 < rec:
                score += 5
                rec = 140
            elif player.rect.y <= 180 < rec:
                score += 10
                rec = 180
            elif player.rect.y <= 300 < rec:
                score += 5
                rec = 300
            elif player.rect.y <= 340 < rec:
                score += 10
                rec = 340
            elif player.rect.y <= 460 < rec:
                score += 5
                rec = 460
            elif player.rect.y <= 500 < rec:
                score += 10
                rec = 500
            elif player.rect.y <= 620 < rec:
                score += 5
                rec = 620
            elif player.rect.y <= 660 < rec:
                score += 10
                rec = 660
            elif player.rect.y <= 780 < rec:
                score += 5
                rec = 780
        else:
            if player.rect.y >= 20 > rec:
                score += 5
                rec = 20
            elif player.rect.y >= 140 > rec:
                score += 10
                rec = 140
            elif player.rect.y >= 180 > rec:
                score += 5
                rec = 180
            elif player.rect.y >= 300 > rec:
                score += 10
                rec = 300
            elif player.rect.y >= 340 > rec:
                score += 5
                rec = 340
            elif player.rect.y >= 460 > rec:
                score += 10
                rec = 460
            elif player.rect.y >= 500 > rec:
                score += 5
                rec = 500
            elif player.rect.y >= 620 > rec:
                score += 10
                rec = 620
            elif player.rect.y >= 660 > rec:
                score += 5
                rec = 660
            elif player.rect.y >= 780 > rec:
                score += 10
                rec = 780

        for i in dynam:
            corner_x = player.rect.x
            corner_y = player.rect.y
            if i.rect.x <= corner_x < i.rect.x + 80:
                if i.rect.y <= corner_y < i.rect.y + 50:
                    Collided = True
            corner_x = player.rect.x + 34
            corner_y = player.rect.y
            if i.rect.x <= corner_x < i.rect.x + 80:
                if i.rect.y <= corner_y < i.rect.y + 50:
                    Collided = True
            corner_x = player.rect.x
            corner_y = player.rect.y + 32
            if i.rect.x <= corner_x < i.rect.x + 80:
                if i.rect.y <= corner_y < i.rect.y + 50:
                    Collided = True
            corner_x = player.rect.x + 34
            corner_y = player.rect.y + 32
            if i.rect.x <= corner_x < i.rect.x + 80:
                if i.rect.y <= corner_y < i.rect.y + 50:
                    Collided = True

            if not timer % player.speed:
                i.rect.x += 1

            if i.rect.x >= 1500:
                dynam.add(EnemyDynamic(random.randint(-150, -100), i.rect.y))
                dynam.remove(i)


"""
    Loads the background music and plays it in an infinite
    loop.
"""
pygame.mixer.music.load('back.mp3')
pygame.mixer.music.play(-1)


while True:
    """
        Main game loop, calls the functions:
                            round_completed_func()
                            Collision()
                            victory_func()
                            draw()
                            player_move()
                            and score_collided()
        every time the screen is refreshed.
        Also refreshes the screen and updates the FPS clock.
        Sets the exit command to be on the button press of the X.
    """
    if round_completed:
        round_completed_func()

    # Check if collision has happened
    if Collided:
        collision()

    # Function to check for victory
    victory_func()

    # Function to update the screen
    draw()

    # In game events
    for event in pygame.event.get():

        # Exit Command (The X button is pressed)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Update movement of player, and work for holding keys
    player_move()

    # Check if collision has taken place
    # Update score
    score_collide()

    # To display the update every frame
    pygame.display.flip()
    fpsclock.tick(FPS)
