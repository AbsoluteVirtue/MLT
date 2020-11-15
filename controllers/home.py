import aiohttp_jinja2
from aiohttp import web

from utils import mp3_ps as media


class Index(web.View):

    async def get(self):
        response = aiohttp_jinja2.render_template(
            'home.html', self.request, context={})

        return response

    async def post(self):
        body = await self.request.post()

        filename = body['filename']
        try:
            media.play(filename, self.request.app['media'])
            _s = True
        except Exception as e:
            self.request.app['logger'].error(e)
            _s = False

        return web.json_response({'success': _s})
