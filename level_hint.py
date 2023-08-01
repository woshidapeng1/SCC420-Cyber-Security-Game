import pygame
import sys
from define import *

pe_img_width = 150
pe_img_height = 350
re_img_width = 200
re_img_height = 200
class LEVEL_HINT:
    def __init__(self, x, y, te, pe_img,re_img,color):
        self.rect = pygame.Rect(x, y, 50, 50)
        self.x = x
        self.y = y
        self.te = te
        self.pe_img = pe_img
        self.re_img = re_img
        self.color = color
    def draw_pic(self):
        pe_img = pygame.transform.scale(self.pe_img, (pe_img_width,pe_img_height))
        re_img = pygame.transform.scale(self.re_img, (re_img_width,re_img_height))
        pe_rect = pe_img.get_rect()
        re_rect = re_img.get_rect()
        pe_rect.center = (80, 253)
        re_rect.center = (SCREEN_WIDTH//2,SCREEN_HEIGHT//2+40)
        screen.blit(pe_img,pe_rect)
        screen.blit(re_img,re_rect)

pe_img = pygame.image.load('./bgpic/pe.png')
re_img = pygame.image.load('./bgpic/re.png')
Level1_hint_text_L =["    In this level, you need to categorize all the balls and place \
    them into their corresponding baskets. Once you classify them correctly, you can pass the level!.",
    "    In this level, you need to categorize all the balls and place \
    them into their corresponding baskets. Once you classify them correctly, you can pass the level!.",
    "    In this level, you need to categorize all the balls and place \
    them into their corresponding baskets. Once you classify them correctly, you can pass the level!.",
    "    In this level, you need to categorize all the balls and place \
    them into their corresponding baskets. Once you classify them correctly, you can pass the level!.",
    "    In this level, you need to categorize all the balls and place \
    them into their corresponding baskets. Once you classify them correctly, you can pass the level!."]  
#此处修改关卡前提示页面的说明，上个列表中包含五项完全相同的内容
def Le_Hint(Level1_hint_text):
    
    Level1_hint = LEVEL_HINT(350, 30, Level1_hint_text, pe_img,re_img,BLACK)
    Level1_hint.draw_pic()
    