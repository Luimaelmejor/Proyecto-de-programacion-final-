import tkinter as tk
from tkinter import messagebox
from datetime import datetime


libros = {
    101: {"titulo": "El Quijote", "autor": "Miguel de Cervantes", "isbn": "978-3-16-148410-0"},
    102: {"titulo": "Cien Años de Soledad", "autor": "Gabriel García Márquez", "isbn": "978-0-06-088328-7"},
    103: {"titulo": "Don Juan Tenorio", "autor": "José Zorrilla", "isbn": "978-84-376-0494-1"},
    104: {"titulo": "La Sombra del Viento", "autor": "Carlos Ruiz Zafón", "isbn": "978-0-14-303490-2"},
    105: {"titulo": "El Alquimista", "autor": "Paulo Coelho", "isbn": "978-0-06-112241-5"},
    106: {"titulo": "1984", "autor": "George Orwell", "isbn": "978-0-452-28423-4"},
    107: {"titulo": "Crimen y Castigo", "autor": "Fiódor Dostoyevski", "isbn": "978-0-14-044913-6"},
    108: {"titulo": "Orgullo y Prejuicio", "autor": "Jane Austen", "isbn": "978-0-19-953556-9"},
    109: {"titulo": "Matar a un Ruiseñor", "autor": "Harper Lee", "isbn": "978-0-06-112008-4"},
    110: {"titulo": "La Odisea", "autor": "Homero", "isbn": "978-0-14-026886-7"},
    111: {"titulo": "Ulises", "autor": "James Joyce", "isbn": "978-0-679-72232-7"},
    112: {"titulo": "En Busca del Tiempo Perdido", "autor": "Marcel Proust", "isbn": "978-0-14-243796-4"},
    113: {"titulo": "La Metamorfosis", "autor": "Franz Kafka", "isbn": "978-0-14-243755-1"},
    114: {"titulo": "Divina Comedia", "autor": "Dante Alighieri", "isbn": "978-0-14-243722-3"},
    115: {"titulo": "Fahrenheit 451", "autor": "Ray Bradbury", "isbn": "978-0-7432-4722-1"},
    116: {"titulo": "El Gran Gatsby", "autor": "F. Scott Fitzgerald", "isbn": "978-0-7432-7356-3"},
    117: {"titulo": "El Señor de los Anillos", "autor": "J.R.R. Tolkien", "isbn": "978-0-618-00222-8"},
    118: {"titulo": "Los Miserables", "autor": "Victor Hugo", "isbn": "978-0-14-044430-8"},
    119: {"titulo": "Cumbres Borrascosas", "autor": "Emily Brontë", "isbn": "978-0-14-143955-6"},
    120: {"titulo": "El Retrato de Dorian Gray", "autor": "Oscar Wilde", "isbn": "978-0-14-143957-0"},
    121: {"titulo": "El Príncipe", "autor": "Nicolás Maquiavelo", "isbn": "978-0-14-044915-0"},
    122: {"titulo": "Ana Karenina", "autor": "León Tolstói", "isbn": "978-0-14-303500-8"},
    123: {"titulo": "Las Mil y Una Noches", "autor": "Anónimo", "isbn": "978-0-14-044938-9"},
    124: {"titulo": "El Guardián entre el Centeno", "autor": "J.D. Salinger", "isbn": "978-0-316-76948-0"},
    125: {"titulo": "La Iliada", "autor": "Homero", "isbn": "978-0-14-027536-0"}
}

miembros = {
    2301009: {"nombre": "Luis Garcia", "email": "luis.garcia@example.com"},
    202: {"nombre": "Joerlyn Morfe", "email": "joerlyn.morfe@example.com"},
    203: {"nombre": "Ana Pérez", "email": "ana.perez@example.com"},
    204: {"nombre": "Carlos Sánchez", "email": "carlos.sanchez@example.com"},
    205: {"nombre": "María López", "email": "maria.lopez@example.com"},
    206: {"nombre": "Pedro Fernández", "email": "pedro.fernandez@example.com"},
    207: {"nombre": "Laura Gómez", "email": "laura.gomez@example.com"},
    208: {"nombre": "Juan Martínez", "email": "juan.martinez@example.com"},
    209: {"nombre": "Sofía Torres", "email": "sofia.torres@example.com"},
    210: {"nombre": "Miguel Ángel", "email": "miguel.angel@example.com"}
}

prestamos = []


def agregar_libro():
    try:
        id_libro = int(entry_id_libro.get())
        titulo = entry_titulo.get()
        autor = entry_autor.get()
        isbn = entry_isbn.get()
        
        if id_libro in libros:
            messagebox.showwarning("Advertencia", "El libro ya existe en la biblioteca.")
        else:
            libros[id_libro] = {"titulo": titulo, "autor": autor, "isbn": isbn}
            messagebox.showinfo("Información", "Libro agregado correctamente.")
            limpiar_campos_libro()
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese un ID de libro válido.")

def eliminar_libro():
    try:
        id_libro = int(entry_id_libro.get())
        if id_libro in libros:
            del libros[id_libro]
            messagebox.showinfo("Información", "Libro eliminado correctamente.")
            limpiar_campos_libro()
        else:
            messagebox.showwarning("Advertencia", "El libro no existe en la biblioteca.")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese un ID de libro válido.")

def buscar_libro():
    try:
        id_libro = int(entry_id_libro.get())
        if id_libro in libros:
            libro = libros[id_libro]
            entry_titulo.delete(0, tk.END)
            entry_titulo.insert(0, libro["titulo"])
            entry_autor.delete(0, tk.END)
            entry_autor.insert(0, libro["autor"])
            entry_isbn.delete(0, tk.END)
            entry_isbn.insert(0, libro["isbn"])
        else:
            messagebox.showwarning("Advertencia", "El libro no existe en la biblioteca.")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese un ID de libro válido.")

def limpiar_campos_libro():
    entry_id_libro.delete(0, tk.END)
    entry_titulo.delete(0, tk.END)
    entry_autor.delete(0, tk.END)
    entry_isbn.delete(0, tk.END)


def agregar_miembro():
    try:
        id_miembro = int(entry_id_miembro.get())
        nombre = entry_nombre.get()
        email = entry_email.get()
        
        if id_miembro in miembros:
            messagebox.showwarning("Advertencia", "El miembro ya existe en la biblioteca.")
        else:
            miembros[id_miembro] = {"nombre": nombre, "email": email}
            messagebox.showinfo("Información", "Miembro agregado correctamente.")
            limpiar_campos_miembro()
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese un ID de miembro válido.")

def eliminar_miembro():
    try:
        id_miembro = int(entry_id_miembro.get())
        if id_miembro in miembros:
            del miembros[id_miembro]
            messagebox.showinfo("Información", "Miembro eliminado correctamente.")
            limpiar_campos_miembro()
        else:
            messagebox.showwarning("Advertencia", "El miembro no existe en la biblioteca.")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese un ID de miembro válido.")

def buscar_miembro():
    try:
        id_miembro = int(entry_id_miembro.get())
        if id_miembro in miembros:
            miembro = miembros[id_miembro]
            entry_nombre.delete(0, tk.END)
            entry_nombre.insert(0, miembro["nombre"])
            entry_email.delete(0, tk.END)
            entry_email.insert(0, miembro["email"])
        else:
            messagebox.showwarning("Advertencia", "El miembro no existe en la biblioteca.")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese un ID de miembro válido.")

def limpiar_campos_miembro():
    entry_id_miembro.delete(0, tk.END)
    entry_nombre.delete(0, tk.END)
    entry_email.delete(0, tk.END)


def registrar_prestamo():
    try:
        id_miembro = int(entry_id_miembro_prestamo.get())
        id_libro = int(entry_id_libro_prestamo.get())
        fecha_prestamo = datetime.now().strftime("%Y-%m-%d")
        
        if id_miembro not in miembros:
            messagebox.showwarning("Advertencia", "El miembro no existe en la biblioteca.")
            return
        
        if id_libro not in libros:
            messagebox.showwarning("Advertencia", "El libro no existe en la biblioteca.")
            return
        
        prestamos.append({"id_miembro": id_miembro, "id_libro": id_libro, "fecha_prestamo": fecha_prestamo, "fecha_devolucion": None})
        messagebox.showinfo("Información", "Préstamo registrado correctamente.")
        limpiar_campos_prestamo()
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese IDs válidos para miembro y libro.")

def registrar_devolucion():
    try:
        id_miembro = int(entry_id_miembro_prestamo.get())
        id_libro = int(entry_id_libro_prestamo.get())
        
        for prestamo in prestamos:
            if prestamo["id_miembro"] == id_miembro and prestamo["id_libro"] == id_libro and prestamo["fecha_devolucion"] is None:
                prestamo["fecha_devolucion"] = datetime.now().strftime("%Y-%m-%d")
                messagebox.showinfo("Información", "Devolución registrada correctamente.")
                limpiar_campos_prestamo()
                return
        
        messagebox.showwarning("Advertencia", "No se encontró un préstamo activo para este libro y miembro.")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese IDs válidos para miembro y libro.")

def limpiar_campos_prestamo():
    entry_id_miembro_prestamo.delete(0, tk.END)
    entry_id_libro_prestamo.delete(0, tk.END)


root = tk.Tk()
root.title("Sistema de Biblioteca")


frame_libros = tk.LabelFrame(root, text="Gestión de Libros")
frame_libros.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

label_id_libro = tk.Label(frame_libros, text="ID Libro:")
label_id_libro.grid(row=0, column=0, padx=10, pady=5)
entry_id_libro = tk.Entry(frame_libros)
entry_id_libro.grid(row=0, column=1, padx=10, pady=5)

label_titulo = tk.Label(frame_libros, text="Título:")
label_titulo.grid(row=1, column=0, padx=10, pady=5)
entry_titulo = tk.Entry(frame_libros)
entry_titulo.grid(row=1, column=1, padx=10, pady=5)

label_autor = tk.Label(frame_libros, text="Autor:")
label_autor.grid(row=2, column=0, padx=10, pady=5)
entry_autor = tk.Entry(frame_libros)
entry_autor.grid(row=2, column=1, padx=10, pady=5)

label_isbn = tk.Label(frame_libros, text="ISBN:")
label_isbn.grid(row=3, column=0, padx=10, pady=5)
entry_isbn = tk.Entry(frame_libros)
entry_isbn.grid(row=3, column=1, padx=10, pady=5)

button_agregar_libro = tk.Button(frame_libros, text="Agregar Libro", command=agregar_libro)
button_agregar_libro.grid(row=4, column=0, padx=10, pady=5)
button_eliminar_libro = tk.Button(frame_libros, text="Eliminar Libro", command=eliminar_libro)
button_eliminar_libro.grid(row=4, column=1, padx=10, pady=5)
button_buscar_libro = tk.Button(frame_libros, text="Buscar Libro", command=buscar_libro)
button_buscar_libro.grid(row=5, column=0, padx=10, pady=5)
button_limpiar_libro = tk.Button(frame_libros, text="Limpiar Campos", command=limpiar_campos_libro)
button_limpiar_libro.grid(row=5, column=1, padx=10, pady=5)


frame_miembros = tk.LabelFrame(root, text="Gestión de Miembros")
frame_miembros.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

label_id_miembro = tk.Label(frame_miembros, text="ID Miembro:")
label_id_miembro.grid(row=0, column=0, padx=10, pady=5)
entry_id_miembro = tk.Entry(frame_miembros)
entry_id_miembro.grid(row=0, column=1, padx=10, pady=5)

label_nombre = tk.Label(frame_miembros, text="Nombre:")
label_nombre.grid(row=1, column=0, padx=10, pady=5)
entry_nombre = tk.Entry(frame_miembros)
entry_nombre.grid(row=1, column=1, padx=10, pady=5)

label_email = tk.Label(frame_miembros, text="Email:")
label_email.grid(row=2, column=0, padx=10, pady=5)
entry_email = tk.Entry(frame_miembros)
entry_email.grid(row=2, column=1, padx=10, pady=5)

button_agregar_miembro = tk.Button(frame_miembros, text="Agregar Miembro", command=agregar_miembro)
button_agregar_miembro.grid(row=3, column=0, padx=10, pady=5)
button_eliminar_miembro = tk.Button(frame_miembros, text="Eliminar Miembro", command=eliminar_miembro)
button_eliminar_miembro.grid(row=3, column=1, padx=10, pady=5)
button_buscar_miembro = tk.Button(frame_miembros, text="Buscar Miembro", command=buscar_miembro)
button_buscar_miembro.grid(row=4, column=0, padx=10, pady=5)
button_limpiar_miembro = tk.Button(frame_miembros, text="Limpiar Campos", command=limpiar_campos_miembro)
button_limpiar_miembro.grid(row=4, column=1, padx=10, pady=5)


frame_prestamos = tk.LabelFrame(root, text="Gestión de Préstamos")
frame_prestamos.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

label_id_miembro_prestamo = tk.Label(frame_prestamos, text="ID Miembro:")
label_id_miembro_prestamo.grid(row=0, column=0, padx=10, pady=5)
entry_id_miembro_prestamo = tk.Entry(frame_prestamos)
entry_id_miembro_prestamo.grid(row=0, column=1, padx=10, pady=5)

label_id_libro_prestamo = tk.Label(frame_prestamos, text="ID Libro:")
label_id_libro_prestamo.grid(row=1, column=0, padx=10, pady=5)
entry_id_libro_prestamo = tk.Entry(frame_prestamos)
entry_id_libro_prestamo.grid(row=1, column=1, padx=10, pady=5)

button_registrar_prestamo = tk.Button(frame_prestamos, text="Registrar Préstamo", command=registrar_prestamo)
button_registrar_prestamo.grid(row=2, column=0, padx=10, pady=5)
button_registrar_devolucion = tk.Button(frame_prestamos, text="Registrar Devolución", command=registrar_devolucion)
button_registrar_devolucion.grid(row=2, column=1, padx=10, pady=5)

root.mainloop()
