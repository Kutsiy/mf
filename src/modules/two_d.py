import pygame
from math import *

def start_first_scene(root):
    root.destroy()

    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    running = True

    center = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    top_center = pygame.Vector2(screen.get_width() / 2, 0)
    time = 0.0
    gravity = 9.81 # m / s 
    line_l = sqrt(pow((center.x - top_center.x), 2) + pow((center.y - top_center.y), 2)) # m, don't forget it
    period_T = (2 * pi) * sqrt((line_l / gravity))

    dt = 0.01
    w = (2 * pi) / period_T

    theta_rero = radians(45)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
        screen.fill(color="black")

        time += dt

        theta = theta_rero * cos((w * time))

        center.x = top_center.x + line_l * sin(theta)
        center.y = top_center.y + line_l * cos(theta)

        pygame.draw.line(surface=screen, color="white", start_pos=top_center, end_pos=center, width=4)
        pygame.draw.circle(surface=screen, color="red", center=center, radius=40,)
        pygame.display.flip()

    pygame.quit()

def start_second_scene(root):
    root.destroy()

    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        pygame.draw.circle(surface=screen, color="white", center=(250, 250), radius=40,)
        pygame.display.flip()

    pygame.quit()
