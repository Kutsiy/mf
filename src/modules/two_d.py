import pygame

def start_first_scene(root):
    root.destroy()

    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    running = True

    center = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    top_center = pygame.Vector2(screen.get_width() / 2, 0)


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(color="black")
        pygame.draw.circle(surface=screen, color="white", center=center, radius=40)
        pygame.display.flip()

    pygame.quit()