from Enemies import *

# Spawning static obstacles
stat = pygame.sprite.Group()


def create_enemies_static():
    """
        The function that is called in the very beginning of the game,
        to initialize the positions of the static enemies.
        Hard coded positions to ensure consistent difficulty
    """
    stat.add(EnemyStatic(100, 140))
    stat.add(EnemyStatic(320, 140))
    stat.add(EnemyStatic(550, 140))
    stat.add(EnemyStatic(780, 140))
    stat.add(EnemyStatic(1000, 140))
    stat.add(EnemyStatic(1400, 140))

    stat.add(EnemyStatic(150, 300))
    stat.add(EnemyStatic(400, 300))
    stat.add(EnemyStatic(650, 300))
    stat.add(EnemyStatic(800, 300))
    stat.add(EnemyStatic(1100, 300))
    stat.add(EnemyStatic(1300, 300))

    stat.add(EnemyStatic(10, 460))
    stat.add(EnemyStatic(230, 460))
    stat.add(EnemyStatic(440, 460))
    stat.add(EnemyStatic(632, 460))
    stat.add(EnemyStatic(876, 460))
    stat.add(EnemyStatic(1333, 460))

    stat.add(EnemyStatic(300, 620))
    stat.add(EnemyStatic(900, 620))
    stat.add(EnemyStatic(1050, 620))
    stat.add(EnemyStatic(1200, 620))
    stat.add(EnemyStatic(1400, 620))
    stat.add(EnemyStatic(300, 620))
    stat.add(EnemyStatic(300, 620))


# Calling function to add enemies to screen
create_enemies_static()

# Spawning moving obstacles
dynam = pygame.sprite.Group()


def create_enemies_dynamic():
    """
        The function that is called in the very beginning of the game,
        to initialize the positions of the dynamic enemies.
        Hard coded positions to ensure proper movement,
        and good spacing.
    """
    dynam.add(EnemyDynamic(100, 725))
    dynam.add(EnemyDynamic(400, 725))
    dynam.add(EnemyDynamic(700, 725))
    dynam.add(EnemyDynamic(1000, 725))
    dynam.add(EnemyDynamic(1300, 725))

    dynam.add(EnemyDynamic(100, 565))
    dynam.add(EnemyDynamic(400, 565))
    dynam.add(EnemyDynamic(700, 565))
    dynam.add(EnemyDynamic(1000, 565))
    dynam.add(EnemyDynamic(1300, 565))

    dynam.add(EnemyDynamic(100, 405))
    dynam.add(EnemyDynamic(400, 405))
    dynam.add(EnemyDynamic(700, 405))
    dynam.add(EnemyDynamic(1000, 405))
    dynam.add(EnemyDynamic(1300, 405))

    dynam.add(EnemyDynamic(100, 245))
    dynam.add(EnemyDynamic(400, 245))
    dynam.add(EnemyDynamic(700, 245))
    dynam.add(EnemyDynamic(1000, 245))
    dynam.add(EnemyDynamic(1300, 245))

    dynam.add(EnemyDynamic(100, 85))
    dynam.add(EnemyDynamic(400, 85))
    dynam.add(EnemyDynamic(700, 85))
    dynam.add(EnemyDynamic(1000, 85))
    dynam.add(EnemyDynamic(1300, 85))


# Calling function to draw the dynamic enemies
create_enemies_dynamic()
