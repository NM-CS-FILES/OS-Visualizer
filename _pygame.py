import pygame

###

pygame.init()
pygame.font.init()

###

font = pygame.font.SysFont(pygame.font.get_default_font(), 30)
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

###

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    ###

    pygame.draw.circle(screen, "red", (100, 100), 40)
    
    text_surface = font.render("AB", True, "White")
    screen.blit(text_surface, (100, 100))

    ###

    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit()