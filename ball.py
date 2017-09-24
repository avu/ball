import pygame

pygame.init()
pygame.mixer.init()

meaow = pygame.mixer.Sound("Meow.ogg")


screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])
my_cat = pygame.image.load('cat.png')
x = 50
y = 50
y_speed = 4
x_speed = 10

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                meaow.play()

    pygame.time.delay(20)
    pygame.draw.rect(screen, [255, 255, 255], [x, y, 90, 90], 0)
    x = x + x_speed
    y = y + y_speed

    if x > screen.get_width() - 90 or x < 0:
        x_speed = -x_speed
        meaow.play()

    if y > screen.get_height() - 90 or y < 0:
        y_speed = -y_speed
        meaow.play()

    screen.blit(my_cat, [x, y])
    pygame.display.flip()

pygame.quit()

