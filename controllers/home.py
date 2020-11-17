import aiohttp_jinja2
from aiohttp import web
from . import parse


class Index(web.View):

    async def get(self):
        response = aiohttp_jinja2.render_template(
            'home.html', self.request, context={})

        return response

    async def post(self):
        body = await self.request.post()

        query = body['query']   # TODO: input validation
        tokens = query.split(' ')

        parse(self.request.app, tokens)

        raise web.HTTPFound(self.request.app.router['home'].url_for())
