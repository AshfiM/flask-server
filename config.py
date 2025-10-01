import os

class Config:
    FLASK_SECRET_KEY = os.getnev("FLASK_SECRET_KEY", "dev_secret_key")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "jsonsecret")
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URL", "mysql.com")
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config = {
    "development":DevelopmentConfig,
    "production":ProductionConfig
}

