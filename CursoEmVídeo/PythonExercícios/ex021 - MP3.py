import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
print('\033[1;31mEnjoy the music!')
while pygame.mixer.music.get_busy():
    pass
