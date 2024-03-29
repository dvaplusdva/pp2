import pygame
from pygame import mixer


pygame.init()


screen = pygame.display.set_mode((800, 600))


mixer.init()


music_files = ['song1.mp3', 'song2.mp3', 'song3.mp3']


current_index = 0


mixer.music.load(music_files[current_index])


is_playing = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if is_playing:
                    mixer.music.pause()
                else:
                    mixer.music.unpause()
                is_playing = not is_playing

            elif event.key == pygame.K_s:
                mixer.music.stop() 
                is_playing = False

            elif event.key == pygame.K_n:
                current_index = (current_index + 1) % len(music_files)
                mixer.music.load(music_files[current_index])
                mixer.music.play()
                is_playing = True

            elif event.key == pygame.K_p: 
                current_index = (current_index - 1) % len(music_files)
                mixer.music.load(music_files[current_index])
                mixer.music.play()
                is_playing = True