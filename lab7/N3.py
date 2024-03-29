import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Шар")

white = (255, 255, 255)
red = (255, 0, 0)

x, y = 400, 300
radius = 25

speed = 20


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    x = max(radius, min(x, 800 - radius))
    y = max(radius, min(y, 600 - radius))


    screen.fill(white)


    pygame.draw.circle(screen, red, (x, y), radius)


    pygame.display.flip()


    pygame.time.delay(30)