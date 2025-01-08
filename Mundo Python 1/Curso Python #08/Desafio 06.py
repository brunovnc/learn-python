# Faça um programa que abra e reproduza o áudio de um arquivo MP3.
from pygame import mixer

mixer.init()

mixer.music.load('oloco.mp3')
mixer.music.play()
x = input('Digite algo para parar a música... ')