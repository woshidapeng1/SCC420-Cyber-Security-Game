import pygame
import sys
from define import *
from classes import *
question4 = 'which is the Fake Websit?'
options_4 = ["A:  www.samsung.com/uk","B:  www.google.com","C:  www.applle.com","D:  www.amazon.co.uk"]
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
        question = " Is this a phishing email?"
        
        font = pygame.font.Font('myfont.ttf', 20)
        question_text = font.render(question, True, WHITE)
        question_rect = question_text.get_rect(left=50, top=self.question_y, width = 300,height = 300)
        question_rect.y = 50
        screen.blit(question_text, question_rect)
    
    def draw_op(self,pic):
        option_img = pygame.image.load(pic)
        option_img = pygame.transform.scale(option_img, (400,250))
        option_rect = option_img.get_rect(center=(self.width // 2, self.height // 2))
        screen.blit(option_img, option_rect)
       
        no_text = font.render("YES", True, WHITE)
        no_text_rect = no_text.get_rect(center=(100, 525))
      
        yes_text = font.render("NO", True, WHITE)
        yes_text_rect = no_text.get_rect(center=(275,525))
       
        no_button_rect = pygame.Rect(50, 500, 100, 50)
        self.no_button_rect = no_button_rect
        pygame.draw.rect(screen, (0, 0, 0), no_button_rect)
        screen.blit(yes_no_button,(50,500))
        screen.blit(no_text, no_text_rect)

        
        yes_button_rect = pygame.Rect(225, 500, 100, 50)
        self.yes_button_rect = yes_button_rect
        pygame.draw.rect(screen, (0, 0, 0), yes_button_rect)
        screen.blit(yes_no_button,(225,500))
        screen.blit(yes_text, yes_text_rect)
    def check(self,mouse_pos):
        if self.no_button_rect.collidepoint(mouse_pos):
            return 1
        elif self.yes_button_rect.collidepoint(mouse_pos):
            pass_num[3] += 1
            wrong_message_box()
            pygame.display.flip()
            pygame.time.delay(1000)
            return 0
        
Level4_S2 = Level4_2(SCREEN_HEIGHT,SCREEN_WIDTH,40,50)
options = ["./level4/No1.png",
           "./level4/No2.png",
           "./level4/No3.png",
           "./level4/No4.png"]   #修改第四关的四个图片