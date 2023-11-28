from selenium import webdriver
import json
import time


def abrir_navegador():
    url = r'https://es.singlelogin.se'

    # abrir el navegador
    driver = webdriver.Chrome()
    driver.get(url)


def abrir_json():

    # acceder al usuario y contraseña de un json llamado credenciales
    with open('credenciales.json', 'r') as f:
        credenciales = json.load(f)
        email = credenciales['email']
        password = credenciales['password']

        return email, password

# espera 10 segundos antes de cerrar el navegador
# time.sleep(10)


# abrir_navegador()
email, password = abrir_json()
print(email, password)
