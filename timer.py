import time as t
import winsound as ws
import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

print("1 hora = 60 mins\n2 horas = 120\n3 horas = 180\n4 horas = 240\n5 horas = 300\n6 horas = 360\n7 horas = 420\n\n")

horas = int(input("horas?= "))


tiempo = int(input("Cuantos minutos quieres que dure: "))
min = 0
sec = 1
t.sleep(1)

for i in range(1, tiempo * 60):
    
    if i == 1:
        clear_terminal()

    if i % 60 == 0 and i != 0:
        min += 1
        sec = 0
        print("\n\n\n\n")


    if min <= 9:
        if sec <= 9:
            print("tiempo = 0%i:0%i" %(min, sec))
        else:
            print("tiempo = 0%i:%i" %(min, sec))
    else:
        if sec <= 9:
            print("tiempo = %i:0%i" %(min, sec))
        else:
            print("tiempo = %i:%i" %(min, sec))
    sec += 1
    
    print(i)
    print(tiempo *60)
    t.sleep(1)
    if i == (tiempo * 60) - 1:
        print("")
    else:
        clear_terminal()

# for i in range(mins * 2):
#     time.sleep(1)
#     if i == 0:
#         print("TIEMPO: %i:30" % i)
#     elif i == 1:
#         print("tiempo: %i:00" % i)
#     elif i % 2 == 0:
#         print("TIEMPO: %i:30" % (i/2))
#     else:
#         print("tiempo: %i:00" % ((i+1)/2))

#     print("\n\n")

#ws.Beep(2000, 5000)
