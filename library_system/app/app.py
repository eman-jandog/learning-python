from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./library.db'

    db.init_app(app)

    from app.library.routes import library
    app.register_blueprint(library, url_prefix=('/'))

    migrate = Migrate(app, db)

    return app