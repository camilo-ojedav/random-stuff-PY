import json


def abrir_json():

    # acceder al usuario y contraseña de un json llamado credenciales
    with open('credenciales.json', 'r') as f:
        credenciales = json.load(f)
        email = credenciales['email']
        password = credenciales['password']

        return email, password
