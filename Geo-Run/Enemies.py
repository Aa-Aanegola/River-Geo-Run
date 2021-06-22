from config import *


# Definition for the static enemies class
class EnemyStatic(pygame.sprite.Sprite):
    """
        The class exists to help group all the required information about the
        static enemies. Contains the image and positions of the objects.
    """

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(
            'Obstacle_Static.png').convert_alpha(screen)
        self.rect = self.image.get_rect()
        self.size = self.image.get_size()
        self.image = pygame.transform.scale(
            self.image, (int(self.size[0] / 6), int(self.size[1] / 6)))
        self.rect.x = x
        self.rect.y = y


# Definition for the dynamic enemies class
class EnemyDynamic(pygame.sprite.Sprite):
    """
        The class exists to group the required information about the
        dynamic enemies. Contains the image and the positions of the objects.
    """

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(
            'Obstacle_Dynamic.png').convert_alpha(screen)
        self.rect = self.image.get_rect()
        self.size = self.image.get_size()
        self.image = pygame.transform.scale(
            self.image, (int(self.size[0] / 3), int(self.size[1] / 3)))
        self.rect.x = x
        self.rect.y = y
