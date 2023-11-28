from selenium.webdriver.common.by import By


def buscar_libro(driver, libro):

    element = driver.find_element(By.ID, "searchFieldx")
    element.send_keys(libro)

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

    input("Pulsa enter para cerrar el navegador...")
    driver.close()
