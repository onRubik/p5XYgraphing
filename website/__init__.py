from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import event
from os import path
# from .models import db, DVRPSet
from .models import db


DB_NAME = "dvrp.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    # from .models import GeoPermutations, GeoPoints, ORSCallLog, ORSDirectionsGeoJSONPost, StageGeoPermutations, StageGeoPoints

    create_database(app)

    return app


def create_database(app):
    db_path = path.join(app.instance_path, DB_NAME)
    if not path.exists(db_path):
        with app.app_context():
            db.create_all()
        print('Database created')