import pygame
import sys
from define import *
from classes import *
question4 = 'which is the ...?'#
options_4 = ["A:  www.example-a.com","B:  www.example-b.com","C:  www.example-c.com","D:  www.example-d.com"]#此处修改第四关界面的选项
Level4_S = Select(SCREEN_HEIGHT,SCREEN_WIDTH,40,50,options_4,question4)
class Level4_2:
    def __init__(self,height,width,font_size,option_gap):
        
   
        self.font_size = font_size
        self.option_gap = option_gap
        self.height = height
        self.width = width
        self.question_y = self.height // 4
        self.options_y = self.height // 2
    def q(self):
        question = "Which one is phishing email"
        
        font = pygame.font.Font('myfont.ttf', 20)
        question_text = font.render(question, True, BLACK)
        question_rect = question_text.get_rect(left=50, top=self.question_y, width = 300,height = 300)
        question_rect.y = 50
        screen.blit(question_text, question_rect)
    def op(self,mouse_pos):
        # global right_rect
        options = {"A": "./level4/A.png",
                   "B": "./level4/B.png",
                    "C": "./level4/C.png",
                    "D": "./level4/D.png"}#
        
        g = 1
        for i in options:
                option_img = pygame.image.load(options[i])
                option_img = pygame.transform.scale(option_img, (150,150))
                for x in range(-100,101,200):
                    for y in range(-100,101,200):
                        option_rect = option_img.get_rect(center=(self.width // 2+x, self.height // 2 + y))
                        if option_rect.collidepoint(mouse_pos):
                            selected_option = g
                            
                            
                            if selected_option == 2:
                                print("Yes！")
                                return 1
                            else:
                                print("No！")
                            pass_num[3] += 1
                        g += 1
        
    def draw_op(self):
        selected_option = -1
        options = {"A": "./level4/A.png",
                   "B": "./level4/B.png",
                    "C": "./level4/C.png",
                    "D": "./level4/D.png"}
        
        # n = 1
        option_rect_L = []
        option_xys = []
        for i in options:
            option_img = pygame.image.load(options[i])
            option_img = pygame.transform.scale(option_img, (150,150))
            for x in range(-80,81,160):
                for y in range(-80,81,160):
                    option_rect_L.append(option_img.get_rect(center=(self.width // 2+x, self.height // 2 + y)))
                    option_xy = pygame.Rect(self.width // 2+x+10,self.height // 2 + y+10,50,50)
                    option_xys.append(option_xy)
            # print('hddddddddddd',option_xys)
        n = 0
        for i in options:
            option_img = pygame.image.load(options[i])
            option_img = pygame.transform.scale(option_img, (150,150))
            i_text = font.render(i,True,WHITE)
            screen.blit(option_img, option_rect_L[n])
            screen.blit(i_text,option_xys[n])
            n+=1
Level4_S2 = Level4_2(SCREEN_HEIGHT,SCREEN_WIDTH,40,50)