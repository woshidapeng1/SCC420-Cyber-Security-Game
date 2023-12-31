import pygame
import sys
from define import *
from classes import *

class Level_31:
    def __init__(self):
        
        self.dialog_width = 150
        self.dialog_height = 465
        self.dialog_width2 = 150
        self.dialog_height2 = 515
        self.input_rect = pygame.Rect(self.dialog_width,self.dialog_height,200,35)
        self.input_rect2 = pygame.Rect(self.dialog_width2,self.dialog_height2,200,35)
    def level3(self,mouse_pos):
        font = pygame.font.Font('myfont.ttf', 15)
        pygame.draw.rect(screen, (255, 255, 255), self.input_rect)
        pygame.draw.rect(screen, (0, 0, 0), self.input_rect, 2)
        pygame.draw.rect(screen, (255, 255, 255), self.input_rect2)
        pygame.draw.rect(screen, (0, 0, 0), self.input_rect2, 2)
        user_website = ""
        user_phone_number = ""
        # correct_website = "https://www.sainsburys.co.uk/shop/gb/groceries"
        # correct_website = 'sainsburys'
        correct_website = 'sainsbury'
        # correct_phone_number = "193746825"
        correct_phone_number = '193'
        # active_in = True
        running = True
        while running:
            
            for event in pygame.event.get():
                mouse_pos = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        
                        
                        if user_website == correct_website and user_phone_number == correct_phone_number:
                            pass_num[2] += 1
                            over_message_box(messages[0],pass_num[2])
                            pygame.time.delay(2000)
                            pygame.display.flip()
                            running = False
                            
                        else:
                            pass_num[2] += 1
                            wrong_message_box()
                            pygame.display.flip()
                            pygame.time.delay(1000)
                            bg_screen.draw(level_3_pic)
                            self.draw_level3()
                            user_website = ""
                            user_phone_number = ""
                            
                    elif event.key == pygame.K_BACKSPACE:
                        
                        if user_website != '' and (mouse_pos[0]>self.input_rect2.x and mouse_pos[0]<(self.input_rect2.x+self.dialog_width)) and (mouse_pos[1]>self.input_rect2.y and mouse_pos[1]<(self.input_rect2.y+self.dialog_height)):
                            user_website = user_website[:-1]
                        elif user_phone_number != '' and (mouse_pos[0]>self.input_rect.x and mouse_pos[0]<(self.input_rect.x+self.dialog_width2)) and (mouse_pos[1]>self.input_rect.y and mouse_pos[1]<(self.input_rect.y+self.dialog_height2)):
                            user_phone_number = user_phone_number[:-1]
                    else:
                        if check_button_click(mouse_pos,self.input_rect2):
                            user_website += event.unicode
                        if check_button_click(mouse_pos,self.input_rect):
                            user_phone_number += event.unicode
            pygame.draw.rect(screen, (255, 255, 255), self.input_rect)
            pygame.draw.rect(screen, (0, 0, 0), self.input_rect, 2)
            pygame.draw.rect(screen, (255, 255, 255), self.input_rect2)
            pygame.draw.rect(screen, (0, 0, 0), self.input_rect2, 2)
            website_text = font.render(user_website, True, (0,0,0))
            website_rect = website_text.get_rect(center = self.input_rect2.center)
            phone_number_text = font.render(user_phone_number, True, (0,0,0))
            phone_number_rect = phone_number_text.get_rect(center=self.input_rect.center)
            screen.blit(website_text, website_rect)
            screen.blit(phone_number_text, phone_number_rect)
            pygame.display.flip()
    def draw_text(self,screen, font, text, color, rect, aa=False, bkg=None):
        rect = pygame.Rect(rect)
        y = rect.top
        line_spacing = -2

        # 
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

    def draw_level3(self):
        
        font = pygame.font.Font('myfont.ttf', 16)
            
        # level3()
        # encrypted_text = "moT raeD\n seirecorg/bg/pohs/ku.oc.syrubsnias\n.www//:sptth : knil eht si ereH\n !noitamrofni reffO cificepS remmuS weiv\n ot etisbew ruo tisiv nac uoY !elas no\n smeti erom evah dna slaicepS remmuS ruo\n dehcnual yltnecer eW.sreffo laiceps s'ynapmoc\n ruo ot gnibircsbus rof uoy knahT\n .528647391 ta enohpelet ro liame yb su tcatnoc ot\n eerf leef esaelp ,snoitseuq yna evah uoy\nfIsehsiW\ntseB ymmiJ"
        # 
        # text_rect = pygame.Rect(40, 55, SCREEN_WIDTH-20, SCREEN_HEIGHT-50)

        # 
        # self.draw_text(screen, font, encrypted_text, (0,0,0), text_rect)
        website_text = font.render("Company", True, (0, 0, 0))
        phone_number_title = font.render("PhoneNumber ", True, (0, 0, 0))
        screen.blit(website_text, (40, 520))
        screen.blit(phone_number_title, (40, 470))
        dialog_width = 150
        dialog_height = 465

        dialog_width2 = 150
        dialog_height2 = 515
        font = pygame.font.Font('myfont.ttf', 15)
        input_rect = pygame.Rect(dialog_width,dialog_height, 200,35)
        pygame.draw.rect(screen, (255, 255, 255), input_rect)
        pygame.draw.rect(screen, (0, 0, 0), input_rect, 2)

        input_rect2 = pygame.Rect(dialog_width2,dialog_height2,200,35)
        pygame.draw.rect(screen, (255, 255, 255), input_rect2)
        pygame.draw.rect(screen, (0, 0, 0), input_rect2, 2)
        pygame.display.flip()
Level_3S_2 = Level_31()