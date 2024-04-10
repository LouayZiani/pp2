import pygame

pygame.init()

WIDTH = 800
HEIGHT = 480

screen = pygame.display.set_mode((WIDTH, HEIGHT))
baseLayer = pygame.Surface((WIDTH, HEIGHT))

done = False

prevX = -1
prevY = -1
currX = -1
currY = -1

LMBPressed = False
drawType = "Rect"
color = "Red"
shapes = []  

def calculate_rect(x1, x2, y1, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

def check_collision(x, y):
    for shape_type, shape, _ in shapes:
        if shape_type == 'Rect':
            if shape.collidepoint(x, y):
                shapes.remove((shape_type, shape, _))
                return True
        elif shape_type == 'Circle':
            cx, cy, radius = shape
            if (x - cx)**2 + (y - cy)**2 <= radius**2:
                shapes.remove((shape_type, shape, _))
                return True
    return False

font = pygame.font.Font(None, 24)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            LMBPressed = True
            prevX = event.pos[0]
            prevY = event.pos[1]
            currX = event.pos[0]
            currY = event.pos[1]

        if event.type == pygame.MOUSEMOTION:
            if LMBPressed:
                currX = event.pos[0]
                currY = event.pos[1]

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            LMBPressed = False
            if drawType == 'Rect':
                shapes.append(('Rect', calculate_rect(prevX, currX, prevY, currY), color))
            elif drawType == 'Circle':
                radius = abs(currX - prevX) // 2
                shapes.append(('Circle', (prevX + radius, prevY + radius, radius), color))
            elif drawType == 'Erase':
                check_collision(currX, currY)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                drawType = "Rect"
            elif event.key == pygame.K_c:
                drawType = "Circle"
            elif event.key == pygame.K_e:
                drawType = "Erase"
            elif event.key == pygame.K_y:
                color = "Yellow"
            elif event.key == pygame.K_b:
                color = "Blue"
            elif event.key == pygame.K_g:
                color = "Green"
            elif event.key == pygame.K_z:
                color = "Red"

    screen.fill("Black")
    
    text = [  "Yellow = Y",
               "Blue = B",
               "Green = G",
               "Z for Red",
               "-----------------",
               "R = Rectangle",
               "C = Circle",
               "E = Eraser" ]
    for i, text in enumerate(text):
        text_surface = font.render(text, True, "Gold")
        screen.blit(text_surface, (10, 10 + i * 20))
    
    if LMBPressed:
        if drawType == 'Rect':
            temp_rect = calculate_rect(prevX, currX, prevY, currY)
            pygame.draw.rect(screen, color, temp_rect, 2)
        elif drawType == 'Circle':
            radius = abs(currX - prevX) // 2
            pygame.draw.circle(screen, color, (prevX + radius, prevY + radius), radius, 2)

    for shape_type, shape, shape_color in shapes:
        if shape_type == 'Rect':
            pygame.draw.rect(screen, shape_color, shape, 2)
        elif shape_type == 'Circle':
            cx, cy, radius = shape
            pygame.draw.circle(screen, shape_color, (cx, cy), radius, 2)

    pygame.display.flip()

