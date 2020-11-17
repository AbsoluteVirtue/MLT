import aiohttp
import argparse
import asyncio
import os.path
import yaml
import logging
from yaml import FullLoader


def get_cl_args():
    parser = argparse.ArgumentParser(description='Process arguments.')
    parser.add_argument(
        '--config_file', dest='config_file', default='./config/local.yaml', help='config file relative path')
    parser.add_argument(
        '--media', dest='media_folder', default='', help='media files absolute path')

    _cfg_path = parser.parse_args().config_file
    _media_path = parser.parse_args().media_folder

    config_file = os.path.abspath(_cfg_path)
    with open(config_file) as f:
        _config = yaml.load(f, Loader=FullLoader)

    return _config, _cfg_path, _media_path


def get_logger():
    _logger = logging.getLogger(name='aiohttp.access')
    _logger.setLevel(log_level)
    _logger.addHandler(logging.StreamHandler())

    return _logger


config, cfg_path, media_path = get_cl_args()

log_level = logging.DEBUG if config['debug'] else logging.INFO

logging.getLogger('aiohttp.server').setLevel(log_level)
logging.getLogger('aiohttp.web').setLevel(log_level)

logger = get_logger()


async def close_session(app):
    await asyncio.sleep(0.25)
    await app['http'].close()


def configure_settings(app):
    app['history'] = []
    app['http'] = aiohttp.ClientSession()

    app.on_cleanup.append(close_session)
