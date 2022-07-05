from distutils.command.config import config
from distutils.debug import DEBUG
import secrets


class Config:
    SECRET_KEY = "nf*j*50fFe4h"

class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = "localhost"
    MYSQL_USER = "root"
    MYSQL_PASSWORD = ""
    MYSQL_DB = "tienda"


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}