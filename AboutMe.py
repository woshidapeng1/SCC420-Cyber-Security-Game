import pygame
from Button import Button


class AboutMeMenu:
    def __init__(self):
        self.button_return = Button(10, 10, 100, 40, "Return", self.return_clicked)

    def return_clicked(self):
        global current_menu
        current_menu = None

    def draw(self, screen):
        
        self.button_return.draw(screen)

        
        font = pygame.font.Font(None, 30)
        text = [
            "THIS GAME IS GOOD"
        ]
        for i, line in enumerate(text):
            text_surface = font.render(line, True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(screen.get_width() // 2, 150 + i * 30))
            screen.blit(text_surface, text_rect)
