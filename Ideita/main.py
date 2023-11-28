from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import time


def abrir_navegador(url):

    # abrir el navegador
    driver = webdriver.Chrome()
    driver.get(url)

    return driver  # Devuelve el driver


def abrir_json():

    # acceder al usuario y contraseña de un json llamado credenciales
    with open('credenciales.json', 'r') as f:
        credenciales = json.load(f)
        email = credenciales['email']
        password = credenciales['password']

        return email, password


def iniciar_sesión(url):

    # Guarda el driver devuelto por abrir_navegador()
    driver = abrir_navegador(url)
    email, password = abrir_json()

    element = driver.find_element(By.NAME, "email")
    element.send_keys(email)

    element = driver.find_element(By.NAME, "password")
    element.send_keys(password)

    element = driver.find_element(By.NAME, "submit")
    element.click()

    time.sleep(10)

    buscar_libro(driver)


def buscar_libro(driver):

    element = driver.find_element(By.ID, "searchFieldx")
    element.send_keys("Imaginaria (Spanish Edition)")

    element = driver.find_element(
        By.XPATH, '//button[@type="submit" and @aria-label="Buscar"]')
    element.click()

    # Buscar todos los enlaces en los resultados de búsqueda
    elements = driver.find_elements(By.XPATH, '//h3[@itemprop="name"]/a')

    # Verificar que la lista no está vacía
    if elements:
        # Hacer clic en el primer enlace
        elements[1].click()
    else:
        print("No se encontraron resultados de búsqueda.")

    element = driver.find_element(
        By.CSS_SELECTOR, '.btn.btn-primary.dlButton.addDownloadedBook')
    element.click()
    '''
    element = driver.find_element(
        By.CLASS_NAME, 'btn btn-primary dlButton addDownloadedBook')
    element.click()
    '''
    input("Pulsa enter para cerrar el navegador...")
    driver.close()


# abrir_navegador()
# email, password = abrir_json()
# print(email, password)


url = r'https://es.singlelogin.se'
url2 = r'https://es.z-library.se/'

sel = input("Elija la url a la que desea acceder:")

if sel == "1":
    iniciar_sesión(url)
elif sel == "2":
    driver = abrir_navegador(url2)
    buscar_libro(driver)
else:
    print("Opción no válida")
