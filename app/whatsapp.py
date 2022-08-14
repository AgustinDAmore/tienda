import pywhatkit

def confirmacion_compra(app, WhatsApp,usuario,libro):
    try:
        pywhatkit.sendwhatmsg_instantly("+549"+WhatsApp,f"""
Hola {usuario.usuario}
Te adjuntamos el enlace al libro {libro.titulo}
{libro.url}
Espero lo disfrutes! :)""",9,True,2)
    except Exception as ex:
        raise Exception(ex)