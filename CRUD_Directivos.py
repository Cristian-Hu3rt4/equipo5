import sqlite3, tkinter as tk
from tkinter import messagebox
db = sqlite3.connect('escuela.db')
db.execute("CREATE TABLE IF NOT EXISTS directivo (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, cargo TEXT, correo TEXT)")
ventana = tk.Tk(); ventana.title("CRUD Directivo"); ventana.geometry("400x500")
tk.Label(ventana, text="CRUD Directivo", font=("Arial", 16, "bold")).pack(pady=10)
tk.Label(ventana, text="Nombre:").pack(); e1 = tk.Entry(ventana, width=30); e1.pack()
tk.Label(ventana, text="Cargo:").pack(); e2 = tk.Entry(ventana, width=30); e2.pack()
tk.Label(ventana, text="Correo:").pack(); e3 = tk.Entry(ventana, width=30); e3.pack()
lista = tk.Listbox(ventana, width=50, height=10); lista.pack(pady=10)
def mostrar():
    lista.delete(0, tk.END)
    for r in db.execute("SELECT * FROM directivo"): lista.insert(tk.END, f"{r[0]} - {r[1]} - {r[2]} - {r[3]}")
def guardar():
    if e1.get()=="": return
    db.execute("INSERT INTO directivo (nombre, cargo, correo) VALUES (?,?,?)", (e1.get(), e2.get(), e3.get())); db.commit(); mostrar(); messagebox.showinfo("Listo","Directivo guardado")
    e1.delete(0, tk.END); e2.delete(0, tk.END); e3.delete(0, tk.END)
def borrar():
    sel = lista.curselection()
    if not sel: return
    db.execute("DELETE FROM directivo WHERE id=?", (lista.get(sel[0]).split(" - ")[0],)); db.commit(); mostrar()
tk.Button(ventana, text="Guardar Directivo", bg="green", fg="white", command=guardar).pack(pady=5)
tk.Button(ventana, text="Borrar seleccionado", bg="red", fg="white", command=borrar).pack()
mostrar(); ventana.mainloop()
