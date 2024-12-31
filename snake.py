import pygame
import time
import random

# Initialize the pygame
pygame.init()

# Define colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
cyan = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
red = (213, 50, 80)

# Set display width and height
display_width = 700
display_height = 500

# Restrict the game area to start below the welcome message and score
game_area_start_y = 100  # The y-coordinate below which the game starts

# Create display window
dis = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Game by Alefiya')

# Define game clock
clock = pygame.time.Clock()

# Snake variables
snake_block = 10
snake_speed = 10  # Slower speed

# Fonts
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)          
welcome_font = pygame.font.SysFont("dejavusansmono", 35)

# Function to display the score
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, white)
    dis.blit(value, [0, 50])  # Move score below the welcome message

# Function to display the welcome message
def display_welcome_message():
    welcome_message = welcome_font.render("Welcome To Alefiya's Game", True, blue)
    dis.blit(welcome_message, [display_width / 8, 10])

# Function to draw the snake
def our_snake(snake_block, snake_List):
    for x in snake_List:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])

# Function to display messages on the screen
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [display_width / 6, display_height / 3])

# Function to pause the game
def pause():
    paused = True
    message("Game Paused! Press P to Resume", yellow)
    pygame.display.update()
    
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:  # Resume when 'P' is pressed again
                    paused = False
        clock.tick(5)

# Main game loop
def gameLoop():
    game_over = False
    game_close = False

    # Snake's initial position (below the restricted area)
    x1 = display_width / 2
    y1 = display_height / 2

    # Change in position
    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    # Generate food in random position (ensure food spawns below the restricted area)
    foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(game_area_start_y, display_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
                elif event.key == pygame.K_p:  # Check if 'P' is pressed to pause
                    pause()

        # Check if snake hits the boundaries
        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < game_area_start_y:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)

        # Display the welcome message
        display_welcome_message()

        pygame.draw.rect(dis, yellow, [foodx, foody, snake_block, snake_block])

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        # Check if snake ate the food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(game_area_start_y, display_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Start the game
gameLoop()
