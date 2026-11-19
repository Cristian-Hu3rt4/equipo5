#miguel sanchez salazar
import mysql.connector
import tkinter as tk
from tkinter import messagebox

def conectar():
    return mysql.connector.connect(host="localhost", user="root", password="", database="302")

def guardar():
    try:
        con = conectar(); cur = con.cursor()
        cur.execute("INSERT INTO incidencias (id_alumno, id_docente, fecha, descripcion) VALUES (%s, %s, %s, %s)", (id_alumno.get(), id_docente.get(), fecha.get(), descripcion.get()))
        con.commit(); cur.close(); con.close()
        messagebox.showinfo("INCIDENCIAS", "Guardado"); consultar(); limpiar()
    except Exception as e: messagebox.showerror("Error", str(e))

def consultar():
    try:
        con = conectar(); cur = con.cursor()
        cur.execute("SELECT id_incidencia, id_alumno, id_docente, fecha, descripcion FROM incidencias")
        filas = cur.fetchall(); cur.close(); con.close()
        lista.delete(0, tk.END)
        for f in filas: lista.insert(tk.END, f"{f[0]} | {f[1]} | {f[2]} | {f[3]} | {f[4]}")
    except Exception as e: messagebox.showerror("Error", str(e))

def actualizar():
    try:
        con = conectar(); cur = con.cursor()
        cur.execute("UPDATE incidencias SET id_alumno=%s, id_docente=%s, fecha=%s, descripcion=%s WHERE id_incidencia=%s", (id_alumno.get(), id_docente.get(), fecha.get(), descripcion.get(), id_incidencia.get()))
        con.commit(); cur.close(); con.close()
        messagebox.showinfo("INCIDENCIAS", "Actualizado"); consultar(); limpiar()
    except Exception as e: messagebox.showerror("Error", str(e))

def eliminar():
    try:
        con = conectar(); cur = con.cursor()
        cur.execute("DELETE FROM incidencias WHERE id_incidencia=%s", (id_incidencia.get(),))
        con.commit(); cur.close(); con.close()
        messagebox.showinfo("INCIDENCIAS", "Eliminado"); consultar(); limpiar()
    except Exception as e: messagebox.showerror("Error", str(e))

def limpiar():
    id_incidencia.delete(0, tk.END); id_alumno.delete(0, tk.END); id_docente.delete(0, tk.END); fecha.delete(0, tk.END); descripcion.delete(0, tk.END)

def seleccionar(event):
    try:
        p = lista.get(lista.curselection()).split(" | ")
        id_incidencia.delete(0, tk.END); id_incidencia.insert(0, p[0])
        id_alumno.delete(0, tk.END); id_alumno.insert(0, p[1])
        id_docente.delete(0, tk.END); id_docente.insert(0, p[2])
        fecha.delete(0, tk.END); fecha.insert(0, p[3])
        descripcion.delete(0, tk.END); descripcion.insert(0, p[4])
    except: pass

FONDO = "#FFE4EC"; ROSA_FUERTE = "#FF5C8A"; BLANCO = "#FFFFFF"; TEXTO = "#4A0E2E"; ENTRADA = "#FFF0F5"
ventana = tk.Tk(); ventana.title("INCIDENCIAS - 302"); ventana.geometry("420x480"); ventana.configure(bg=FONDO)
tk.Label(ventana, text="Id Incidencia", bg=FONDO, fg=TEXTO, font=("Arial", 10, "bold")).grid(row=0, column=0, padx=6, pady=4, sticky="w")
id_incidencia = tk.Entry(ventana, bg=ENTRADA, fg=TEXTO, relief="flat", font=("Arial", 10)); id_incidencia.grid(row=0, column=1, padx=6, pady=4)
tk.Label(ventana, text="Id Alumno", bg=FONDO, fg=TEXTO, font=("Arial", 10, "bold")).grid(row=1, column=0, padx=6, pady=4, sticky="w")
id_alumno = tk.Entry(ventana, bg=ENTRADA, fg=TEXTO, relief="flat", font=("Arial", 10)); id_alumno.grid(row=1, column=1, padx=6, pady=4)
tk.Label(ventana, text="Id Docente", bg=FONDO, fg=TEXTO, font=("Arial", 10, "bold")).grid(row=2, column=0, padx=6, pady=4, sticky="w")
id_docente = tk.Entry(ventana, bg=ENTRADA, fg=TEXTO, relief="flat", font=("Arial", 10)); id_docente.grid(row=2, column=1, padx=6, pady=4)
tk.Label(ventana, text="Fecha (AAAA-MM-DD)", bg=FONDO, fg=TEXTO, font=("Arial", 10, "bold")).grid(row=3, column=0, padx=6, pady=4, sticky="w")
fecha = tk.Entry(ventana, bg=ENTRADA, fg=TEXTO, relief="flat", font=("Arial", 10)); fecha.grid(row=3, column=1, padx=6, pady=4)
tk.Label(ventana, text="Descripcion", bg=FONDO, fg=TEXTO, font=("Arial", 10, "bold")).grid(row=4, column=0, padx=6, pady=4, sticky="w")
descripcion = tk.Entry(ventana, bg=ENTRADA, fg=TEXTO, relief="flat", font=("Arial", 10)); descripcion.grid(row=4, column=1, padx=6, pady=4)
lista = tk.Listbox(ventana, width=55, bg=BLANCO, fg=TEXTO, selectbackground=ROSA_FUERTE, selectforeground="white", relief="flat", font=("Arial", 10)); lista.grid(row=5, column=0, columnspan=2, padx=6, pady=6); lista.bind("<<ListboxSelect>>", seleccionar)
tk.Button(ventana, text="Guardar", command=guardar, bg=ROSA_FUERTE, fg="white", relief="flat", font=("Arial", 10, "bold")).grid(row=6, column=0, pady=4, sticky="ew", padx=6)
tk.Button(ventana, text="Consultar", command=consultar, bg=ROSA_FUERTE, fg="white", relief="flat", font=("Arial", 10, "bold")).grid(row=6, column=1, pady=4, sticky="ew", padx=6)
tk.Button(ventana, text="Actualizar", command=actualizar, bg=ROSA_FUERTE, fg="white", relief="flat", font=("Arial", 10, "bold")).grid(row=7, column=0, pady=4, sticky="ew", padx=6)
tk.Button(ventana, text="Eliminar", command=eliminar, bg=ROSA_FUERTE, fg="white", relief="flat", font=("Arial", 10, "bold")).grid(row=7, column=1, pady=4, sticky="ew", padx=6)
ventana.mainloop()