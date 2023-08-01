import pygame
import sys
from define import *
# from level5 import draw_text

class NewScreen:
    def __init__(self, title):
        self.title = title
        pygame.display.set_caption(self.title)

    def draw_bg(self,bg_img):
        screen.fill(WHITE)
        screen.blit(bg_img, (0, 0))
        screen.blit(game_name,game_name_rect)
        screen.blit(play_button_img, play_button_rect)
        screen.blit(play_button_img, hint_button_rect)
        screen.blit(play_button_img, about_button_rect)

    def draw_char(self):
        play_text = font.render("Play", True, (255,255,255))
        hint_text = font.render("Hint", True, (255,255,255))
        about_text = font.render("About", True, (255,255,255))
        screen.blit(play_text, play_button_rect.move((BUTTON_WIDTH - play_text.get_width()) // 2, (BUTTON_HEIGHT - play_text.get_height()) // 2))
        screen.blit(hint_text, hint_button_rect.move((BUTTON_WIDTH - hint_text.get_width()) // 2, (BUTTON_HEIGHT - hint_text.get_height()) // 2))
        screen.blit(about_text, about_button_rect.move((BUTTON_WIDTH - about_text.get_width()) // 2, (BUTTON_HEIGHT - about_text.get_height()) // 2))

    def draw(self,bg_img):
        screen.fill(WHITE)
        screen.blit(bg_img, (0, 0))
        
class Basket:
    def __init__(self, x, y, category):
        
        self.rect = pygame.Rect(x, y, 130, 100)
        self.category = category
        

    def draw(self):        
        screen.blit(lan_img,self.rect)
        font = pygame.font.SysFont('宋体', 30)
        basket_text = font.render(self.category, True, (255,255,255))
        screen.blit(basket_text, self.rect.move((130 - basket_text.get_width()) // 2, (100 - basket_text.get_height()) // 2))
        


class Ball:
    def __init__(self, x, y, category,radius,ball_dragging,ball_in):
        self.rect = pygame.Rect(x, y, 50, 50)
        self.x = x
        self.y = y
        self.category = category
        self.radius = radius
        self.ball_dragging = ball_dragging
        self.ball_in = ball_in

    def draw(self):
        
        screen.blit(ball_img,self.rect)
        font = pygame.font.SysFont('宋体', 20)
        ball_text = font.render(self.category, True, (255,255,255))
        screen.blit(ball_text, self.rect.move((50 - ball_text.get_width()) // 2, (50 - ball_text.get_height()) // 2))
class Select:
    def __init__(self,height,width,font_size,option_gap,options,question):
        
    # 题目和选项的文本和布局信
        self.font_size = font_size
        self.option_gap = option_gap
        self.height = height
        self.width = width
        self.question_y = self.height // 4
        self.options_y = self.height // 2
        self.options = options
        self.question = question
    def draw_text(self, screen, font, text, color, rect, aa=False, bkg=None):
        font = pygame.font.SysFont('serial', 40)
        rect = pygame.Rect(rect)
        y = rect.top
        line_spacing = -2
        

        # 逐行绘制文字
        for line in text.split("\n"):
            while line:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                i = 1
                if y + font.size(line)[1] > rect.bottom+25:
                    break
                while font.size(line[:i])[0] < rect.width and i < len(line):
                    i += 1
                if i < len(line):
                    i = line.rfind(" ", 0, i) + 1
                if bkg:
                    image = font.render(line[:i], aa, color, bkg)
                    image.set_colorkey(bkg)
                else:
                    image = font.render(line[:i], aa, color)
                screen.blit(image, (rect.left, y))
                y += font.size(line)[1] + line_spacing
                line = line[i:]
    def q(self):
        # 绘制题目
        font = pygame.font.SysFont('serial', 50)
        question_text = font.render(self.question, True, BLACK)
        question_rect = question_text.get_rect(left=20, top=self.question_y, width = 350,height = 300)
        self.draw_text(screen, font, self.question, (0,0,0), question_rect)
    def op_2(self,mouse_pos):
        for i in range(len(self.options)):
            option_text = font.render(self.options[i], True, BLACK)
        for i in range(len(self.options)):
            if self.options[i][0] in ["A", "B", "C", "D"]:  # 仅针对ABCD选项绘制选中框
                option_rect_o = option_text.get_rect(left=30, top=self.options_y + i * self.option_gap,width = 30)
                if option_rect_o.collidepoint(mouse_pos):
                    selected_option = i
                        
                    # 检查选择是否正确
                    if selected_option == 1:
                        print("回答正确！")
                        return 1
                    else:
                        print("回答错误！")
    def op_4(self,mouse_pos):
        for i in range(len(self.options)):
            option_text = font.render(self.options[i], True, BLACK)
        for i in range(len(self.options)):
            if self.options[i][0] in ["A", "B", "C", "D"]:  # 仅针对ABCD选项绘制选中框
                option_rect_o = option_text.get_rect(left=30, top=self.options_y + i * self.option_gap,width = 30)
                if option_rect_o.collidepoint(mouse_pos):
                    selected_option = i
                        
                    # 检查选择是否正确
                    if selected_option == 2:
                        print("回答正确！")
                        return 1
                    else:
                        print("回答错误！")
    def draw_op(self):
        selected_option = -1
        # 绘制选项文本
        for i in range(len(self.options)):
            option_text = font.render(self.options[i], True, BLACK)
            option_rect = option_text.get_rect(left=30, top=self.options_y + i * self.option_gap)  # 使文本左对齐
            screen.blit(option_text, option_rect)
        
        # 绘制选中框
        for i in range(len(self.options)):
            if self.options[i][0] in ["A", "B", "C", "D"]:  # 仅针对ABCD选项绘制选中框
                option_rect_o = option_text.get_rect(left=30, top=self.options_y + i * self.option_gap,width = 30)
                if i == selected_option:
                    pygame.draw.rect(screen, GREEN, option_rect_o, 2)
                else:
                    pygame.draw.rect(screen, BLACK, option_rect_o, 2)
class Level_5:
    def __init__(self,x,y,options,w_dragging,text_in):
        self.L_rect = pygame.Rect(x,y,200,25)
        self.x = x
        self.y = y
        self.options = options
        self.w_dragging = w_dragging
        self.text_in = text_in
    def draw_op(self):
        font = pygame.font.Font('myfont.ttf', 15)
        word_surface = font.render(self.options, True, (255,255,255))
        # pygame.draw.rect(screen, BLACK, self.L_rect)
        screen.blit(word_surface, self.L_rect)


# 创建主界面和提示界面对象
bg_screen = NewScreen("游戏主界面")

basket1 = Basket(1, 400, 'animals')
basket2 = Basket(135, 400, "fruits")
basket3 = Basket(270, 400, "tools")
baskets = [basket1,basket2,basket3]


ball1 = Ball(60, 200, "apple",25,False,False)
ball2 = Ball(135, 200, "dog",25,False,False)
ball3 = Ball(210, 200, "hammer",25,False,False)
ball4 = Ball(285, 200, "orange",25,False,False)
ball5 = Ball(60, 300, "cat",25,False,False)
ball6 = Ball(135, 300, "banana",25,False,False)
ball7 = Ball(210, 300, "saw",25,False,False)
ball8 = Ball(285, 300, "bird",25,False,False)
balls = [ball1, ball2, ball3, ball4, ball5, ball6, ball7, ball8]
