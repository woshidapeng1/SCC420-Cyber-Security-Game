import pygame

class Button:
    def __init__(self, x, y, width, height, text, click_handler):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.click_handler = click_handler

    def draw(self, screen):
        pygame.draw.rect(screen, (100, 100, 100), self.rect)
        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.click_handler()
