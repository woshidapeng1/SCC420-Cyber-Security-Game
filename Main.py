
import pygame
import Menu
from LevelMenu import LevelMenu
from QA import QAMenu
from AboutMe import AboutMeMenu



def main():
    pygame.init()


    screen = pygame.display.set_mode((640,480))

    pygame.display.set_caption('Cyber Security Game')

    # button
    button_width = 240
    button_height = 60
    button_color = (100, 100, 100)
    button_text_color = (255, 255, 255)

    '''
    # button list
    buttons = [
        {"text": "PLAY", "x": 200, "y": 200},
        {"text": "Q & A", "x": 200, "y": 300},
        {"text": "ABOUT ME", "x": 200, "y": 400}
    ]
    '''
    level_menu = LevelMenu()
    about_me = AboutMeMenu()
    q_a = QAMenu()
    current_menu = None
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                
                x, y = pygame.mouse.get_pos()

                
                if 10 < x < 110 and 10 < y < 50:
                    current_menu = None
                elif 200 < x < 440 and 200 < y < 260:
                    current_menu = level_menu
                elif 200 < x < 440 and 400 < y < 460:
                    current_menu = about_me
                elif 200 < x < 440 and 300 < y < 360:
                    current_menu = q_a
                

                
                
        screen.fill((0, 0, 0))

        
        if current_menu is None:
            menu_buttons = [
                {"text": "PLAY", "x": 200, "y": 200},
                {"text": "Q & A", "x": 200, "y": 300},
                {"text": "ABOUT ME", "x": 200, "y": 400}
            ]
            for button in menu_buttons:
                Menu.draw_button(screen, button["x"], button["y"], button_width, button_height, button_color, button["text"], button_text_color)
        
        
        if current_menu == level_menu:
            level_menu.draw(screen)
        elif current_menu == about_me:
            about_me.draw(screen)
        elif current_menu == q_a:
             q_a.draw(screen)
        
        
        pygame.display.flip()

    pygame.quit()




if __name__ == "__main__":
    main()
