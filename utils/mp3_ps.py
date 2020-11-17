from playsound import playsound, PlaysoundException

from settings import media_path


def play(*args):
    try:
        playsound(f'{media_path}\\{args[0]}.mp3')
    except PlaysoundException as pe:
        raise Exception(pe)


def stop():
    try:
        playsound('utils/stop.mp3')
    except PlaysoundException as pe:
        raise Exception(pe)
