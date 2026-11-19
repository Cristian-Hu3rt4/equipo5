import sqlite3, tkinter as tk
from tkinter import messagebox

db = sqlite3.connect('escuela.db')
db.execute("CREATE TABLE IF NOT EXISTS alumnos (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, grupo TEXT, correo TEXT)")

ventana = tk.Tk()
ventana.title("CRUD Alumnos")
ventana.geometry("400x500")

tk.Label(ventana, text="CRUD Alumnos", font=("Arial", 16, "bold")).pack(pady=10)
tk.Label(ventana, text="Nombre:").pack()
e_nombre = tk.Entry(ventana, width=30); e_nombre.pack()
tk.Label(ventana, text="Grupo:").pack()
e_grupo = tk.Entry(ventana, width=30); e_grupo.pack()
tk.Label(ventana, text="Correo:").pack()
e_correo = tk.Entry(ventana, width=30); e_correo.pack()

lista = tk.Listbox(ventana, width=50, height=10); lista.pack(pady=10)

def mostrar():
    lista.delete(0, tk.END)
    for r in db.execute("SELECT * FROM alumnos"):
        lista.insert(tk.END, f"{r[0]} - {r[1]} - {r[2]} - {r[3]}")

def guardar():
    if e_nombre.get()=="": return
    db.execute("INSERT INTO alumnos (nombre, grupo, correo) VALUES (?,?,?)", (e_nombre.get(), e_grupo.get(), e_correo.get()))
    db.commit(); mostrar()
    messagebox.showinfo("Listo", "Alumno guardado")
    e_nombre.delete(0, tk.END); e_grupo.delete(0, tk.END); e_correo.delete(0, tk.END)

def borrar():
    sel = lista.curselection()
    if not sel: return
    id_borrar = lista.get(sel[0]).split(" - ")[0]
    db.execute("DELETE FROM alumnos WHERE id=?", (id_borrar,)); db.commit(); mostrar()

tk.Button(ventana, text="Guardar Alumno", bg="green", fg="white", command=guardar).pack(pady=5)
tk.Button(ventana, text="Borrar seleccionado", bg="red", fg="white", command=borrar).pack()
mostrar()
ventana.mainloop()