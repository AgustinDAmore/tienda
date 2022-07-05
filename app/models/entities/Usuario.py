from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(UserMixin):
    def __init__(self, id, usuario, password,tipousuario):
        self.id = id
        self.usuario = usuario
        self.password = password
        self.tipousuario = tipousuario

    def encriptar_password(self, password):
        encriptado = generate_password_hash(password)
        return check_password_hash(encriptado, password)