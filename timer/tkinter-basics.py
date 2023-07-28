import tkinter as tk

ventana = tk.Tk()
# Dimensiones = Anchura x Altura
ventana.geometry("500x300")

def saludo(nombre):
    print("Hello", nombre)



etiqueta = tk.Label(ventana, text = "Hola Mundo", background= "Blue")

#etiqueta.pack(side= tk.BOTTOM)

def textoDeLaCaja():
    texto = CajaTexto.get()
    etiqueta["text"] = texto

CajaTexto = tk.Entry(ventana, font = "Helvetica 18")
CajaTexto.pack()

boton1 = tk.Button(ventana, text= "Clickeame", padx = 30, pady= 40, command= textoDeLaCaja)
boton1.pack()

etiqueta = tk.Label(ventana, font = "Times 25")
etiqueta.pack()


ventana.mainloop()