import pygame
#Reproduza um som mp3.

pygame.init()
pygame.mixer.music.load('musicaloka.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()