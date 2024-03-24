
This is my attempt to learn how to create a 2-D video game. I will be using Python as the programming language. Pygame was recommended when creating my first game. I will attempt to build Space Invaders. 

Game Process - 
   1. Checking the player input (the event loop)           
   2. Use that information to place elements in the screen            
        - Result = Creates an image                         
   3. Repeat 1 and 2 

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
   1. "enemy1" By smalllikeart - https://www.flaticon.com/free-icon/alien_3823672?related_id=3823672
   2. "enemy2" By Atif Arshad - https://www.flaticon.com/free-icon/art_13534823?term=space+invader+enemy&page=1&position=1&origin=search&related_id=13534823
   3. "enemy3" By smalllikeart - https://www.flaticon.com/free-icon/alien_3823688?term=space+invader+enemy&page=1&position=36&origin=search&related_id=3823688
   4. "shooter" By Smashicons - https://www.flaticon.com/free-icon/space-invaders_705975?term=space+invader+enemy&page=1&position=11&origin=search&related_id=705975
   5. "dead_shooter" By Aldo Cervantes - https://www.flaticon.com/free-icon/explosion_2147238?term=explosions&related_id=2147238
   6. "background" by kues1 - https://www.freepik.com/free-photo/abstract-geometric-background-shapes-texture_20386173.htm#query=space%20invaders%20background&position=20&from_view=keyword&track=ais&uuid=9d2cf759-8df2-4a09-963d-8bd92ba1bfc2
   7. "bullet" - by Smashicons - https://www.flaticon.com/free-icon/paintball_3547800?term=bullet&page=1&position=82&origin=search&related_id=3547800 

Font - 
   1. "space_invader_font" - https://www.dafontfree.co/space-invaders-font/
