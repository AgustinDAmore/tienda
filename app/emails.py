import pywhatkit

def confirmacion_compra(app, WhatsApp,usuario,libro):
    try:
        pywhatkit.sendwhatmsg_instantly("+549"+WhatsApp,f"""
Hola {usuario.usuario}
Te confirmamos que has comprado el libro {libro.titulo}
{libro.url}
        """)
    except Exception as ex:
        raise Exception(ex)