import pygame, sys # import pygame and sys(system-specific parameters and functions)
import random
# what happens when you have 'pygame' as a filename?
# Check the terminal (most likely due to a circular import)

pygame.init()
pygame.display.init() # initiates 
clock = pygame.time.Clock() #


SCREEN_WIDTH = 1000 # Width of a screen
SCREEN_HEIGHT = 800 # Height of a screen


# Displays Screen
SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) # inside mode is tuple
pygame.display.set_caption('Pong') # Displays caption- the title head

PlAYER_1_SCORE = 0
PlAYER_2_SCORE = 0

FONT = pygame.font.SysFont('Default', 60)

# pygame.Rect() is pygame object for storing rectangular coordinates.
# pygame.Rect(x, y, width, height)
# pygame.rect() is for drawing rectangle

# Create Ball using pygame.Rect
BALL = pygame.Rect(SCREEN_WIDTH/2 -20,SCREEN_HEIGHT/2-20,40,40)

# Right and left player co-ordinates
RIGHT_PLAYER_X = 950 #SCREEN_WIDTH - 50 
RIGHT_PLAYER_Y = 300 #SCREEN_WIDTH/5+100
LEFT_PLAYER_X  = 10  #Constant 10
LEFT_PLAYER_Y  = 300 #SCREEN_WIDTH/5+100


# Create Player using pygame.Rect
LEFT_PLAYER = pygame.Rect(LEFT_PLAYER_X,LEFT_PLAYER_Y,40, 200)
RIGHT_PLAYER = pygame.Rect(RIGHT_PLAYER_X,RIGHT_PLAYER_Y,40,200)

# Create a mid-line 
MID_LINE = pygame.Rect(SCREEN_WIDTH/2 -5, 0, 5,800)

# Extra info on colors:
# create with color with (r,g,b) - (255,0,0) or pygame.color('name)

Bar_Speed = 10 # Speed of the left and right bar on Y axis
Ball_Speed_X = 10 # Speed of the ball on x axis. Ball is moving by 10 units at a time
Ball_Speed_Y = 15 # Speed of the ball on Y axis

while True:
    for event in pygame.event.get(): # all user interaction are called in event
        if event.type == pygame.QUIT: # Pygame calls x on the window QUIT
            pygame.quit() # initialize the quit method # Looks like code runs without it
            sys.exit() # exit the screen
    # Ball_Speed_X = random.randrange(10,15)
    # Ball_Speed_Y = random.randrange(10,15)

    BALL.x += Ball_Speed_X # x coordinate of the position of the ball
    BALL.y += Ball_Speed_Y # y coordinate of the position of the ball
   
    # Changing the direction of the ball if the ball hits the celing or the floor. 
    if BALL.top <= 0 or BALL.bottom >= SCREEN_HEIGHT:
        Ball_Speed_Y *= -1
    
    # If the ball hits the left wall, the right player gets the point
    if BALL.left == 0:
        PlAYER_2_SCORE = PlAYER_2_SCORE+1
        #delay(10)
        BALL.x = 500 # x coordinate of the position of the ball
        BALL.y = 500 # y coordinate of the position of the ball
    
    # If the ball hits the right wall, the left player gets the point
    if BALL.right == SCREEN_WIDTH:
        PlAYER_1_SCORE = PlAYER_1_SCORE+1
        #delay(10)
        BALL.x = 500 
        BALL.y = 500

    # Score tracking
    SCORE_1 = FONT.render(str(PlAYER_1_SCORE), True, (55,255,20))
    SCORE_2 = FONT.render(str(PlAYER_2_SCORE), True, (55,255,20))

    if BALL.colliderect(RIGHT_PLAYER):
        Ball_Speed_Y = -1*(random.randrange(10,15))
        Ball_Speed_X = -1*(random.randrange(10,15))

    if BALL.colliderect(LEFT_PLAYER):
        Ball_Speed_Y = (random.randrange(10,15))
        Ball_Speed_X = (random.randrange(10,15)) 

    KEYS = pygame.key.get_pressed() # Keeps all the pressed keys in a list
        
    # When the up arrow key is pressed (up or down)
    # We only change the Y- cordinates because it's either going up or down
    if KEYS[pygame.K_UP] and RIGHT_PLAYER_Y > 0:  
        # decrement in y co-ordinate
        RIGHT_PLAYER_Y -= Bar_Speed

    # When the down arrow key is pressed   
    if KEYS[pygame.K_DOWN] and RIGHT_PLAYER_Y < 600:
        # increment in y co-ordinate
        RIGHT_PLAYER_Y += Bar_Speed

    if KEYS[pygame.K_e] and LEFT_PLAYER_Y > 0 :  # The left player goes up 
        # decrement in y co-ordinate
        LEFT_PLAYER_Y -= Bar_Speed

    # When the down arrow key is pressed   
    if KEYS[pygame.K_d] and LEFT_PLAYER_Y < 600: # The left player goes down
        # increment in y co-ordinate
        LEFT_PLAYER_Y += Bar_Speed


    SCREEN.fill(pygame.Color('grey4')) ## see what is does with it



    #pygame.draw.rect(random, (255, 0, 0), (x, y, width, height))

    pygame.draw.ellipse(SCREEN,(55,255,20), BALL) # pygame.draw.ellipse draws epllipse
    pygame.draw.rect(SCREEN,(55,255,20),LEFT_PLAYER) # draw.rect draws rectangle
    pygame.draw.rect(SCREEN,(55,255,20),RIGHT_PLAYER)
    pygame.draw.rect(SCREEN,(55,255,20), MID_LINE)
   

    SCREEN.blit(SCORE_1,(400, 20))
    SCREEN.blit(SCORE_2,(575, 20))


    RIGHT_PLAYER = pygame.Rect(RIGHT_PLAYER_X,RIGHT_PLAYER_Y,40,200)
    LEFT_PLAYER = pygame.Rect(LEFT_PLAYER_X,LEFT_PLAYER_Y,40,200)
    # Update the Window
    pygame.display.flip() # How is is different from pygame.display.update()
    clock.tick(50) # Slow down the display to see what is going on @ 50 fps








