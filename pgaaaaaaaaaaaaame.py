import buttons
import pygame
win = pygame.display.set_mode((700, 700))
run = True
clock = pygame.time.Clock()
main = buttons.Button(100, 100, 500, 500, (255, 255, 255), "click me")
x = 0
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if pygame.mouse.get_pressed()[0]:
            mouseX, mouseY = pygame.mouse.get_pos()
            if main.clicked((mouseX, mouseY)):
                x+=1
    win.fill((107, 238, 184))
    main.draw(win)
    pygame.display.flip()
    cps = x/60
    with open("cps.txt", "w") as file:
        file.write(f"{round(cps, 2)} cps")
    print(cps)
pygame.quit()