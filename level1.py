import pygame
import sys
from classes import *
from define import *

num = 0
level1_d = {"Attacks\n":["Ddos","Spoofing","SQLi"],"Malware\n":["Trojans","Spyware","Viruses"],"Social\nEngineering":["Phishing","Vishing","Baiting"]}

level1_dy = {}
for basket in baskets:
    level1_dy[basket.category] = []
def level1():
    for ball in balls:
        if ball.ball_dragging:
            ball.ball_dragging = False
            break
    
def blit_level1():
    bg_screen.draw()
    basket1.draw()
    basket2.draw()
    basket3.draw()

    for ball in balls:
        if ball.ball_dragging:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            ball.rect.x = mouse_x
            ball.rect.y = mouse_y


    for ball in balls:
        ball.draw()
