import pygame

from windows.Window import Window
from sprites.Button import Button
from sprites.Text import Text


class MainMenu(Window):
    def __init__(self, game):
        super().__init__(game)

        # TEXTS
        self.font = pygame.font.Font("../assets/fonts/pixelify.ttf", 60)
        main_title_content = "Punching Jellies"
        main_title_text_size = self.font.size(main_title_content)
        self.main_title_text = Text(
            ((700-main_title_text_size[0])//2,(500-main_title_text_size[1])//4),
            main_title_content,
            self.font,
            (255,255,255)
        )

        # BUTTONS
        self.button_next_window = Button(
            (0, 0),
            self.next_window,
            None,
        )

        # ADDING SPRITES TO INITIAL GROUPS
        self.buttons.add([self.button_next_window,])
        self.texts.add([self.main_title_text])

        # MUSIC
        pygame.mixer.music.set_volume(0.05)
        pygame.mixer.music.load("../assets/audio/music/main_theme.mp3")
        pygame.mixer.music.play(-1)

    def next_window(self):
        pass

    def previous_window(self):
        pass