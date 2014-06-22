import pygame

class PlayBuzzer:
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.load("fail-buzzer-03.mp3")
    def keepOnNoising(self):
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.play()
    def __del__(self):
        pygame.mixer.quit()
