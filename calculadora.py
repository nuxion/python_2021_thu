import tkinter as tk
import tkinter.ttk as ttk


# breakpoint()
def sumar():
    # Obtenemos el texto ingresado por el usuario en cada caja
    # y lo convertimos a un entero para poder sumarlo.
    a = int(caja_a.get())
    b = int(caja_b.get())
    res = a + b
    resultado.config(text = "El resultado es: {}".format(res)) 
    print(res)
     


ventana = tk.Tk()
s = ttk.Style()
#s.theme_use('alt')
# s.configure(foreground='maroon')

ventana.config(width=400, height=300)
ventana.title("Esto es una calculadora")

caja_a = tk.Entry()
caja_a.place(x=20, y=20, width=50, height=25)

caja_b = tk.Entry()
caja_b.place(x=20, y=60, width=50, height=25)

resultado = tk.Label(text="Resultado: ")
resultado.place(x=20, y=140)



boton = tk.Button(text="Sumar", command=sumar)
boton.place(x=20, y=100)
ventana.mainloop()
