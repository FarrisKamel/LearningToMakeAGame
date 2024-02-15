
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
   Using surfaces:
       - Display Surface (The game window)
           * Can only be one
       - Regular Surface (Essential an image)
           * Needs to be put in the display surface 
           * Can be many 

