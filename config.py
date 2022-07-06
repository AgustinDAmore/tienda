from distutils.command.config import config
from distutils.debug import DEBUG
import secrets


class Config:
    SECRET_KEY = "nf*j*50fFe4h"

class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = "localhost"
    MYSQL_USER = "root"
    MYSQL_PASSWORD = "meii@#Mz#Xwx4qq"
    MYSQL_DB = "tienda"


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}