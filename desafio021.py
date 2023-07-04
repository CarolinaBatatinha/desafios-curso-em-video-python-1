#Faça um programa em Python que abra e reproduza o áudio de um arquivo mp3.

#PESQUISAR NO PYPI.ORG

import pygame

pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()