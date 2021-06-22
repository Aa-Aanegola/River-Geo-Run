from config import *


class Player(pygame.sprite.Sprite):
    """
        The player class contains the player's image, size,
        number of rounds won, current round time and score.
        also holds the speed of the dynamic obstacles
    """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('player.png').convert_alpha(screen)
        self.rect = self.image.get_rect()
        self.size = self.image.get_size()
        self.image = pygame.transform.scale(
            self.image, (int(self.size[0] / 6), int(self.size[1] / 6)))
        self.time = 0
        self.score = 0
        self.speed = 50
        self.victory = False
        self.rounds = 0

    def control(self, x, y):
        """
            function to move the player
            :param x: number of pixels to move in the +x direction
            :param y: number of pixels to move in the +y direction
            Also defines bounding box, and ensures that the sprite
            doesn't exit the screen
        """

        if self.rect.x <= 0:
            if x < 0:
                self.rect.x = 0
            else:
                self.rect.x += x
        elif self.rect.x >= 1464:
            if x > 0:
                self.rect.x = 1464
            else:
                self.rect.x += x
        else:
            self.rect.x += x

        if self.rect.y <= 0:
            if y < 0:
                self.rect.y = 0
            else:
                self.rect.y += y
        elif self.rect.y >= 804:
            if y > 0:
                self.rect.y = 804
            else:
                self.rect.y += y
        else:
            self.rect.y += y
