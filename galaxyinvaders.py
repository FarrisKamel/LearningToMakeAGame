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
title_test_font = pygame.font.Font("fonts/space_invader1.otf", 120)      #Use a font for text
score_test_font = pygame.font.Font("fonts/space_invader1.otf", 50)      #Use a font for text
start_game_test_font = pygame.font.Font("fonts/space_invader1.otf", 50)      #Use a font for text
end_game_test_font = pygame.font.Font("fonts/space_invader1.otf", 150)      #Use a font for text
play_again_test_font = pygame.font.Font("fonts/space_invader1.otf", 50)      #Use a font for text

#Surfaces used in game
background_surface = pygame.image.load("Images/background.jpeg").convert()
title_surface = title_test_font.render("Space Invaders", False, "White")
title_rec = title_surface.get_rect(center = (400, 350))

# Start screen surfaces
start_game_surface = start_game_test_font.render("Start Game", False, "White")
start_game_rec = start_game_surface.get_rect(center = (400,500))
start_game_surface_2 = start_game_test_font.render("Start Game", False, "Black")
start_game_rec_2 = start_game_surface.get_rect(center = (400,500))

# Score surfaces
score_surface = score_test_font.render("Score: ", False, "White")
score_rec = score_surface.get_rect(center = (100, 50))

# End Screen surfaces
end_title_surface = end_game_test_font.render("Game Over", False, "Red")
end_title_rec = end_title_surface.get_rect(center = (400, 350))
end_game_surface = play_again_test_font.render("Play Again", False, "White")
end_game_rec = end_game_surface.get_rect(center = (400,450))
end_game_surface_2 = play_again_test_font.render("Play Again", False, "Black")
end_game_rec_2 = end_game_surface_2.get_rect(center = (400,450))
win_title_surface = end_game_test_font.render("You Win!!", False, "White")
win_title_rec = win_title_surface.get_rect(center = (400, 350))
win_game_surface = play_again_test_font.render("Play Again", False, "White")
win_game_rec = win_game_surface.get_rect(center = (400,450))
win_game_surface_2 = play_again_test_font.render("Play Again", False, "Black")
win_game_rec_2 = win_game_surface_2.get_rect(center = (400,450))


class Shooter(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__() 

        self.x = x 
        self.y = y 
        self.velocity = 4
        self.hitbox = [x+10, y+10]
        self.image = pygame.image.load("Images/shooter.png").convert_alpha()
        self.rect = self.image.get_rect(midtop = (self.x, self.y)) 
        
    def draw(self, state): 
        if state == 1:
            self.image = pygame.image.load("Images/shooter.png").convert_alpha()
            self.rect = self.image.get_rect(midtop = (self.x, self.y)) 
        else:
            self.image = pygame.image.load("Images/dead_shooter.png").convert_alpha()
            self.rect = self.image.get_rect(midtop = (self.x, self.y)) 
        screen.blit(self.image, self.rect)


class Enemy(pygame.sprite.Sprite):

    enemy_location = 900

    def __init__(self, enemy_num, x, y, id):
        super().__init__()
        
        self.id = id            # Keep track of enemy for removal 
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
        if Enemy.enemy_location == 200 or Enemy.enemy_location == 400:
            self.rect.y += 10
        if Enemy.enemy_location <= 0:
            self.rect.x += 2
            Enemy.enemy_location -= 1
        if Enemy.enemy_location == -100 or Enemy.enemy_location == -400:
            self.rect.y += 10
        if Enemy.enemy_location == -900:
            self.rect.y += 10
            Enemy.enemy_location = 900  

    def getId(self):
        return self.id


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__() 

        self.x = x
        self.y = y
        self.velocity = 4
        self.image = pygame.image.load("images/bullet.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (10,10))
        self.rect = self.image.get_rect(midbottom = (self.x, self.y))

    def draw(self):
        self.image = pygame.image.load("images/bullet.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (10,10))
        self.rect = self.image.get_rect(midbottom = (self.x, self.y))
        screen.blit(self.image, self.rect)

def drawScore(score):
    new_score_surface = score_test_font.render(score, False, "White")
    new_score_rec = score_surface.get_rect(center = (250, 50))
    screen.blit(new_score_surface, new_score_rec) 

def redrawGameWindow(screen_type, state, score):
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
        screen.blit(background_surface, (0,0))
        screen.blit(score_surface, score_rec) 
        enemies_group.draw(screen)
        enemies_group.update() 
        shooter.draw(state)
        shooter.update() 
        for bullet in bullets:
            bullet.draw()
            bullet.update()
        drawScore(score) 

    elif screen_type == 4:
        screen.blit(background_surface, (0,0))
        screen.blit(end_title_surface, end_title_rec) 
        screen.blit(end_game_surface, end_game_rec) 
    
    elif screen_type == 5:
        screen.blit(background_surface, (0,0))
        screen.blit(end_title_surface, end_title_rec) 
        pygame.draw.rect(screen, "White", end_game_rec_2)
        screen.blit(end_game_surface_2, end_game_rec_2) 
    
    elif screen_type == 6:
        screen.blit(background_surface, (0,0))
        screen.blit(win_title_surface, win_title_rec) 
        screen.blit(win_game_surface, win_game_rec) 
    
    elif screen_type == 7:
        screen.blit(background_surface, (0,0))
        screen.blit(win_title_surface, win_title_rec) 
        pygame.draw.rect(screen, "White", win_game_rec_2)
        screen.blit(win_game_surface_2, win_game_rec_2) 
    
    pygame.display.update()

def enemiesConfig(enemies, state):
    if state == 1:      # Placing the enemies in the position they need to be 
        count = 0
        id = 1
        for position in enemies:
            enemies_group.add(Enemy(count, position[0], position[1], id))  
            count += 1
            if count > 2:
                count = 0
            id += 1
    
    if state == 2:  # Remove all the enemies
        for enemy in enemies_group:
            enemies_group.remove(enemy) 


enemy_location = 600            # Variables for moving the enemies from left to right

# Creating the enemies
enemies_group = pygame.sprite.Group()
enemy_position_for_spawn = [(x, y) for x in range (200, 700, 70) for y in range(200, 500, 70)]

shooter = Shooter(400, 700)     # Creating the Shooter group
screen_type = 1                 # Keep track of screen type
shooter_state = 1               # Used to keep track of the shooters state
bullets = []                    # List for the bullets fired
score = 0                       # Key track of score 

#Create a infinite loop using a while true loop
while True:
    
    # Check if player beat the game
    if score == 200:
        screen_type = 6

    mouse_position = pygame.mouse.get_pos()         # Get the mouse position

    # Move the bullets across the screen when shot 
    for bullet in bullets:
        if bullet.y > 0:
            bullet.y -= bullet.velocity
        else:
            bullets.pop(bullets.index(bullet))

    # Event loop
    for event in pygame.event.get():

        # Constant used for quiting 
        if event.type == pygame.QUIT:
            pygame.quit()       # Opposite of pygame.init()
            exit()              # use sys function to die

        if screen_type == 1:    
            if start_game_rec.collidepoint(mouse_position):
                screen_type = 2                         # Set the screen_type to select mode

        if screen_type == 2:    
            if not start_game_rec.collidepoint(mouse_position):
                screen_type = 1                         # Set screen_type to home mode

            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_game_rec.collidepoint(event.pos):
                    shooter.x, shooter.y = 400, 700     # Set the shooters in the correct position 
                    shooter_state = 1                   # Set the shooters state to alive
                    screen_type = 3                     # Set screen_type to game 
                    score = 0                           # Set score to 0
                    enemiesConfig(enemy_position_for_spawn, 1)  # Spawn enemies

        if screen_type == 3:
            if pygame.sprite.spritecollide(shooter, enemies_group, False):
                shooter_state = 2                       # Set shooter_state to dead
                screen_type = 4                         # Set the screen_type to game over screen
                enemiesConfig(enemy_position_for_spawn, 2)      # Remove all eneies

        if screen_type == 4:
            if end_game_rec.collidepoint(mouse_position):
                screen_type = 5                         # Set the screen_type to select mode

        if screen_type == 5:    
            if not end_game_rec.collidepoint(mouse_position):
                screen_type = 4                         # Set screen_type to gameover mode

            if event.type == pygame.MOUSEBUTTONDOWN:
                if end_game_rec.collidepoint(event.pos):
                    shooter.x, shooter.y = 400, 700     # Set the shooters in the correct position 
                    shooter_state = 1                   # Set the shooters state to alive
                    screen_type = 3                     # Set screen_type to game 
                    score = 0                           # Set score to 0
                    enemiesConfig(enemy_position_for_spawn, 1)  # Spawn enemies
        
        if screen_type == 6:
            if win_game_rec.collidepoint(mouse_position):
                screen_type = 7                         # Set the screen_type to select mode
                enemiesConfig(enemy_position_for_spawn, 2)      # Remove all enemies

        if screen_type == 7:    
            if not win_game_rec.collidepoint(mouse_position):
                screen_type = 6                         # Set screen_type to you win mode

            if event.type == pygame.MOUSEBUTTONDOWN:
                if win_game_rec.collidepoint(event.pos):
                    shooter.x, shooter.y = 400, 700     # Set the shooters in the correct position 
                    shooter_state = 1                   # Set the shooters state to alive
                    screen_type = 3                     # Set screen_type to game 
                    score = 0                           # Set score to 0
                    enemiesConfig(enemy_position_for_spawn, 1)  # Spawn Enemies

        bullet_shot = False                             # Used to shoot a bullet a time 
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if len(bullets) < 20: 
                bullets.append(Bullet(shooter.x, shooter.y))    # Add bullets
            bullet_shot = True
        
        if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
            bullet_shot = False        

                 
    # Continous Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        shooter.y -= shooter.velocity
    if keys[pygame.K_DOWN]:
        shooter.y += shooter.velocity
    if keys[pygame.K_RIGHT]:
        shooter.x += shooter.velocity
    if keys[pygame.K_LEFT]:
        shooter.x -= shooter.velocity 

    for bullet in bullets: 
        enemies_hit = pygame.sprite.spritecollide(bullet, enemies_group, True)  # Check for collisions
        if enemies_hit:                                                         # If any enemies were hit
            bullets.remove(bullet)                                              # Remove the bullet
            for enemy in enemies_hit:                                           # Loop through the enemies hit
                score += 5

    # Keep the shooter within the screen boundaries
    shooter.x = max(20, min(800 - 50, shooter.x))
    shooter.y = max(20, min(800 - 50, shooter.y))
   
    redrawGameWindow(screen_type, shooter_state, str(score))        # Update everything 

    # This till pygame that this while loop should not
    # run faster than 60 time per second. 
    clock.tick(60) 
