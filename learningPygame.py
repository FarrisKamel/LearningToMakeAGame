# The code below was written by Farris Alqalam
# This is my first attempt to building a game. 
# After research, it was recommend to use Pygame.

# Game Process - 
#   1. Checking the player input (the event loop)         <-------|
#   2. Use that information to place elements in the screen       |
#   Result = Creates an image                            >--------|

# Pygame - 
#   1. Helps draws images. 
#   2. Check for player input 
#       (input() stops the game, therefore useless of game)
#   3. Made only for simply game. (Typically 2-D games).

# Deciding Frame rate of the game -
#   1. Strong PC can handle high frame rate
#   Ideally - 
#       - Should use constant framerate
#       - We will use 60 fps for this 
#           * 60 fps ceiling
#           * 60 fps floor 

# Displaying Images -
#   Using surfaces:
#       - Display Surface (The game window)
#           * Can only be one
#       - Regular Surface (Essential an image)
#           * Needs to be put in the display surface 
#           * Can be many 

##############################################

# Creating a windown in Pygame
import pygame
from sys import exit

#Initiate pygame
pygame.init()
#Create the display screen that the game will appear in 
screen = pygame.display.set_mode((800,400))
# Set a caption to the window of the game
pygame.display.set_caption("Learning Pygame")
# Create a clock object to help us keep track of fps
clock = pygame.time.Clock() 

#Creating a Surface 
first_surface = pygame.Surface((100,100))
first_surface.fill("Green")

#Create a infinite loop using a while true loop
while True:
    
    # This is where all the drawing and elements of the game should be 

    # Create a loop (essentially a for loop)
    # To look for all the possibel events that may happen
    # Use the pygame.event.get() function 
    for event in pygame.event.get():

        # Constant used for quiting 
        if event.type == pygame.QUIT:
            pygame.quit()       # Opposite of pygame.init()
            exit()              # use sys function to die

        # Add our first_surface on the display surface
        # blit - block image transfer = put on surface on another surface
        screen.blit(first_surface, (0,0)) # (0,0) top left pixel
        screen.blit(first_surface, (200, 200)) 

    # Update everything
    pygame.display.update()

    # This till pygame that this while loop should not
    # run faster than 60 time per second. 
    clock.tick(60) 

