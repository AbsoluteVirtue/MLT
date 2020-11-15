import aiohttp_jinja2
import asyncio
import jinja2
import logging
import os.path
from aiohttp import web

from settings import config, cfg_path, setup_app


async def make_app():
    loop = asyncio.get_event_loop()
    app = web.Application(loop=loop)

    setup_app(app)

    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(os.path.abspath('templates')))

    return app


if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO)
    logging.info('Web server started on port %s' % config['port'])
    logging.info('Config file: %s' % cfg_path)

    web.run_app(make_app(), host=config['host'], port=config['port'],
                access_log_format='%t %P %s %r (%a) [%{Referer}i] %Tf')
