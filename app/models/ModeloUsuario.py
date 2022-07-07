from .entities.Usuario import Usuario
from .entities.TipoUsuario import TipoUsuario

class ModeloUsuario():

    @classmethod
    def login(self,db,usuario):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT id, usuario, password 
                    FROM usuario WHERE usuario = '{0}' """.format(usuario.usuario)
            cursor.execute(sql)
            data = cursor.fetchone()
            if data != None:
                if Usuario.verificar_password(data[2], usuario.password):
                    usuario_logeado = Usuario(data[0], data[1],None, None)
                    return usuario_logeado
                else:
                    return None
            else:
                return None
                
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def crear_usuario(self,db,nuevoUsuario):
        # validar contraseña
        if nuevoUsuario[1] != nuevoUsuario[2]:
            return None
        try:
            usuario = Usuario(0, nuevoUsuario[0], Usuario.crear_password(nuevoUsuario[1]), 2)
            cursor = db.connection.cursor()
            sql = """INSERT INTO usuario (id, usuario, password, tipousuario_id)
                    VALUES ('NULL', '{0}', '{1}', 2) """.format(usuario.usuario, usuario.password)
            cursor.execute(sql)
            db.connection.commit()
            return True
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def obtener_por_id(self,db,id):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT USU.id, USU.usuario, TIP.id, TIP.nombre
                    FROM usuario USU JOIN tipousuario TIP ON USU.tipousuario_id = TIP.id
                    WHERE USU.id = {0} """.format(id)
            cursor.execute(sql)
            data = cursor.fetchone()
            tipousuario = TipoUsuario(data[2],data[3])
            usuario_logeado = Usuario(data[0],data[1],None,tipousuario)
            return usuario_logeado
        except Exception as ex:
            raise Exception(ex)