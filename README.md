
This is my attempt to learn how to create a 2-D video game. I will be using Python as the programming language. Pygame was recommended when creating my first game. I will attempt to build Space Invaders. 

Game Process - 
   1. Checking the player input (the event loop)              <-------|
   2. Use that information to place elements in the screen            |
        - Result = Creates an image                          >--------|

Pygame - 
   1. Helps draws images. 
   2. Check for player input 
       (input() stops the game, therefore useless of game)
   3. Made only for simply game. (Typically 2-D games).

Deciding Frame rate of the game -
   1. Strong PC can handle high frame rate
   Ideally - 
       - Should use constant framerate
       - We will use 60 fps for this 
           * 60 fps ceiling
           * 60 fps floor 

Displaying Images -
   1. Using surfaces:
       - Display Surface (The game window)
           * Can only be one
       - Regular Surface (Essential an image)
           * Needs to be put in the display surface 
           * Can be many 


Images -
   1. "enemy1" By Icon Mark - https://www.flaticon.com/free-icon/play_13862255?term=space+invader&page=1&position=14&origin=search&related_id=13862255
   2. "enemy2" By Andrew Dynamite - https://www.flaticon.com/free-icon/retro_12942473?term=space+invader&page=1&position=2&origin=search&related_id=12942473
   3. "enemy3" By Mayor Icons - https://www.flaticon.com/free-icon/alien_4188923?term=space+invader&page=1&position=23&origin=search&related_id=4188923
   4. "shooter" By Smashicons - https://www.flaticon.com/free-icon/space-invaders_705791?term=space+invader&page=1&position=21&origin=search&related_id=705791
   5. "background" by kues1 - https://www.freepik.com/free-photo/abstract-geometric-background-shapes-texture_20386173.htm#query=space%20invaders%20background&position=20&from_view=keyword&track=ais&uuid=9d2cf759-8df2-4a09-963d-8bd92ba1bfc2

Font - 
   1. "space_invader_font" - https://www.dafontfree.co/space-invaders-font/