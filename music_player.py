from pygame import mixer
from pygame.mixer import music

LEVEL_MUSIC = {'main': 'scott-buckley-permafrost.mp3'}


def load_level_music(level_name):
    if not mixer.get_init():
        mixer.init()
    music.load(f"./data/audio/{LEVEL_MUSIC[level_name]}")
    music.play()


def quit_game_fix():
    if mixer.get_init():
        music.stop()
        mixer.quit()
