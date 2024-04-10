import pygame
import math

pygame.init()

# rhombus --> losange

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
drawType = 'r'
color = "Red"
shapes = [] 

font = pygame.font.Font(r"C:\Users\hp\Downloads\pygame project\Pixeltype.ttf", 30)

def calculate_rect(x1, x2, y1, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

def draw_square(x1, y1, x2, y2):
    width = abs(x2 - x1)
    height = abs(y2 - y1)
    size = min(width, height)
    if x2 < x1:
        x1 -= size
    if y2 < y1:
        y1 -= size
    return pygame.Rect(x1, y1, size, size)

def draw_right_triangle(x1, y1, x2, y2):
    return [(x1, y1), (x1, y2), (x2, y2)]


def draw_equilateral_triangle(x1, y1, x2, y2):
    base = abs(x2 - x1)
    height = base * math.sqrt(3) / 2
    return [(x1, y2), ((x1 + x2) // 2, y1), (x2, y2)]

def draw_rhombus(x1, y1, x2, y2):
    cx = (x1 + x2) // 2
    cy = (y1 + y2) // 2
    width = abs(x2 - x1)
    height = abs(y2 - y1)
    return [(cx - width // 2, cy), (cx, cy - height // 2), (cx + width // 2, cy), (cx, cy + height // 2)]

def get_bounding_rect(points):
    x_values = [p[0] for p in points]
    y_values = [p[1] for p in points]
    x_min, x_max = min(x_values), max(x_values)
    y_min, y_max = min(y_values), max(y_values)
    return pygame.Rect(x_min, y_min, x_max - x_min, y_max - y_min)

def check_collision(x, y):
    for shape_type, shape, _ in shapes:
        if shape_type == 'r' or shape_type == 'c':
            if shape_type == 'r' and shape.collidepoint(x, y):
                shapes.remove((shape_type, shape, _))
                return True
            elif shape_type == 'c':
                cx, cy, radius = shape
                if (x - cx)**2 + (y - cy)**2 <= radius**2:
                    shapes.remove((shape_type, shape, _))
                    return True
        elif shape_type == 'p':
            bounding_rect = get_bounding_rect(shape)
            if bounding_rect.collidepoint(x, y):
                shapes.remove((shape_type, shape, _))
                return True
    return False


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
            if drawType == 'r':
                shapes.append(('r', calculate_rect(prevX, currX, prevY, currY), color))
            elif drawType == 'c':
                radius = abs(currX - prevX) // 2
                shapes.append(('c', (prevX + radius, prevY + radius, radius), color))
            elif drawType == 'e':
                check_collision(currX, currY)
            elif drawType == 's':
                shapes.append(('r', draw_square(prevX, prevY, currX, currY), color))
            elif drawType == 't':
                shapes.append(('p', draw_right_triangle(prevX, prevY, currX, currY), color))
            elif drawType == 'p':
                shapes.append(('p', draw_equilateral_triangle(prevX, prevY, currX, currY), color))
            elif drawType == 'h':
                shapes.append(('p', draw_rhombus(prevX, prevY, currX, currY), color))

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                drawType = 'r'  # Switch to drawing rectangles
            elif event.key == pygame.K_c:
                drawType = 'c'  # Switch to drawing circles
            elif event.key == pygame.K_e:
                drawType = 'e'  # Switch to eraser
            elif event.key == pygame.K_y:
                color = "Yellow"
            elif event.key == pygame.K_b:
                color = "Blue"
            elif event.key == pygame.K_g:
                color = "Green"
            elif event.key == pygame.K_a:
                color = "Red"
            elif event.key == pygame.K_s:
                drawType = 's'
            elif event.key == pygame.K_t:
                drawType = 't'
            elif event.key == pygame.K_p:
                drawType = 'p'
            elif event.key == pygame.K_h:
                drawType = 'h'

    screen.fill("Black")  # arrière-plan
    
    text = [
               "Yellow = Y",
               "Blue = B",
               "Green = G",
               "Z = Red",
               "-----------------",
               "R = Rectangle",
               "C = Circle",
               "E = Eraser",
               "-----------------",
               "S = Square",
               "T = Right Triangle",
               "P = Equilateral Triangle",
               "H = Rhombus"
    ]
    for i, text in enumerate(text):
        text_surface = font.render(text, False, "Gold")
        screen.blit(text_surface, (10, 10 + i * 20))
    
    if LMBPressed:
        if drawType == 'r':
            temp_rect = calculate_rect(prevX, currX, prevY, currY)
            pygame.draw.rect(screen, color, temp_rect, 2)
        elif drawType == 'c':
            radius = abs(currX - prevX) // 2
            pygame.draw.circle(screen, color, (prevX + radius, prevY + radius), radius, 2)
        elif drawType == 's':
            temp_square = draw_square(prevX, prevY, currX, currY)
            pygame.draw.rect(screen, color, temp_square, 2)
        elif drawType == 't':
            temp_triangle = draw_right_triangle(prevX, prevY, currX, currY)
            pygame.draw.polygon(screen, color, temp_triangle, 2)
        elif drawType == '3':
            temp_rhombus = draw_rhombus(prevX, prevY, currX, currY)
            pygame.draw.polygon(screen, color, temp_rhombus, 2)
        elif drawType == '2':
            temp_etriangle = draw_equilateral_triangle(prevX, prevY, currX, currY)
            pygame.draw.polygon(screen, color, temp_etriangle, 2)

    for shape_type, shape, shape_color in shapes:
        if shape_type == 'r':
            pygame.draw.rect(screen, shape_color, shape, 2)
        elif shape_type == 'c':
            cx, cy, radius = shape
            pygame.draw.circle(screen, shape_color, (cx, cy), radius, 2)
        elif shape_type == 'p':
            pygame.draw.polygon(screen, shape_color, shape, 2)
    pygame.display.flip()