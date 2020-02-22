from server import create_app

app = create_app()

app.run(
    host=app.config['APP_HOST'],
    port=app.config['APP_PORT'],
    debug=app.config['FLASK_DEBUG'],
)
