
def menu():
    
    
    horas = int(input("¿horas?: "))
    # v_horas = True
    # while v_horas:
    #     horas = int(input("¿horas?: "))
    #     if horas >= 24:
    #         v_horas = False
    #     else:
    #         print("Valor erroneo, ingrese un valor menor o igual a 24.\n")
    
    v_minutos = True

    while v_minutos:
        minutos = int(input("¿minutos?: "))

        if minutos <= 59:
            v_minutos = False
        else:
            print("Valor erroneo, ingrese un valor menor o igual a 59.\n")

    v_segundos = True

    while v_segundos:
        segundos = int(input("¿segundos?: "))

        if segundos <= 59:
            v_segundos = False
        else:
            print("Valor erroneo, ingrese un valor menor o igual a 59.\n")


    tiempo = segundos + (minutos * 60) + (horas * 60 * 60)

    return(tiempo)
