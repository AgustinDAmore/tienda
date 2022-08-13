from decouple import config

class Config:
    SECRET_KEY = config("SECRET_KEY")

class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = "localhost"
    MYSQL_USER = "root"
    MYSQL_PASSWORD = config("MYSQL_PASSWORD")
    MYSQL_DB = "tienda"
    MAIL_SERVER = "smtp.googlemail.com" # "smtp.gmail.com"
    MAIL_PORT = 587 # TLS: Transport Layer Security
    MAIL_USE_TLS = True
    MAIL_USERNAME = config("MAIL")
    MAIL_PASSWORD = config("MAIL_PASSWORD")


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}