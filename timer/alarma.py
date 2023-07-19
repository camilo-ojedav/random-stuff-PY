from random import randint as r
from winsound import Beep as Beep
from time import sleep as sleep

def alarma():
    for i in range(15):
        frec = r(37,1500)
        Beep(frec, 500)
        print("sonando alarma: %i ---> frecuencia: %i Hz" %(i+1, frec))
        #sleep(0.2)