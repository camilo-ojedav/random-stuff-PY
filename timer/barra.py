
def barra(actual, tiempo):

    total = tiempo / 100
    porcentaje = int(actual / total)
    porcentaje_real = actual / total
    print("[%.2f%%]" % porcentaje_real,end=" ")

    for i in range(porcentaje):
        print("#", end="")