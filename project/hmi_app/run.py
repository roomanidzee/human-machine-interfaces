from server import create_app

app = create_app()

app.run(
    host=app.config.host,
    port=app.config.port,
    debug=app.config.debug,
    use_reloader=app.config.use_reloader,
)
