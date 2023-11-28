from selenium import webdriver


def abrir_navegador(url):

    # abrir el navegador
    driver = webdriver.Chrome()
    driver.get(url)

    return driver  # Devuelve el driver
