import random as r
import winsound as ws
import time as t

def alarma():
    for i in range(15):
        frec = r.randint(37,1500)
        ws.Beep(frec, 500)
        print("sonando alarma: %i ---> frecuencia: %i Hz" %(i+1, frec))
        #t.sleep(0.2)