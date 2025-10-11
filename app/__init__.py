from flask import Flask
from config import config
import os
from .extensions import jwt, db, cors
from .auth import auth_bp
from .routes import main_bp
from .api import dataSets_bp, users_bp

def create_app(env_name=None):
    app = Flask(__name__)
    env_name = env_name or os.getenv("FLASK_ENV")
    app.config.from_object(config[env_name])
    
    db.init_app(app)
    jwt.init_app(app)
    cors.init_app(app)
    
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(dataSets_bp, url_prefix="/api/datasets")
    app.register_blueprint(users_bp, url_prefix="/api/users")
    
    return app
