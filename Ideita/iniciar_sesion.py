from selenium.webdriver.common.by import By
from abrir_navegador import abrir_navegador
from abrir_json import abrir_json
from buscar_libro import buscar_libro
import time


def iniciar_sesion(url, libro):

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

    buscar_libro(driver, libro)
