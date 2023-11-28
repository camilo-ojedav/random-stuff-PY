from abrir_navegador import abrir_navegador
from iniciar_sesion import iniciar_sesion
from buscar_libro import buscar_libro


# abrir_navegador(url)
# email, password = abrir_json()
# print(email, password)


url = r'https://es.singlelogin.se'
url2 = r'https://es.z-library.se/'

'''libro = input("Introduzca el libro que desea descargar:")
libro = libro.replace(" ", "+")'''
libro = "Imaginaria (Spanish Edition)"

iniciar_sesion(url, libro)

sel = input("Elija la url a la que desea acceder:")

if sel == "1":
    iniciar_sesion(url, libro)
elif sel == "2":
    driver = abrir_navegador(url2)
    buscar_libro(driver)
else:
    print("Opción no válida")
