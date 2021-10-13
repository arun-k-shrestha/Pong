import pygame, sys # import pygame and sys(system-specific parameters and functions)

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

# FONT = pygame.font.SysFont('comicsansms', 29)
# TEXT = FONT.render('Score', True, (0,128,0))

PlAYER_1_SCORE = 0
PlAYER_2_SCORE = 0

FONT = pygame.font.SysFont('Default', 60)
SCORE_1 = FONT.render(str(PlAYER_1_SCORE), True, (55,255,20))
SCORE_2 = FONT.render(str(PlAYER_2_SCORE), True, (55,255,20))

# pygame.Rect() is pygame object for storing rectangular coordinates.
# pygame.Rect(x, y, width, height)
# pygame.rect() is for drawing rectangle

# Create Ball using pygame.Rect
BALL = pygame.Rect(SCREEN_WIDTH/2 -20,SCREEN_HEIGHT/2-20,40,40)

# Right and left player co-ordinates
RIGHT_PLAYER_X = 950 #SCREEN_WIDTH - 50 
RIGHT_PLAYER_Y = 300 #SCREEN_WIDTH/5+100
LEFT_PLAYER_X  = 10
LEFT_PLAYER_Y  = 300 #SCREEN_WIDTH/5+100


# Create Player using pygame.Rect
LEFT_PLAYER = pygame.Rect(LEFT_PLAYER_X,LEFT_PLAYER_Y,40, 200)
RIGHT_PLAYER = pygame.Rect(RIGHT_PLAYER_X,RIGHT_PLAYER_Y,40,200)

# Create a mid-line 

MID_LINE = pygame.Rect(SCREEN_WIDTH/2 -5, 0, 5,800)

# Extra info on colors:
# create with color with (r,g,b) - (255,0,0) or pygame.color('name)

#SCORE = pygame.font.Font()

Bar_Speed = 20
Ball_Speed_X = 3
Ball_Speed_Y = 7

while True:
    for event in pygame.event.get(): # all user interaction are called in event
        if event.type == pygame.QUIT: # Pygame calls x on the window QUIT
            pygame.quit() # initialize the quit method # Looks like code runs without it
            sys.exit() # exit the screen
    
    BALL.x = Ball_Speed_X + BALL.x # UNDERSTAND THIS ??
    BALL.y += Ball_Speed_Y  # UNDERSTAND THIS ??

    if BALL.top <= 0 or BALL.bottom >= SCREEN_HEIGHT:
        Ball_Speed_Y *= -1
    # if BALL.left <= 0 or BALL.right >= SCREEN_WIDTH:
    #     Ball_Speed_X *= -1

    # if BALL.left <= LEFT_PLAYER or BALL.right >= RIGHT_PLAYER:
    #     Ball_Speed_X *= -1


    if BALL.colliderect(LEFT_PLAYER) or BALL.colliderect(RIGHT_PLAYER):
        Ball_Speed_Y *= -1
        Ball_Speed_X *= -1
    
    keys = pygame.key.get_pressed() # Keeps all the pressed keys in a list
        
    # When the up arrow key is pressed (up or down)
    # We only change the Y- cordinates because it's either going up or down
    if keys[pygame.K_UP] and RIGHT_PLAYER_Y > 0:  
        # decrement in y co-ordinate
        RIGHT_PLAYER_Y -= Bar_Speed

    # When the down arrow key is pressed   
    if keys[pygame.K_DOWN] and RIGHT_PLAYER_Y < 600:
        # increment in y co-ordinate
        RIGHT_PLAYER_Y += Bar_Speed

    if keys[pygame.K_e] and LEFT_PLAYER_Y > 0 :  # The left player goes up 
        # decrement in y co-ordinate
        LEFT_PLAYER_Y -= Bar_Speed

    # When the down arrow key is pressed   
    if keys[pygame.K_d] and LEFT_PLAYER_Y < 600: # The left player goes down
        # increment in y co-ordinate
        LEFT_PLAYER_Y += Bar_Speed

    
    #scoretext = myfont.render("Score = "+str(score), 1, (0,0,0))
    SCREEN.fill(pygame.Color('grey4')) ## see what is does with it

    #pygame.draw.rect(random, (255, 0, 0), (x, y, width, height))

    pygame.draw.ellipse(SCREEN,(55,255,20), BALL) # pygame.draw.ellipse draws epllipse
    pygame.draw.rect(SCREEN,(55,255,20),LEFT_PLAYER) # draw.rect draws rectangle
    pygame.draw.rect(SCREEN,(55,255,20),RIGHT_PLAYER)
    pygame.draw.rect(SCREEN,(55,255,20), MID_LINE)
    #pygame.blit(TEXT, 25, 250)

    SCREEN.blit(SCORE_1,(400, 20)) # to display the score of player 1
    SCREEN.blit(SCORE_2,(575, 20)) # to display the score of player 2


    RIGHT_PLAYER = pygame.Rect(RIGHT_PLAYER_X,RIGHT_PLAYER_Y,40,200)
    LEFT_PLAYER = pygame.Rect(LEFT_PLAYER_X,LEFT_PLAYER_Y,40,200)
    # Update the Window
    pygame.display.flip() # How is is different from pygame.display.update()
    clock.tick(50) # Slow down the display to see what is going on @ 60 fps

