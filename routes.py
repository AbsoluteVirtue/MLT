from controllers import home


def setup_routes(app):
    app.router.add_view(r'/', handler=home.Index, name='home')
