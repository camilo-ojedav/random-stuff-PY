import json

url = 'https://es.singlelogin.se'

# acceder al usuario y contraseña de un json llamado credenciales
with open('credenciales.json') as f:
    credenciales = json.load(f)
    email = credenciales['email']
    password = credenciales['password']
