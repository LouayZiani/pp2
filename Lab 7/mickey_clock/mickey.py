import pygame
import datetime 

pygame.init()

pygame.mixer.music.load(r"C:\Users\hp\Desktop\PP2\Lab 7\mickey_clock\clock-tick-tock-sound-effects.mp3")
pygame.mixer.music.play(-1)

screen = pygame.display.set_mode((900, 800))

pygame.display.set_caption("It's Mickey Mouse O'Clock")

mainclock = pygame.image.load(r"C:\Users\hp\Desktop\PP2\Lab 7\mickey_clock\mainclock.png")
righthand = pygame.image.load(r"C:\Users\hp\Desktop\PP2\Lab 7\mickey_clock\leftarm.png")
lefthand = pygame.image.load(r"C:\Users\hp\Desktop\PP2\Lab 7\mickey_clock\rightarm.png")

clockCenter = screen.get_rect().center

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    now = datetime.datetime.now()

    secondAngle = (now.second / 60) * 360
    minuteAngle = (now.minute / 60) * 360

    location = mainclock.get_rect(center = clockCenter)
    screen.blit(mainclock, location)

    newLeft = pygame.transform.rotate(lefthand, -minuteAngle)
    leftLocation = newLeft.get_rect(center = clockCenter)
    screen.blit(newLeft, leftLocation)


    newRigth = pygame.transform.rotate(righthand, -secondAngle)
    rightLocation = newRigth.get_rect(center = clockCenter)
    screen.blit(newRigth, rightLocation)


    pygame.display.flip()