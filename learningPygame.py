# The code below was written by Farris Alqalam
# This is my first attempt to building a game. 
# After research, it was recommend to use Pygame.

import pygame
from sys import exit

pygame.init()   #Initiate pygame 
screen = pygame.display.set_mode((800,800))      #Create main display screen  
pygame.display.set_caption("Learning Pygame | Space Invaders | Farris Alqalam")    #Set a window caption
clock = pygame.time.Clock()    # Create a clock object to help us keep track of fps
test_font = pygame.font.Font("fonts/space_invader1.otf", 100)      #Use a font for text

#Surfaces used in game
background_surface = pygame.image.load("Images/background.jpeg")
text_surface = test_font.render("Space Invaders", False, "White")
enemy1_surface = pygame.image.load("Images/enemy1.png")
enemy2_surface = pygame.image.load("Images/enemy2.png")
enemy3_surface = pygame.image.load("Images/enemy3.png")
shooter_surface = pygame.image.load("Images/shooter.png")

# Game variables
enemy1_x_position = 400
enemy1_y_position = 400
enemy2_x_position = 400
enemy2_y_position = 450
enemy3_x_position = 400
enemy3_y_position = 500
shooter_x_position = 550
shooter_y_position = 400


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
        screen.blit(background_surface, (0,0))
        screen.blit(text_surface, (125,150)) 
        screen.blit(enemy1_surface, (enemy1_x_position, enemy1_y_position)) 
        screen.blit(enemy2_surface, (enemy2_x_position, enemy2_y_position)) 
        screen.blit(enemy3_surface, (enemy3_x_position, enemy3_y_position)) 
        screen.blit(shooter_surface, (shooter_x_position, shooter_y_position)) 

    # Update everything
    pygame.display.update()

    # This till pygame that this while loop should not
    # run faster than 60 time per second. 
    clock.tick(60) 

