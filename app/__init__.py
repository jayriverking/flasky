from flask import Flask

def create_app():
    # __name__ stores the name of the module we're in
    app = Flask(__name__)
    # import amethyst_bp from amethyst.py file
    # from .amethyst import amethyst_bp
    # register blueprint
    # app.register_blueprint(amethyst_bp)

    return app