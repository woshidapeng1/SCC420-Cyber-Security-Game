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
        basket_texts = self.category.split("\n")
        y = 5
        for basket_text in basket_texts:
            basket_text = font.render(basket_text, True, (255,255,255))
            screen.blit(basket_text, self.rect.move((140 - basket_text.get_width()) // 2-10, (100 - basket_text.get_height()) // 2 + y))
            y += 20


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
        screen.blit(ball_text, self.rect.move((80 - ball_text.get_width()) // 2, (80 - ball_text.get_height()) // 2))
class Select:
    def __init__(self,height,width,font_size,option_gap,options,question):
        

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

        font = pygame.font.SysFont('serial', 40)
        question_text = font.render(self.question, True, BLACK)
        question_rect = question_text.get_rect(left=20, top=self.question_y, width = 350,height = 300)
        self.draw_text(screen, font, self.question, (255,255,255), question_rect)
    def op_2(self,mouse_pos):
        for i in range(len(self.options)):
            option_text = font.render(self.options[i], True, BLACK)
        for i in range(len(self.options)):
            if self.options[i][0] in ["A", "B", "C", "D"]:  
                option_rect_o = option_text.get_rect(left=30, top=self.options_y + i * self.option_gap,width = 30)
                if option_rect_o.collidepoint(mouse_pos):
                    selected_option = i
                        
                  
                    if selected_option == 1:
                        print("Yes！")
                        return 1
                    else:
                        print("No！")
                        pass_num[1] += 1
                        wrong_message_box()
                        pygame.display.flip()
                        pygame.time.delay(1000)
                        self.q()
                        self.draw_op()
    def op_4(self,mouse_pos):
        
        for i in range(len(self.options)):
            option_text = font.render(self.options[i], True, BLACK)
        for i in range(len(self.options)):
            if self.options[i][0] in ["A", "B", "C", "D"]:  
                option_rect_o = option_text.get_rect(left=30, top=self.options_y + i * self.option_gap,width = 30)
                if option_rect_o.collidepoint(mouse_pos):
                    selected_option = i
                        
                  
                    if selected_option == 2:
                        print("Yes！")
                        return 1
                    else:
                        print("No！")
                        pass_num[3] += 1
                        wrong_message_box()
                        pygame.display.flip()
                        pygame.time.delay(1000)
                        self.q()
                        self.draw_op()
    def draw_op(self):
        selected_option = -1
        font = pygame.font.SysFont('serial', 40)
        

        for i in range(len(self.options)):
            option_text = font.render(self.options[i], True, WHITE)
            if self.options[i][0] in ["A", "B", "C", "D"]:  
                option_rect_o = option_text.get_rect(left=25, top=self.options_y-4 + i * self.option_gap,width = 30)
                screen.blit(select_button,option_rect_o)
                # if i == selected_option:
                #     pygame.draw.rect(screen, RED, option_rect_o, 2)
                # else:
                #     pygame.draw.rect(screen, WHITE, option_rect_o, 2)
        for i in range(len(self.options)):
            option_text = font.render(self.options[i], True, WHITE)
            option_rect = option_text.get_rect(left=30, top=self.options_y + i * self.option_gap)  
            screen.blit(option_text, option_rect)
        
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
        word_surface = font.render(self.options, True, (0,0,255))
        # pygame.draw.rect(screen, BLACK, self.L_rect)
        screen.blit(word_surface, self.L_rect)



bg_screen = NewScreen("Cyber Game")

basket1 = Basket(6, 400, "Attacks\n")
basket2 = Basket(140, 400, "Malware\n")
basket3 = Basket(275, 400, "Social\nEngineering")
baskets = [basket1,basket2,basket3]

ball1 = Ball(50, 80, "Trojans",25,False,False)
ball2 = Ball(160, 80, "Ddos",25,False,False)
ball3 = Ball(270, 80, "Phishing",25,False,False)
ball4 = Ball(50, 180, "Spyware",25,False,False)
ball5 = Ball(160, 180, "Spoofing",25,False,False)
ball6 = Ball(270, 180, "Viruses",25,False,False)
ball7 = Ball(50, 280, "Vishing",25,False,False)
ball8 = Ball(160, 280, "SQLi",25,False,False)
ball9 = Ball(270, 280, "Baiting",25,False,False)
balls = [ball1, ball2, ball3, ball4, ball5, ball6, ball7, ball8, ball9]
