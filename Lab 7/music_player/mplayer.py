import pygame, os

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Music Player")

font = pygame.font.Font(r"C:\Users\hp\Downloads\Pixeltype.ttf", 40)

music_dir = "songs"
os.chdir(music_dir)
songs = os.listdir()

is_on = False
current_song = 0

def play_music(song):
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()

running = True
while running:
    screen.fill("Black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                if is_on:
                    pygame.mixer.music.pause()
                    is_on = False
                else:
                    pygame.mixer.music.unpause()
                    is_on = True
            elif event.key == pygame.K_n:
                current_song = (current_song + 1) % len(songs)
                play_music(songs[current_song])
            elif event.key == pygame.K_b:
                current_song = (current_song - 1) % len(songs)
                play_music(songs[current_song])
            elif event.key == pygame.K_e:
                running = False

    text = font.render("Pause or Play, Press P", True, "Red")
    screen.blit(text, (50, 50))
    text = font.render("Next song , Press N", True, "Red")
    screen.blit(text, (50, 100))
    text = font.render("Previous song, Press B (Back)", True, "Red")
    screen.blit(text, (50, 150))
    text = font.render("Exit music player, Press E", True, "Red")
    screen.blit(text, (50, 200))

    pygame.display.flip()

pygame.quit()