from settings import logger
from utils import mp3_ps as media


execute = {
    'play': media.play,
    'stop': media.stop,
}


def parse(app, tokens):
    try:
        execute[tokens[0]](*tokens[1:])
    except Exception as e:
        logger.error(e)
