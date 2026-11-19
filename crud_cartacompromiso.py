#itzel rosas galvan
import mysql.connector, tkinter as tk
from tkinter import messagebox
db = mysql.connector.connect(host="localhost", user="root", password="", database="escuela")
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS carta_compromiso (id INT AUTO_INCREMENT PRIMARY KEY, alumno VARCHAR(100), tutor VARCHAR(100), compromiso VARCHAR(200))")
ventana = tk.Tk(); ventana.title("CRUD Carta Compromiso"); ventana.geometry("400x500")
tk.Label(ventana, text="CRUD Carta Compromiso", font=("Arial", 14, "bold")).pack(pady=10)
tk.Label(ventana, text="Alumno:").pack(); e1 = tk.Entry(ventana, width=30); e1.pack()
tk.Label(ventana, text="Tutor:").pack(); e2 = tk.Entry(ventana, width=30); e2.pack()
tk.Label(ventana, text="Compromiso:").pack(); e3 = tk.Entry(ventana, width=30); e3.pack()
lista = tk.Listbox(ventana, width=50, height=10); lista.pack(pady=10)
def mostrar():
    lista.delete(0, tk.END)
    cursor.execute("SELECT * FROM carta_compromiso")
    for r in cursor.fetchall(): lista.insert(tk.END, f"{r[0]} - {r[1]} - {r[2]} - {r[3]}")
def guardar():
    if e1.get()=="": return
    cursor.execute("INSERT INTO carta_compromiso (alumno, tutor, compromiso) VALUES (%s,%s,%s)", (e1.get(), e2.get(), e3.get())); db.commit(); mostrar(); messagebox.showinfo("Listo","Carta guardada")
    e1.delete(0, tk.END); e2.delete(0, tk.END); e3.delete(0, tk.END)
def borrar():
    sel = lista.curselection()
    if not sel: return
    cursor.execute("DELETE FROM carta_compromiso WHERE id=%s", (lista.get(sel[0]).split(" - ")[0],)); db.commit(); mostrar()
tk.Button(ventana, text="Guardar Carta", bg="green", fg="white", command=guardar).pack(pady=5)
tk.Button(ventana, text="Borrar seleccionado", bg="red", fg="white", command=borrar).pack()
mostrar(); ventana.mainloop()