
import pygame
import Menu



def main():
    pygame.init()


    screen = pygame.display.set_mode((640,480))

    pygame.display.set_caption('Cyber Security Game')

    # button
    button_width = 240
    button_height = 60
    button_color = (100, 100, 100)
    button_text_color = (255, 255, 255)

    # button list
    buttons = [
        {"text": "Button 1", "x": 200, "y": 200},
        {"text": "Button 2", "x": 200, "y": 300},
        {"text": "Button 3", "x": 200, "y": 400}
    ]


    running = True
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        
        screen.fill((0, 0, 0))
        #drawing button
        for button in buttons:
            Menu.draw_button(screen, button["x"], button["y"], button_width, button_height, button_color, button["text"], button_text_color)
        
        
        pygame.display.flip()

    pygame.quit()




if __name__ == "__main__":
    main()