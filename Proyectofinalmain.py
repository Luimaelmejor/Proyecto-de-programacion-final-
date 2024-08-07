import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import random
import string


def generar_contrasena():
    longitud = int(entry_longitud.get())
    incluir_numeros = var_numeros.get()
    incluir_simbolos = var_simbolos.get()
    incluir_mayusculas = var_mayusculas.get()
    incluir_minusculas = var_minusculas.get()
    
    caracteres = ''
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    if incluir_minusculas:
        caracteres += string.ascii_lowercase

    if not caracteres:
        messagebox.showwarning("Advertencia", "Debe seleccionar al menos un tipo de carácter")
        return

    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    entry_contrasena.delete(0, tk.END)
    entry_contrasena.insert(0, contrasena)


def guardar_contrasena():
    contrasena = entry_contrasena.get()
    if not contrasena:
        messagebox.showwarning("Advertencia", "No hay contraseña generada para guardar")
        return

    archivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if archivo:
        with open(archivo, 'w') as f:
            f.write(contrasena)
        messagebox.showinfo("Información", "Contraseña guardada correctamente")


root = tk.Tk()
root.title("Generador de Contraseñas")

label_longitud = tk.Label(root, text="Longitud:")
label_longitud.grid(row=0, column=0, padx=10, pady=10)

entry_longitud = tk.Entry(root)
entry_longitud.grid(row=0, column=1, padx=10, pady=10)

var_numeros = tk.BooleanVar()
check_numeros = tk.Checkbutton(root, text="Incluir números", variable=var_numeros)
check_numeros.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

var_simbolos = tk.BooleanVar()
check_simbolos = tk.Checkbutton(root, text="Incluir símbolos", variable=var_simbolos)
check_simbolos.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

var_mayusculas = tk.BooleanVar()
check_mayusculas = tk.Checkbutton(root, text="Incluir mayúsculas", variable=var_mayusculas)
check_mayusculas.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

var_minusculas = tk.BooleanVar()
check_minusculas = tk.Checkbutton(root, text="Incluir minúsculas", variable=var_minusculas)
check_minusculas.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

button_generar = tk.Button(root, text="Generar Contraseña", command=generar_contrasena)
button_generar.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

entry_contrasena = tk.Entry(root, width=50)
entry_contrasena.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

button_guardar = tk.Button(root, text="Guardar Contraseña", command=guardar_contrasena)
button_guardar.grid(row=7, column=0, columnspan=2, padx=10, pady=10)


root.mainloop()
