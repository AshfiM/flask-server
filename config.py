import os

class Config:
    # Flask session secret
    SECRET_KEY = os.getenv("FLASK_SECRET_KEY", "dev_secret_key")

    # JWT secret
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "jsonsecret")

    # Database URL
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URL", "sqlite:///dev.db")

    # Turn off warning
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig
}
