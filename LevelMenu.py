import pygame
from Button import Button
class LevelMenu:
    def __init__(self):
        self.button_width = 200
        self.button_height = 80

        self.button_level1 = Button(100, 100, self.button_width, self.button_height, "Level 1", self.level1_clicked)
        self.button_level2 = Button(100, 200, self.button_width, self.button_height, "Level 2", self.level2_clicked)
        self.button_level3 = Button(100, 300, self.button_width, self.button_height, "Level 3", self.level3_clicked)

        self.button_level4 = Button(360, 100, self.button_width, self.button_height, "Level 4", self.level1_clicked)
        self.button_level5 = Button(360, 200, self.button_width, self.button_height, "Level 5", self.level2_clicked)
        self.button_level6 = Button(360, 300, self.button_width, self.button_height, "Level 6", self.level3_clicked)

        self.button_return = Button(10, 10, 100, 40, "Back", self.return_clicked)
    



    def level1_clicked(self):
        print("Level 1 Clicked!")

    def level2_clicked(self):
        print("Level 2 Clicked!")


    def level3_clicked(self):
        print("Level 3 Clicked!")

    def level4_clicked(self):
        print("Level 4 Clicked!")

    def level5_clicked(self):
        print("Level 5 Clicked!")

    def level6_clicked(self):
        print("Level 6 Clicked!")


    def return_clicked(self):
        global current_menu
        current_menu = None


    def draw(self, screen):
       
        self.button_level1.draw(screen)
        self.button_level2.draw(screen)
        self.button_level3.draw(screen)
        self.button_level4.draw(screen)
        self.button_level5.draw(screen)
        self.button_level6.draw(screen)
        self.button_return.draw(screen)

    def handle_event(self, event):
        self.button_level1.handle_event(event)
        self.button_level2.handle_event(event)
        self.button_level3.handle_event(event)
        self.button_level4.handle_event(event)
        self.button_level5.handle_event(event)
        self.button_level6.handle_event(event)
        self.button_return.handle_event(event)
