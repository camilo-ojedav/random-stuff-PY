import pyperclip as pyc
import winsound as ws

pagina = 8  #Numero de paginas del libro/documento

arr = [2, 3, 6, 7, 4, 1, 8, 5]      # Array principal
temp = []                           # Array temporal, en donde se guardan los numeros de una iteración del for
output = [2, 3, 6, 7, 4, 1, 8, 5]   # Array de salida
mult = (pagina // 8) - 1            # Se calcula el numero de iteraciones
resto = pagina % 8                  

for i in range(mult):
    # Se agrupan los 8 digitos en temp, siguiendo el orden de arr
    for j in arr:
        operation = j + 8
        temp.append(operation)
        
    # Se añaden a la salida
    for i in range(8):
        output.append(temp[i])
    
    arr = temp      # Se pasan los digitos temporales al array principal
    temp = []       
 
# if resto != 0:
#     for i in range(resto):
#         operation = arr[i] + 8
#         output.append(operation)

print(output)
texto = str(output)
texto = texto[1:-1]
pyc.copy(texto)


ws.Beep(2000, 100)  # Frecuencia de 2000 Hz durante 0.1 segundos




# numeros admiitos: multiplos de 8

# 8     16      24      32      40      48      56       64     72      80
# 88    96      104     112     120     128     136      144    152     160
# 168   176     184     192     200     208     216      224    232     240   
