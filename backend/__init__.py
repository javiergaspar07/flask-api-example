from flask import Flask
from backend.config import Config, APIRouter
from backend.middlewares import Middleware
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

jwt = JWTManager()
db = SQLAlchemy()
migrate = Migrate()
api_router = APIRouter()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)
    #app.wsgi_app = Middleware(app.wsgi_app)
    api_router.init_app(app)
    return app
