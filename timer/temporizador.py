import clear_terminal as cl

import time as t

def te(tiempo, dormido):
    
    if tiempo >= 3600:
        hour = tiempo / 3600
    else:
        hour = 0

    if tiempo >= 60:
        min = tiempo // 60
    else:
        min = 0
    
    if tiempo >= 60:
        sec = tiempo % 60
    else:
        sec = tiempo
    cl.clear_terminal()

    for i in range(tiempo , -1, -1):

        if i % 60 == 0 and i != 0:
            sec = 0

        if i % 3600 == 0 and i != 0:
            hour -=1
            min = 0


        print("tiempo = ", end="")

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

        if sec == 0 and i != -1:
            min -= 1
            sec = 59
        else:
            sec -= 1
        
        print("i: ",i)
        print("tiempo: ",tiempo)


        if dormido:
            t.sleep(1)
        
        if i == 0:
            print("")
        else:
            cl.clear_terminal()



