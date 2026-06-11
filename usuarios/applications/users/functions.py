import secrets
#
import string

def crear_codigo(size=6, chars=string.ascii_uppercase+string.digits):
    codigo = []
    for _ in range(size):
        codigo.append(secrets.choice(chars))
    return ''.join(codigo)



def enviar_correo():
    pass