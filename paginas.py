import pyperclip as pyc
import winsound as ws


pagina = 23

c = 1

arr = [2, 3, 6, 7, 4, 1, 8, 5]
temp = []
temp2 = [2, 3, 6, 7, 4, 1, 8, 5]
mult = (pagina // 8) - 1
resto = pagina % 8
print("Resto = ", resto)


for i in range(mult):
    for j in arr:
        operation = j + 8
        temp.append(operation)
        

    for i in range(8):
        temp2.append(temp[i])
    arr = temp
    temp = []

if resto != 0:
    for i in range(resto):
        operation = arr[i] + 8
        temp.append(operation)

print(temp2)
texto = str(temp2)
texto = texto[1:-1]
pyc.copy(texto)


ws.Beep(2000, 500)  # Frecuencia de 2000 Hz durante medio segundo





