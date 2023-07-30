import os
import pyautogui
import pyautogui
import time
from PIL import Image
from winsound import Beep as Beep


def cambiar_ventana():
   
    pyautogui.keyDown('alt')
    pyautogui.press('tab')

    time.sleep(0.5)

    pyautogui.keyUp('alt')

    pyautogui.keyDown('f11')
    pyautogui.keyUp('f11')
    time.sleep(4.5)


def cambiar_pagina():
    pyautogui.keyDown('right')
    pyautogui.keyUp('right')
    time.sleep(2)


def take_screenshot(file_path):
    # Capturar la pantalla
    screenshot = pyautogui.screenshot()

    # Guardar la imagen
    screenshot.save(file_path)



if __name__ == "__main__":

    cambiar_ventana()

    folder_path = "libro"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


    pages = 190

    for i in range(pages+1):
        pag = str(i)
        file_name = pag + ".png"

        # Ruta completa de la captura de pantalla
        file_path = os.path.join(folder_path, file_name)

        # Tomar la captura de pantalla y guardarla en la subcarpeta
        take_screenshot(file_path)
        Beep(1000,500)
        cambiar_pagina()

        print("Captura de pantalla: ", pag,".png" )




