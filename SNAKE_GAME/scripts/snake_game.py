import pygame
from pygame.locals import *
from sys import exit
from random import randint


pygame.init()

# screen_size
width = 640
height = 480

# RGB_colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 150, 0)
green_darkness = (0, 200, 0)
red = (255, 127, 0)
red_ugly = (150, 0, 0)
yellow = (255, 255, 0)

# variables
x_snake, y_snake = 320, 240
x_apple, y_apple = randint(0, 620), randint(0, 460)
frames = pygame.time.Clock()
velocity = 3
size_snake = 5
reset = False
points = 0
tamanho = 20
left = right = down = False
up = True

# screen_creator
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('SNAKE GAME')

list_coordinate_snake = []

# font_text
font = pygame.font.SysFont('arial', 30, True, False)


# functions
def snake_body(list_coordinate):
    for xey in list_coordinate:
        pygame.draw.rect(screen, green, (xey[0], xey[1], tamanho, tamanho))


def reset_game():
    global x_snake, y_snake, x_apple, y_apple, reset, size_snake, list_coordinate_snake, points
    x_snake, y_snake = 320, 240
    x_apple, y_apple = randint(0, 620), randint(0, 460)
    reset = False
    size_snake = 5
    list_coordinate_snake = []
    points = 0


def format_text(text, color, XeY):
    new_variable = font.render(text, False, color)
    screen.blit(new_variable, XeY)


while True:
    if len(list_coordinate_snake) >= size_snake:
        list_coordinate_snake.pop(0)

    frames.tick(60)
    screen.fill(green_darkness)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_a:
                if not right:
                    left = True
                    up = down = False

            if event.key == K_d:
                if not left:
                    right = True
                    up = down = False

            if event.key == K_w:
                if not down:
                    up = True
                    left = right = False

            if event.key == K_s:
                if not up:
                    down = True
                    left = right = False

    # objects
    snake = pygame.draw.rect(screen, green, (x_snake, y_snake, 20, 20))
    apple = pygame.draw.rect(screen, red, (x_apple, y_apple, 20, 20))

    # texts
    text = f'size: {points}'
    format_text(text, black, (10, 10))

    # collisions
    if snake.colliderect(apple):
        x_apple, y_apple = randint(0, 620), randint(0, 460)
        size_snake += 5
        points += 1

    # colisão com o proprio corpo
    for x in list_coordinate_snake:
        if x == [x_snake, y_snake]:
        
            reset = True

            while reset:
                frames.tick(60)
                screen.fill(green)

                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == K_r:
                            reset_game()

                    if event.type == QUIT:
                        pygame.quit()
                        exit()

                texto = f'DEATH'
                format_text(texto, black, (width//2 - 60, height//2 - 40))

                texto_2 = f'SIZE: {points}'
                format_text(texto_2, black, (width // 2 - 60, height // 2 + 20))

                texto_3 = f'PRESS R TO RESTART'
                format_text(texto_3, black, (width // 2 - 170, height - 40))

                pygame.display.flip()

    # list and coordinate
    coordinate = [x_snake, y_snake]
    list_coordinate_snake.append(coordinate)
    snake_body(list_coordinate_snake)

    # movements
    if left:
        x_snake -= velocity

    if right:
        x_snake += velocity

    if up:
        y_snake -= velocity

    if down:
        y_snake += velocity

    # screen_infinity
    if x_snake < 0:
        x_snake = 640

    if x_snake > 640:
        x_snake = 0

    if y_snake < 0:
        y_snake = 480

    if y_snake > 480:
        y_snake = 0

    pygame.display.flip()
