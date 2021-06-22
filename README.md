# River Geo-Run
A game that mimics the age old river crossing game with hand created sprites and very primitive game design. This was created in February of 2020 and hence lacks proper structure. Dodge and weave strange geometric alien shapes with a smirk on your face, find movement patterns and make your way to the opposing river bank. Compete with a friend to reach opposing sides of the rivers to gain points and even rounds!
### How to play
To start up Geo-Run simply run the command ```python3 main.py``` which should start up a playable pygame window. To move around in the world, player 1 can use the arrow keys, and player 2 can use the w, a, s and d keys. 
### Code base
The code is divided based on its purpose. Each individual file contains detailed explanations on each function and a brief overview is provided below. 
- ```Main.py``` contains functions to help with per-tick updates like collision detection, score updation and player swaps. It also has the main loop that runs the game endlessly.
- ```Player.py``` contains the player class which has sprite, score, round score and other information along with functions to help move the sprite. The game requires 2 players and ```playervars.py``` contains all the player related variables required. 
- ```Enemies.py``` contains the classes for dynamic and static obstacles. These simply contain the bounding boxes, sprites and some other enemy related information. In order to spawn these enemis there are helper functions in ```enemycreate.py``` with hardcoded **:(** positions for the enemies. To ensure that the game doesn't become too easy the dynamic obstacles get faster over time. 
- ```config.py``` sets up pygame and also declares some variables for color, text and more pygame related trivialities. 
The sprites and backing track are also present in the same directory (I didn't clean this up since I wanted to preserve the authencity of this project) and are labelled to make them easy to find. 
