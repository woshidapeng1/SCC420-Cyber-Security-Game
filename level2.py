import pygame
from define import *
from classes import *
import re
question2 = " Which Password is the Strongest? "
options_2 = ["A  Password1", "B Pass1Word#!", "C  password", "D  Password123"]
Level2_S = Select(SCREEN_HEIGHT,SCREEN_WIDTH,40,50,options_2,question2)

password_pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$')
def show_password_input():

    dialog_width = 300
    dialog_height = 400
    dialog_x = (SCREEN_WIDTH - dialog_width) // 2
    dialog_y = (SCREEN_HEIGHT - dialog_height) // 2

    mes_pic = pygame.image.load("./bgpic/level_2_mes.jpg")
    mes_pic = pygame.transform.scale(mes_pic, (dialog_width, dialog_height))

    # pygame.draw.rect(screen, (173, 216, 230), (dialog_x, dialog_y, dialog_width, dialog_height))
    pygame.draw.rect(screen, (0, 0, 0), (dialog_x, dialog_y, dialog_width, dialog_height), 2)
    screen.blit(mes_pic,(dialog_x, dialog_y))

    font = pygame.font.Font('myfont.ttf', 30)
    title_text = font.render("Try A Stronger Password", True, (0, 0, 0))
    title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, dialog_y + 100))

    input_rect = pygame.Rect(dialog_x + 50, dialog_y + 250, dialog_width - 100, 40)
    pygame.draw.rect(screen, (255, 255, 255), input_rect)
    pygame.draw.rect(screen, (0, 0, 0), input_rect, 2)

    pygame.display.flip()

    password = ""
    input_active = True
    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if password_pattern.match(password):
                        pass_num[1] += 1
                        over_message_box(messages[0],pass_num[1])
                        pygame.time.delay(2000)
                        pygame.display.flip()
                        input_active = False
                        break
                        
                        
                    else:
                        # show_message_box("False")
                        pass_num[1] += 1
                        wrong_message_box()
                        pygame.display.flip()
                        pygame.time.delay(1000)
                        screen.blit(mes_pic,(dialog_x, dialog_y))
                        password = ""
                    # input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    password = password[:-1]
                else:
                    password += event.unicode

        pygame.draw.rect(screen, (255, 255, 255), input_rect)
        pygame.draw.rect(screen, (0, 0, 0), input_rect, 2)

        text_surface = font.render(password, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=input_rect.center)
        screen.blit(text_surface, text_rect)

        screen.blit(title_text, title_rect)

        pygame.display.flip()

def show_message_box(message):
    messagebox_width = 300
    messagebox_height = 150
    messagebox_x = (SCREEN_WIDTH - messagebox_width) // 2
    messagebox_y = (SCREEN_HEIGHT - messagebox_height) // 2

    # pygame.draw.rect(screen, (173, 216, 230), (messagebox_x, messagebox_y, messagebox_width, messagebox_height))
    
    pygame.draw.rect(screen, (0, 0, 0), (messagebox_x, messagebox_y, messagebox_width, messagebox_height), 2)
    

    font = pygame.font.Font('coolvetica.ttf', 30)
    text_surface = font.render(message, True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

    screen.blit(text_surface, text_rect)

    pygame.display.flip()
