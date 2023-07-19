import clear_terminal as cl

from time import sleep as sleep
from barra import barra as b

def cronometro(tiempo, dormido):

    hour = 0
    min = 0
    sec = 0
    cl.clear_terminal()

    for i in range(0, tiempo+1):

        if i % 60 == 0 and i != 0:
            min += 1
            sec = 0

        if i % 3600 == 0 and i != 0:
            hour +=1
            min = 0
        b(i, tiempo)
        print("\ntiempo = ", end="")

        if hour == 0:
            pass
        else:
            if hour <= 9:
                print("0%i" % hour, end=":")
            else:
                print(hour, end=":")
        if min <= 9:
            print("0%i" % min, end=":")     
        else:
            print("%i" % min, end=":")
        if sec <= 9:
            print("0%i" % sec)
        else:
            print(sec)


        sec += 1
        
        #print("i: ",i)
        #print("tiempo: ",tiempo)
        
        
        if dormido and (i != tiempo):
            sleep(1)


        if i == tiempo:
            print("")
        else:
            cl.clear_terminal()

        
            