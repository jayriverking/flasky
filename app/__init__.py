from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# from env -- import uri's and stuff
from dotenv import load_dotenv
import os

# gives use access to database operations
db = SQLAlchemy()
migrate = Migrate()
load_dotenv()


def create_app(test_config=None):
    # __name__ stores the name of the module we're in
    app = Flask(__name__)

    # set up database
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    if not test_config:
        # development environment configurations
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("RENDER_DATABASE_URI")
    else:
        # testing environment configurations
        app.config["TESTING"] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_TEST_DATABASE_URI")

    db.init_app(app)
    migrate.init_app(app, db)
    # import crystal_bp from routes.py file
    from .routes import crystal_bp, healer_bp
    app.register_blueprint(crystal_bp)
    app.register_blueprint(healer_bp)

    from app.models.crystal import Crystal
    from app.models.healer import Healer
    # return the app
    return app