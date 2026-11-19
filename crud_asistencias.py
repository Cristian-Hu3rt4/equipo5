#yessica odet de los santos gutierrez
import mysql.connector
import tkinter as tk
from tkinter import messagebox

def conectar():
    return mysql.connector.connect(host="localhost", user="root", password="", database="302")
def guardar():
    try:
        con = conectar(); cur = con.cursor()
        cur.execute("INSERT INTO asistencias (id_alumno, fecha, estado) VALUES (%s, %s, %s)", (id_alumno.get(), fecha.get(), estado.get()))
        con.commit(); cur.close(); con.close()
        messagebox.showinfo("ASISTENCIAS", "Guardado"); consultar(); limpiar()
    except Exception as e: messagebox.showerror("Error", str(e))
def consultar():
    try:
        con = conectar(); cur = con.cursor()
        cur.execute("SELECT id_asistencia, id_alumno, fecha, estado FROM asistencias")
        filas = cur.fetchall(); cur.close(); con.close()
        lista.delete(0, tk.END)
        for f in filas: lista.insert(tk.END, f"{f[0]} | {f[1]} | {f[2]} | {f[3]}")
    except Exception as e: messagebox.showerror("Error", str(e))

def actualizar():
    try:
        con = conectar(); cur = con.cursor()
        cur.execute("UPDATE asistencias SET id_alumno=%s, fecha=%s, estado=%s WHERE id_asistencia=%s", (id_alumno.get(), fecha.get(), estado.get(), id_asistencia.get()))
        con.commit(); cur.close(); con.close()
        messagebox.showinfo("ASISTENCIAS", "Actualizado"); consultar(); limpiar()
    except Exception as e: messagebox.showerror("Error", str(e))
def eliminar():
    try:
        con = conectar(); cur = con.cursor()
        cur.execute("DELETE FROM asistencias WHERE id_asistencia=%s", (id_asistencia.get(),))
        con.commit(); cur.close(); con.close()
        messagebox.showinfo("ASISTENCIAS", "Eliminado"); consultar(); limpiar()
    except Exception as e: messagebox.showerror("Error", str(e))

def limpiar():
    id_asistencia.delete(0, tk.END); id_alumno.delete(0, tk.END); fecha.delete(0, tk.END); estado.delete(0, tk.END)

def seleccionar(event):
    try:
        p = lista.get(lista.curselection()).split(" | ")
        id_asistencia.delete(0, tk.END); id_asistencia.insert(0, p[0])
        id_alumno.delete(0, tk.END); id_alumno.insert(0, p[1])
        fecha.delete(0, tk.END); fecha.insert(0, p[2])
        estado.delete(0, tk.END); estado.insert(0, p[3])
    except: pass

FONDO = "#FFE4EC"; ROSA_FUERTE = "#FF5C8A"; BLANCO = "#FFFFFF"; TEXTO = "#4A0E2E"; ENTRADA = "#FFF0F5"
ventana = tk.Tk(); ventana.title("ASISTENCIAS - 302"); ventana.geometry("380x450"); ventana.configure(bg=FONDO)
tk.Label(ventana, text="Id Asistencia", bg=FONDO, fg=TEXTO, font=("Arial", 10, "bold")).grid(row=0, column=0, padx=6, pady=4, sticky="w")
id_asistencia = tk.Entry(ventana, bg=ENTRADA, fg=TEXTO, relief="flat", font=("Arial", 10)); id_asistencia.grid(row=0, column=1, padx=6, pady=4)
tk.Label(ventana, text="Id Alumno", bg=FONDO, fg=TEXTO, font=("Arial", 10, "bold")).grid(row=1, column=0, padx=6, pady=4, sticky="w")
id_alumno = tk.Entry(ventana, bg=ENTRADA, fg=TEXTO, relief="flat", font=("Arial", 10)); id_alumno.grid(row=1, column=1, padx=6, pady=4)
tk.Label(ventana, text="Fecha (AAAA-MM-DD)", bg=FONDO, fg=TEXTO, font=("Arial", 10, "bold")).grid(row=2, column=0, padx=6, pady=4, sticky="w")
fecha = tk.Entry(ventana, bg=ENTRADA, fg=TEXTO, relief="flat", font=("Arial", 10)); fecha.grid(row=2, column=1, padx=6, pady=4)
tk.Label(ventana, text="Estado", bg=FONDO, fg=TEXTO, font=("Arial", 10, "bold")).grid(row=3, column=0, padx=6, pady=4, sticky="w")
estado = tk.Entry(ventana, bg=ENTRADA, fg=TEXTO, relief="flat", font=("Arial", 10)); estado.grid(row=3, column=1, padx=6, pady=4)
lista = tk.Listbox(ventana, width=45, bg=BLANCO, fg=TEXTO, selectbackground=ROSA_FUERTE, selectforeground="white", relief="flat", font=("Arial", 10)); lista.grid(row=4, column=0, columnspan=2, padx=6, pady=6); lista.bind("<<ListboxSelect>>", seleccionar)
tk.Button(ventana, text="Guardar", command=guardar, bg=ROSA_FUERTE, fg="white", relief="flat", font=("Arial", 10, "bold")).grid(row=5, column=0, pady=4, sticky="ew", padx=6)
tk.Button(ventana, text="Consultar", command=consultar, bg=ROSA_FUERTE, fg="white", relief="flat", font=("Arial", 10, "bold")).grid(row=5, column=1, pady=4, sticky="ew", padx=6)
tk.Button(ventana, text="Actualizar", command=actualizar, bg=ROSA_FUERTE, fg="white", relief="flat", font=("Arial", 10, "bold")).grid(row=6, column=0, pady=4, sticky="ew", padx=6)
tk.Button(ventana, text="Eliminar", command=eliminar, bg=ROSA_FUERTE, fg="white", relief="flat", font=("Arial", 10, "bold")).grid(row=6, column=1, pady=4, sticky="ew", padx=6)
ventana.mainloop()