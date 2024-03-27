import pygame
import sys

pygame.init()

width = 800
height = 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Red Ball")
clock = pygame.time.Clock()

ball_radius = 25
ball_x = width / 2
ball_y = height / 2
ball_speed = 20

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and ball_y - ball_speed > 0:
        ball_y -= ball_speed
    if keys[pygame.K_DOWN] and ball_y + ball_speed < height:
        ball_y += ball_speed
    if keys[pygame.K_LEFT] and ball_x - ball_speed > 0:
        ball_x -= ball_speed
    if keys[pygame.K_RIGHT] and ball_x + ball_speed < width:
        ball_x += ball_speed

    screen.fill("White")

    pygame.draw.circle(screen, "Red", (ball_x, ball_y), ball_radius)

    pygame.display.flip()
    clock.tick(30)
