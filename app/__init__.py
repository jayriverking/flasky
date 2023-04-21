from flask import Flask

def create_app():
    # __name__ stores the name of the module we're in
    app = Flask(__name__)
    # import crystal_bp from routes.py file
    from .routes import crystal_bp
    app.register_blueprint(crystal_bp)
    # return the app
    return app