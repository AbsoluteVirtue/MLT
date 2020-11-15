from playsound import playsound, PlaysoundException


def play(filename, media_path):
    try:
        playsound(f'{media_path}\\{filename}')
    except PlaysoundException as pe:
        raise Exception(pe)
