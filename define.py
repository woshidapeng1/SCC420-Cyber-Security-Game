import pygame
import sys

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
BUTTON_WIDTH = 220
BUTTON_HEIGHT = 80
BUTTON_MARGIN = 20
BACKB_HEIGHT = 50
BACKB_WIDTH = 50
START_WIDTH = 100
START_HEIGHT = 50
STAR_WIDTH = 50
STAR_HEIGHT = 50
FONT_SIZE = 50

game_name = 'CYBER GAME'
over_name = 'END'

levels = ["Level 1", "Level 2", "Level 3", "Level 4", "Level 5"]
level_pass = {"Level 1":True, "Level 2":False, "Level 3":False, "Level 4":False, "Level 5":False}
game_states = ['hint1','hint2','hint3','hint4','hint5']
pass_state = ['start1','start2','start3','start4','start5']
pass_num = [0,0,0,0,0]
pass_yes = [0,0,0,0,0]
Level4_S2_pass = {0:False, 1:False, 2:False, 3:False}

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)

select_ball = None
wrong_message = False

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Cyber Game")
hint_text = 'This is the hint . . . .. . . . . .........................'
about_text = 'This is about some some, , , , , , , , , , , ,  , , , , ,  ,'


background_img = pygame.image.load("./bgpic/bg_0.jpg")
bg_1 = pygame.image.load("./bgpic/bg_1.jpg")
bg_2 = pygame.image.load("./bgpic/bg_2.jpg")
bg_3 = pygame.image.load("./bgpic/bg_3.jpg")
bg_4 = pygame.image.load("./bgpic/bg_4.jpg")
bg_5 = pygame.image.load("./bgpic/bg_5.jpg")
play_button_img = pygame.image.load("./bgpic/bt.png")
back_button_img = pygame.image.load('./bgpic/back.png')
start_button_img = pygame.image.load('./bgpic/sta.png')
lan_img = pygame.image.load('./bgpic/lan.png')
ball_img = pygame.image.load('./bgpic/ball.png')
star_img = pygame.image.load('./bgpic/star.png')
level_3_pic = pygame.image.load('./level3/email.png')
yes_no_button = pygame.image.load('./bgpic/yes_no_button.png')
select_button = pygame.image.load('./bgpic/select.png')

background_img = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
bg_1 = pygame.transform.scale(bg_1, (SCREEN_WIDTH, SCREEN_HEIGHT))
bg_2 = pygame.transform.scale(bg_2, (SCREEN_WIDTH, SCREEN_HEIGHT))
bg_3 = pygame.transform.scale(bg_3, (SCREEN_WIDTH, SCREEN_HEIGHT))
bg_4 = pygame.transform.scale(bg_4, (SCREEN_WIDTH, SCREEN_HEIGHT))
bg_5 = pygame.transform.scale(bg_5, (SCREEN_WIDTH, SCREEN_HEIGHT))
level_3_pic = pygame.transform.scale(level_3_pic, (SCREEN_WIDTH, SCREEN_HEIGHT))

play_button_img = pygame.transform.scale(play_button_img, (BUTTON_WIDTH, BUTTON_HEIGHT))
back_button_img = pygame.transform.scale(back_button_img,(BACKB_WIDTH,BACKB_HEIGHT))
start_button_img = pygame.transform.scale(start_button_img,(START_WIDTH,START_HEIGHT))
lan_img = pygame.transform.scale(lan_img, (115,180))
ball_img = pygame.transform.scale(ball_img, (80,80))
star_button_img = pygame.transform.scale(star_img,(STAR_WIDTH,STAR_HEIGHT))
yes_no_button = pygame.transform.scale(yes_no_button,(100,50))
select_button = pygame.transform.scale(select_button,(30,30))


play_button_rect = play_button_img.get_rect()
play_button_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 )
hint_button_rect = play_button_img.get_rect()
hint_button_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + BUTTON_HEIGHT + BUTTON_MARGIN)
about_button_rect = play_button_img.get_rect()
about_button_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 2 * BUTTON_HEIGHT + 2 * BUTTON_MARGIN)
back_button_rect = back_button_img.get_rect()
back_button_rect.bottomright = (SCREEN_WIDTH,SCREEN_HEIGHT)
start_button_rect = start_button_img.get_rect()
start_button_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 3 * (START_HEIGHT + BUTTON_MARGIN))
star_button_rect = star_button_img.get_rect()
star_button_rect.center = (SCREEN_WIDTH // 2 - BUTTON_HEIGHT - BUTTON_MARGIN, SCREEN_HEIGHT // 2)
# star_button_rect.center = (100,100)

font = pygame.font.SysFont('myfont.ttf', FONT_SIZE)
font2 = pygame.font.Font('myfont.ttf', FONT_SIZE)
game_name = font2.render(game_name,True,WHITE)
game_name_rect = game_name.get_rect()
game_name_rect.center = (SCREEN_WIDTH // 2,150)

over_name = font2.render(over_name,True,WHITE)
over_name_rect = over_name.get_rect()
over_name_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

def draw_text(screen, font, text, color, rect, aa=False, bkg=None):
    font = pygame.font.Font('myfont.ttf', 15)
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

def over_message_box(message,pn):
    messagebox_width = 300
    messagebox_height = 150
    messagebox_x = (SCREEN_WIDTH - messagebox_width) // 2
    messagebox_y = (SCREEN_HEIGHT - messagebox_height) // 2

    pygame.draw.rect(screen, (173, 216, 230), (messagebox_x, messagebox_y, messagebox_width, messagebox_height))
    pygame.draw.rect(screen, (0, 0, 0), (messagebox_x, messagebox_y, messagebox_width, messagebox_height), 2)

    font = pygame.font.Font('coolvetica.ttf', 30)
    text_surface = font.render(message, True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

    screen.blit(text_surface, text_rect)
    if pn <= 1:
        for x in range(123,264,50):
            screen.blit(star_button_img, (x,310))
    elif pn > 1 and pn < 3:
        for x in range(140,241,70):
            screen.blit(star_button_img, (x,310))
    else:
        screen.blit(star_button_img, (175,310))

    pygame.display.flip()
def wrong_message_box():
    message = 'Wrong'
    messagebox_width = 300
    messagebox_height = 150
    messagebox_x = (SCREEN_WIDTH - messagebox_width) // 2
    messagebox_y = (SCREEN_HEIGHT - messagebox_height) // 2

    pygame.draw.rect(screen, (173, 216, 230), (messagebox_x, messagebox_y, messagebox_width, messagebox_height))
    pygame.draw.rect(screen, (0, 0, 0), (messagebox_x, messagebox_y, messagebox_width, messagebox_height), 2)

    font = pygame.font.Font('coolvetica.ttf', 30)
    text_surface = font.render(message, True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

    screen.blit(text_surface, text_rect)

def le_me(SCREEN_WIDTH,BUTTON_WIDTH,SCREEN_HEIGHT,BUTTON_HEIGHT,BUTTON_MARGIN):
   
    game_state = "menu"  
    
    levels = ["Level 1", "Level 2", "Level 3", "Level 4", "Level 5", "Level 6"]
    level_buttons_rect = []
    for i in range(len(levels)):
        button_rect = pygame.Rect(SCREEN_WIDTH // 2 - BUTTON_WIDTH // 2,
                                (SCREEN_HEIGHT // 2 - (BUTTON_HEIGHT * (len(levels) // 2) + BUTTON_MARGIN * ((len(levels) // 2))))
                                + (BUTTON_HEIGHT + BUTTON_MARGIN) * (i+0.5),
                                BUTTON_WIDTH, BUTTON_HEIGHT)
        level_buttons_rect.append(button_rect)
    return level_buttons_rect


level_buttons_rect = le_me(SCREEN_WIDTH,BUTTON_WIDTH,SCREEN_HEIGHT,BUTTON_HEIGHT,BUTTON_MARGIN)

def check_button_click(mouse_pos, button_rect):
    if button_rect.collidepoint(mouse_pos):
        return True
    return False


hint_text_rect = pygame.Rect(30,230,340,350)
messages = ['WELL DONE','GAME OVER']

