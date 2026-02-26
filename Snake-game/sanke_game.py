# import pygame
# import time

# import random                         
# pygame.init()
        
# white = (255, 255, 255)
# yellow = (255, 255, 102)
# black = (0, 0, 0)
# red = (213, 50, 80)
# green = (0, 255, 0)
# blue = (50, 153, 213)
                         
# dis_width = 800
# dis_height = 600
                         
# dis = pygame.display.set_mode((dis_width, dis_height))
# pygame.display.set_caption('Snake Game by Sanjita Ray')
                         
# clock = pygame.time.Clock()
                         
# snake_block = 10
# snake_speed = 15
                         
# font_style = pygame.font.SysFont("bahnschrift", 25)
# score_font = pygame.font.SysFont("comicsansms", 35)
                         
                         
# def Your_score(score):
#     value = score_font.render("Your Score: " + str(score), True, yellow)
#     dis.blit(value, [0, 0])
                         
                         
                         
# def our_snake(snake_block, snake_list):
#     for x in snake_list:
#         pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
                         
                         
# def message(msg, color):
#     mesg = font_style.render(msg, True, color)
#     dis.blit(mesg, [dis_width / 6, dis_height / 3])
                         
                         
# def gameLoop():
#     game_over = False
#     game_close = False
                         
#     x1 = dis_width / 2
#     y1 = dis_height / 2
                         
#     x1_change = 0
#     y1_change = 0
                         
#     snake_List = []
#     Length_of_snake = 1
                         
#     foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
#     foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                         
#     while not game_over:
                         
#         while game_close == True:
#             dis.fill(blue)
#             message("You Lost! Press C-Play Again or Q-Quit", red)
#             Your_score(Length_of_snake - 1)
#             pygame.display.update()
                         
#             for event in pygame.event.get():
#                 if event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_q:
#                         game_over = True
#                         game_close = False
#                     if event.key == pygame.K_c:
#                         gameLoop()
                         
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 game_over = True
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_LEFT:
#                     x1_change = -snake_block
#                     y1_change = 0
#                 elif event.key == pygame.K_RIGHT:
#                     x1_change = snake_block
#                     y1_change = 0
#                 elif event.key == pygame.K_UP:
#                     y1_change = -snake_block
#                     x1_change = 0
#                 elif event.key == pygame.K_DOWN:
#                     y1_change = snake_block
#                     x1_change = 0
                         
#         if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
#             game_close = True
#         x1 += x1_change
#         y1 += y1_change
#         dis.fill(blue)
#         pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
#         snake_Head = []
#         snake_Head.append(x1)
#         snake_Head.append(y1)
#         snake_List.append(snake_Head)
#         if len(snake_List) > Length_of_snake:
#             del snake_List[0]
                         
#         for x in snake_List[:-1]:
#             if x == snake_Head:
#                 game_close = True
                         
#         our_snake(snake_block, snake_List)
#         Your_score(Length_of_snake - 1)
                         
#         pygame.display.update()
                         
#         if x1 == foodx and y1 == foody:
#             foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
#             foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
#             Length_of_snake += 1
                         
#         clock.tick(snake_speed)
                         
#     pygame.quit()
# gameLoop()



import pygame
import random

# Initialize pygame
pygame.init()

# Screen size
WIDTH = 600
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Snake Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (50, 153, 213)

# Snake settings
SNAKE_SIZE = 10
SPEED = 15

clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 25)

# Display score
def show_score(score):
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

# Draw snake
def draw_snake(snake_body):
    for block in snake_body:
        pygame.draw.rect(screen, BLACK, [block[0], block[1], SNAKE_SIZE, SNAKE_SIZE])

# Game loop
def game():
    running = True
    game_over = False

    # Snake position
    x = WIDTH // 2
    y = HEIGHT // 2
    x_change = 0
    y_change = 0

    snake_body = []
    snake_length = 1

    # Food position
    food_x = random.randrange(0, WIDTH - SNAKE_SIZE, 10)
    food_y = random.randrange(0, HEIGHT - SNAKE_SIZE, 10)

    while running:

        while game_over:
            screen.fill(BLUE)
            msg = font.render("Game Over! Press C to Play Again or Q to Quit", True, RED)
            screen.blit(msg, (40, HEIGHT // 2))
            show_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        running = False
                        game_over = False
                    if event.key == pygame.K_c:
                        game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -SNAKE_SIZE
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = SNAKE_SIZE
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -SNAKE_SIZE
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = SNAKE_SIZE
                    x_change = 0

        # Wall collision
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            game_over = True

        x += x_change
        y += y_change
        screen.fill(BLUE)

        pygame.draw.rect(screen, GREEN, [food_x, food_y, SNAKE_SIZE, SNAKE_SIZE])

        snake_body.append([x, y])
        if len(snake_body) > snake_length:
            snake_body.pop(0)

        # Self collision
        for block in snake_body[:-1]:
            if block == [x, y]:
                game_over = True

        draw_snake(snake_body)
        show_score(snake_length - 1)

        pygame.display.update()

        # Eating food
        if x == food_x and y == food_y:
            food_x = random.randrange(0, WIDTH - SNAKE_SIZE, 10)
            food_y = random.randrange(0, HEIGHT - SNAKE_SIZE, 10)
            snake_length += 1

        clock.tick(SPEED)

    pygame.quit()

game()






























