import pygame

pygame.init()

screen = pygame.display.set_mode( ( 640,480 ) )
pygame.display.set_caption("Test Pygame")

x = 240
y = 120
speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    
    if keys [pygame.K_LEFT]:
        x -= speed
    elif  keys [pygame.K_RIGHT]:
        x += speed
    elif keys [pygame.K_UP]:
        y -= speed
    elif keys [pygame.K_DOWN]:
        y += speed


    screen.fill( ( 30, 30, 50) )
    pygame.draw.circle( screen, ( 255, 100, 100), (320,240), 30)

    pygame.display.flip()
