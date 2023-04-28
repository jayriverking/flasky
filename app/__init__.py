from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# gives use access to database operations
db = SQLAlchemy()
migrate = Migrate()


def create_app():
    # __name__ stores the name of the module we're in
    app = Flask(__name__)

    # set up database
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/flasky_development'
    
    db.init_app(app)
    migrate.init_app(app, db)
    # import crystal_bp from routes.py file
    from .routes import crystal_bp
    app.register_blueprint(crystal_bp)

    from app.models.crystal import Crystal
    # return the app
    return app