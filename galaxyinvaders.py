# The code below was written by Farris Alqalam
# This is my first attempt to building a game. 
# After research, it was recommend to use Pygame.

import pygame
from sys import exit
from random import randint, choice

#Game Setup
pygame.init()   #Initiate pygame 
screen = pygame.display.set_mode((800,800))      #Create main display screen  
pygame.display.set_caption("Learning Pygame | Space Invaders | Farris Alqalam")    #Set a window caption
clock = pygame.time.Clock()    # Create a clock object to help us keep track of fps
title_test_font = pygame.font.Font("fonts/space_invader1.otf", 100)      #Use a font for text
score_test_font = pygame.font.Font("fonts/space_invader1.otf", 50)      #Use a font for text
start_game_test_font = pygame.font.Font("fonts/space_invader1.otf", 75)      #Use a font for text

# TODO: Prob going to delete these 
game_start_1 = True   # this is the state of the game
game_start_2 = False
game_active = False  # This is the state of the game
game_over = False   # This is the state of the game

#Surfaces used in game
background_surface = pygame.image.load("Images/background.jpeg").convert()
title_surface = title_test_font.render("Space Invaders", False, "White")
title_rec = title_surface.get_rect(center = (400, 150))
start_game_surface = start_game_test_font.render("Start Game", False, "White")
start_game_rec = start_game_surface.get_rect(center = (400,600))
start_game_surface_2 = start_game_test_font.render("Start Game", False, "Black")
start_game_rec_2 = start_game_surface.get_rect(center = (400,600))
score_surface = score_test_font.render("Score: ", False, "White")
score_rec = score_surface.get_rect(center = (100, 50))

# TODO: Prob going to delete later
bullet_surface = pygame.image.load("Images/bullet.png").convert_alpha()
bullet_rec = bullet_surface.get_rect(midtop = (400, 700))

class Shooter(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__() 

        self.x = x 
        self.y = y 
        self.velocity = 6
        
    def draw(self):
        
        self.image = pygame.image.load("Images/shooter.png").convert_alpha()
        self.rect = self.image.get_rect(midtop = (self.x, self.y)) 
        screen.blit(self.image, self.rect)


class Enemy(pygame.sprite.Sprite):

    enemy_location = 900

    def __init__(self, enemy_num, x, y):

        super().__init__()

        if enemy_num == 0:
            self.image = pygame.image.load("images/enemy1.png").convert_alpha()
            self.rect = self.image.get_rect(midbottom = (x, y))
        elif enemy_num == 1: 
            self.image = pygame.image.load("images/enemy2.png").convert_alpha()
            self.rect = self.image.get_rect(midbottom = (x, y))
        else: 
            self.image = pygame.image.load("images/enemy3.png").convert_alpha()
            self.rect = self.image.get_rect(midbottom = (x, y))

    def update(self):

        if Enemy.enemy_location > 0:
            self.rect.x -= 2
            Enemy.enemy_location -= 1
            # print(Enemy.enemy_location)

        if Enemy.enemy_location == 200 or Enemy.enemy_location == 400:
            self.rect.y += 10

        if Enemy.enemy_location <= 0:
            self.rect.x += 2
            Enemy.enemy_location -= 1
            # print(Enemy.enemy_location)

        if Enemy.enemy_location == -100 or Enemy.enemy_location == -400:
            self.rect.y += 10

        if Enemy.enemy_location == -900:
            self.rect.y += 10
            Enemy.enemy_location = 900  

class Bullet(object):
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.velocity = 30

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)


def redrawGameWindow(screen_type):
    if screen_type == 1:
        screen.blit(background_surface, (0,0))
        screen.blit(title_surface, title_rec) 
        screen.blit(start_game_surface, start_game_rec) 

    elif screen_type == 2:
        screen.blit(background_surface, (0,0))
        screen.blit(title_surface, title_rec) 
        pygame.draw.rect(screen, "White", start_game_rec_2)
        screen.blit(start_game_surface_2, start_game_rec_2) 

    elif screen_type == 3:
        # Add our first_surface on the display surface
        # blit - block image transfer = put on surface on another surface
        screen.blit(background_surface, (0,0))
        screen.blit(score_surface, score_rec) 
        enemies_group.draw(screen)
        enemies_group.update() 
        shooter.draw()
        shooter.update()
        screen.blit(bullet_surface, bullet_rec)
        screen.blit(bullet_surface, bullet_rec)
        
    else:
        screen.fill("Green")
    
    pygame.display.update()

# Variables for moving the enemies from left to right
enemy_location = 600

# Function to shoot the bullet
def bulletMoveUp(bullet_rec):
    new_bullet_rec = bullet_rec.move(0, -4)
    return new_bullet_rec

#Groups
# Creating the enemies
enemies_group = pygame.sprite.Group()
enemy_position_for_spawn = [(x, y) for x in range (200, 700, 70) for y in range(200, 500, 70)]
count = 0
# Placing the enemies in the position they need to be
for position in enemy_position_for_spawn:
    enemies_group.add(Enemy(count, position[0], position[1]))  
    count += 1
    if count > 2:
        count = 0

# Creating the Shooter group
shooter = Shooter(400, 700)

# Keep track of screen type
screen_type = 1

#Create a infinite loop using a while true loop
while True:

    # This is where all the drawing and elements of the game should be 

    # Create a loop (essentially a for loop)
    # To look for all the possibel events that may happen
    # Use the pygame.event.get() function 
    mouse_position = pygame.mouse.get_pos()
    for event in pygame.event.get():

        # Constant used for quiting 
        if event.type == pygame.QUIT:
            pygame.quit()       # Opposite of pygame.init()
            exit()              # use sys function to die

        if screen_type == 1:    
            if start_game_rec.collidepoint(mouse_position):
                screen_type = 2 

        if screen_type == 2:    
            if not start_game_rec.collidepoint(mouse_position):
                screen_type = 1 

            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_game_rec.collidepoint(event.pos):
                    shooter.x, shooter.y = 400, 700     # Set the shooters in the correct position 
                    screen_type = 3                     

             
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        # print("Move U")
        shooter.y -= shooter.velocity
    if keys[pygame.K_DOWN]:
        # print("Move U")
        shooter.y += shooter.velocity
    if keys[pygame.K_RIGHT]:
        # print("Move Right")
        shooter.x += shooter.velocity
    if keys[pygame.K_LEFT]:
        # print("Move Left")
        shooter.x -= shooter.velocity 

    # Keep the shooter within the screen boundaries
    shooter.x = max(20, min(800 - 50, shooter.x))
    shooter.y = max(20, min(800 - 50, shooter.y))

    # Update everything    
    # pygame.display.update()
    redrawGameWindow(screen_type)

    # This till pygame that this while loop should not
    # run faster than 60 time per second. 
    clock.tick(60) 
