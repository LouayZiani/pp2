import pygame
import sys
from pygame.locals import *
import random
import time

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINS_COLLECTED = 0

font = pygame.font.Font(r"C:\Users\hp\Downloads\pygame project\Pixeltype.ttf", 60)
font_small = pygame.font.Font(r"C:\Users\hp\Downloads\pygame project\Pixeltype.ttf", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load(r"C:\Users\hp\Desktop\PP2\Lab 9\Racer\AnimatedStreet.png")

DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\hp\Desktop\PP2\Lab 9\Racer\Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.bottom > 600:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Coin(pygame.sprite.Sprite):
    def __init__(self, coin_image, coin_type):
        super().__init__()
        self.image = pygame.image.load(coin_image)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        self.coin_type = coin_type

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.bottom > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\hp\Desktop\PP2\Lab 9\Racer\Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)


P1 = Player()
E1 = Enemy()
enemies = pygame.sprite.Group()
enemies.add(E1)
all_enemy_sprites = pygame.sprite.Group() 
all_enemy_sprites.add(E1)

new_coin_images = [r"C:\Users\hp\Desktop\PP2\Lab 9\Racer\new_coin1.png", r"C:\Users\hp\Desktop\PP2\Lab 9\Racer\new_coin2.png"]

coins = pygame.sprite.Group()
all_coin_sprites = pygame.sprite.Group()  

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

pygame.mixer.music.load(r"C:\Users\hp\Desktop\PP2\Lab 9\Racer\background.wav")
pygame.mixer.music.play(-1)  

while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if random.randint(0, 200) < 3:
        new_coin = Coin(r"C:\Users\hp\Desktop\PP2\Lab 9\Racer\coin.png", "normal")
        coins.add(new_coin)
        all_coin_sprites.add(new_coin)
    elif random.randint(0, 50) < 1:
        new_coin = Coin(r"C:\Users\hp\Desktop\PP2\Lab 9\Racer\new_coin1.png", "ncoin")
        coins.add(new_coin)
        all_coin_sprites.add(new_coin)
    elif random.randint(0, 50) < 1:
        new_coin = Coin(r"C:\Users\hp\Desktop\PP2\Lab 9\Racer\new_coin2.png", "wcoin")
        coins.add(new_coin)
        all_coin_sprites.add(new_coin)

    DISPLAYSURF.blit(background, (0, 0))
    scores = font_small.render(str(SCORE), True, BLACK)
    coins_collected_text = font_small.render(
        "Coins: " + str(COINS_COLLECTED), True, BLACK
    )
    DISPLAYSURF.blit(scores, (10, 10))
    DISPLAYSURF.blit(coins_collected_text, (300, 10))

    for entity in all_enemy_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)

    for entity in all_coin_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)

    P1.move()
    DISPLAYSURF.blit(P1.image, P1.rect)

    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound(r"C:\Users\hp\Desktop\PP2\Lab 9\Racer\crash.wav").play()
        time.sleep(1)

        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))

        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    for coin in pygame.sprite.spritecollide(P1, coins, True):
        if coin.coin_type == "ncoin":
            SPEED += 1 
        elif coin.coin_type == "wcoin":
            SPEED -= 1
        COINS_COLLECTED += 1

    pygame.display.update()
    FramePerSec.tick(FPS)
